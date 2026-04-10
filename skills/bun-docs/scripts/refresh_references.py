#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


DEFAULT_URL = "https://bun.sh/llms-full.txt"
SKIP_TAGS = {"Tabs", "CodeGroup", "Frame", "Steps", "Columns", "CardGroup"}
HEADING_TAGS = {"Tab", "Step", "Accordion", "Card"}
ADMONITION_TAGS = {"Note", "Warning", "Info", "Tip", "Callout"}
PARAM_TAG = "ParamField"
CONTROL_CHAR_RE = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]")
INLINE_FENCE_RE = re.compile(r"```(.*?)```")
THEME_LITERAL = 'theme={"theme":{"light":"github-light","dark":"dracula"}}'

SECTION_INFO = {
    "bundler": {
        "title": "Bundler",
        "summary": "Use for `bun build`, executables, CSS bundling, HTML imports, hot reloading, minification, macros, and bundler plugins.",
    },
    "getting-started": {
        "title": "Getting Started",
        "summary": "Use for installation, quickstart, TypeScript support, the Bun overview pages, and general orientation.",
    },
    "guides-binary": {
        "title": "Guides: Binary Data",
        "summary": "Use for conversions among `ArrayBuffer`, `Blob`, `Buffer`, `DataView`, strings, and typed arrays.",
    },
    "guides-deployment": {
        "title": "Guides: Deployment",
        "summary": "Use for deploying Bun apps to AWS Lambda, Cloud Run, Railway, Render, Vercel, and similar targets.",
    },
    "guides-ecosystem": {
        "title": "Guides: Ecosystem",
        "summary": "Use for framework and library integrations such as React, Next.js, Docker, Prisma, Elysia, Hono, and more.",
    },
    "guides-html-rewriter": {
        "title": "Guides: HTMLRewriter",
        "summary": "Use for quick HTMLRewriter examples like extracting links or Open Graph metadata.",
    },
    "guides-http": {
        "title": "Guides: HTTP",
        "summary": "Use for `fetch`, proxies, SSE, file responses, streaming responses, and Bun HTTP server recipes.",
    },
    "guides-index": {
        "title": "Guides Overview",
        "summary": "Use to find the right guide category before opening a specific guide page.",
    },
    "guides-install": {
        "title": "Guides: Package Installation",
        "summary": "Use for `bun add`, `bun install`, registries, scopes, workspaces, lockfiles, and package-manager migration examples.",
    },
    "guides-process": {
        "title": "Guides: Process",
        "summary": "Use for child processes, IPC, argv parsing, stdin/stdout, uptime, and signal handling.",
    },
    "guides-read-file": {
        "title": "Guides: Read File",
        "summary": "Use for file reading recipes like reading JSON, strings, buffers, or streams.",
    },
    "guides-runtime": {
        "title": "Guides: Runtime",
        "summary": "Use for runtime-specific recipes such as `--define`, `bun upgrade`, GitHub Actions, and Bun runtime flags.",
    },
    "guides-streams": {
        "title": "Guides: Streams",
        "summary": "Use for stream conversions between Node streams, `Blob`, `Response`, strings, and typed arrays.",
    },
    "guides-test": {
        "title": "Guides: Test",
        "summary": "Use for focused `bun test` recipes like coverage, concurrency, bail, snapshots, and quiet output.",
    },
    "guides-util": {
        "title": "Guides: Utilities",
        "summary": "Use for utility helpers such as hashing, deep equality, semver checks, shell helpers, and compression.",
    },
    "guides-websocket": {
        "title": "Guides: WebSocket",
        "summary": "Use for Bun WebSocket server examples, pub/sub, compression, and connection context.",
    },
    "guides-write-file": {
        "title": "Guides: Write File",
        "summary": "Use for writing files, appending, copying, piping, and writing binary data.",
    },
    "package-manager": {
        "title": "Package Manager",
        "summary": "Use for Bun package-manager behavior like workspaces, lockfiles, global cache, npmrc, registries, and overrides.",
    },
    "package-manager-cli": {
        "title": "Package Manager CLI",
        "summary": "Use for command-specific docs such as `bun add`, `bun install`, `bun update`, `bun audit`, and `bun publish`.",
    },
    "project": {
        "title": "Project",
        "summary": "Use for Bun project contribution docs, roadmap, benchmarking, bindgen, and building Bun itself.",
    },
    "runtime": {
        "title": "Runtime",
        "summary": "Use for Bun runtime APIs, `bunfig.toml`, file I/O, globals, compatibility, shell, plugins, workers, and built-in services.",
    },
    "runtime-http": {
        "title": "Runtime HTTP",
        "summary": "Use for `Bun.serve`, HTTP routing, TLS, metrics, error handling, cookies, and WebSockets.",
    },
    "runtime-networking": {
        "title": "Runtime Networking",
        "summary": "Use for DNS, `fetch`, TCP, and UDP runtime docs.",
    },
    "runtime-templating": {
        "title": "Runtime Templating",
        "summary": "Use for `bun create` and `bun init` templating docs.",
    },
    "test": {
        "title": "Test Runner",
        "summary": "Use for core `bun test` documentation: writing tests, lifecycle hooks, mocks, snapshots, config, coverage, and reporters.",
    },
}


@dataclass
class Page:
    title: str
    source: str
    lines: list[str]
    local_path: Path
    section_key: str
    doc_path: str


def fetch_text(url: str) -> tuple[str, str]:
    request = Request(url, headers={"User-Agent": "codex-bun-docs-skill/1.0"})
    with urlopen(request) as response:
        return response.read().decode("utf-8"), response.geturl()


def find_page_starts(lines: list[str]) -> list[int]:
    starts: list[int] = []
    for index, line in enumerate(lines):
        if not line.startswith("# "):
            continue
        probe = index + 1
        while probe < len(lines) and not lines[probe].strip():
            probe += 1
        if probe < len(lines) and lines[probe].startswith("Source: "):
            starts.append(index)
    return starts


def doc_path_from_source(source: str) -> str:
    parts = [part for part in urlparse(source).path.split("/") if part]
    if len(parts) < 2 or parts[0] != "docs":
        raise ValueError(f"Unexpected Bun docs path: {source}")
    return "/".join(parts[1:])


def section_key_from_doc_path(doc_path: str) -> str:
    parts = doc_path.split("/")
    if parts[0] in {"index", "installation", "quickstart"}:
        return "getting-started"
    if re.fullmatch(r"typescript(?:-\d+)?", parts[0]):
        return "getting-started"
    if parts[0] == "feedback":
        return "getting-started"
    if parts[0] == "bundler":
        return "bundler"
    if parts[0] == "runtime":
        if len(parts) > 1 and parts[1] in {"http", "networking", "templating"}:
            return f"runtime-{parts[1]}"
        return "runtime"
    if parts[0] == "pm":
        if len(parts) > 1 and parts[1] == "cli":
            return "package-manager-cli"
        return "package-manager"
    if parts[0] == "test":
        return "test"
    if parts[0] == "project":
        return "project"
    if parts[0] == "guides":
        if len(parts) == 1:
            return "guides-index"
        return f"guides-{parts[1]}"
    return parts[0]


def local_path_from_doc_path(doc_path: str) -> Path:
    return Path("docs") / Path(doc_path).with_suffix(".md")


def parse_pages(text: str) -> list[Page]:
    lines = text.splitlines()
    starts = find_page_starts(lines)
    pages: list[Page] = []
    for page_index, start in enumerate(starts):
        end = starts[page_index + 1] if page_index + 1 < len(starts) else len(lines)
        block = lines[start:end]
        title = block[0][2:].strip()
        source_line = next(
            line for line in block[1:6] if line.startswith("Source: ")
        )
        source = source_line.removeprefix("Source: ").strip()
        doc_path = doc_path_from_source(source)
        pages.append(
            Page(
                title=title,
                source=source,
                lines=block,
                local_path=local_path_from_doc_path(doc_path),
                section_key=section_key_from_doc_path(doc_path),
                doc_path=doc_path,
            )
        )
    return pages


def clean_inline(text: str) -> str:
    cleaned = CONTROL_CHAR_RE.sub("", html.unescape(text))
    cleaned = re.sub(r"<code>(.*?)</code>", lambda match: f"`{match.group(1)}`", cleaned)
    cleaned = re.sub(r"</?span[^>]*>", "", cleaned)
    cleaned = re.sub(r"<br\s*/?>", "<br>", cleaned)
    cleaned = re.sub(r"\\([`*_{}\[\]()#+\-.!|$])", r"\1", cleaned)
    return cleaned.strip()


def extract_title_attr(text: str) -> str | None:
    title_match = re.search(r'title="([^"]+)"', text)
    if title_match:
        return clean_inline(title_match.group(1))
    title_match = re.search(r"title=\{(.+?)\}", text)
    if title_match:
        return clean_inline(title_match.group(1))
    return None


def extract_href_attr(text: str) -> str | None:
    href_match = re.search(r'href="([^"]+)"', text)
    if href_match:
        return clean_inline(href_match.group(1))
    return None


def strip_code_markers(text: str) -> str:
    cleaned = re.sub(r"\s*//\s*\[!code [^\]]+\]", "", text)
    cleaned = re.sub(r"\s*#\s*\[!code [^\]]+\]", "", cleaned)
    cleaned = re.sub(r"\s*<!--\s*\[!code [^\]]+\]\s*-->", "", cleaned)
    return cleaned


def normalize_inline_fences(text: str) -> str:
    def replacer(match: re.Match[str]) -> str:
        body = CONTROL_CHAR_RE.sub("", match.group(1)).strip()
        _language, _sep, remainder = body.partition(" ")
        snippet = remainder.strip() if remainder else body
        snippet = snippet.replace(THEME_LITERAL, "")
        snippet = re.sub(r'\s+icon="[^"]*"', "", snippet)
        snippet = re.sub(r'\s+title="[^"]*"', "", snippet)
        snippet = re.sub(r"\bterminal\b", "", snippet)
        snippet = re.sub(r"\s{2,}", " ", snippet).strip()
        first_token, sep, tail = snippet.partition(" ")
        if first_token and "." in first_token and "=" not in first_token and sep:
            snippet = tail.strip()
        snippet = CONTROL_CHAR_RE.sub("", strip_code_markers(snippet)).strip()
        return f"`{snippet}`" if snippet else ""

    previous = None
    current = text
    while previous != current:
        previous = current
        current = INLINE_FENCE_RE.sub(replacer, current)
    return current


def parse_fence_header(header_line: str) -> tuple[str, str | None]:
    content = header_line.lstrip()[3:].strip()
    if not content:
        return "", None
    language = content.split()[0]
    title = extract_title_attr(content)
    if title is None:
        remaining = content[len(language) :].strip()
        if remaining:
            token = remaining.split()[0]
            if "=" not in token and token not in {"terminal"}:
                title = token
    return language, title


def flush_param_field(field_type: str | None, lines: list[str], output: list[str]) -> None:
    content = " ".join(line for line in lines if line).strip()
    content = normalize_inline_fences(content)
    content = re.sub(
        r"<(Note|Warning|Info|Tip|Callout)\b[^>]*>(.*?)</\1>",
        lambda match: f"{'Note' if match.group(1) == 'Callout' else match.group(1)}: {clean_inline(match.group(2))}",
        content,
    )
    content = clean_inline(strip_code_markers(content))
    content = re.sub(r"\s{2,}", " ", content).strip()
    if not content:
        return
    prefix = f"- ({field_type}) " if field_type else "- "
    output.append(prefix + content)


def clean_page_lines(lines: list[str]) -> list[str]:
    output: list[str] = []
    in_code = False
    code_indent = 0
    block_tag: str | None = None
    block_lines: list[str] = []
    block_meta: dict[str, str] = {}

    for raw_line in lines:
        lstripped = raw_line.lstrip()
        stripped = raw_line.strip()
        indent = len(raw_line) - len(lstripped)

        if in_code:
            if lstripped.startswith("```"):
                output.append("```")
                in_code = False
                code_indent = 0
                continue
            if raw_line.startswith(" " * code_indent):
                output.append(CONTROL_CHAR_RE.sub("", strip_code_markers(raw_line[code_indent:])))
            else:
                output.append(CONTROL_CHAR_RE.sub("", strip_code_markers(lstripped if code_indent else raw_line)))
            continue

        if block_tag is not None:
            if stripped == f"</{block_tag}>":
                if block_tag == PARAM_TAG:
                    flush_param_field(block_meta.get("type"), block_lines, output)
                block_tag = None
                block_lines = []
                block_meta = {}
                continue
            cleaned = clean_inline(stripped)
            if cleaned:
                block_lines.append(cleaned)
            elif block_lines and block_lines[-1] != "":
                block_lines.append("")
            continue

        if lstripped.startswith("```"):
            language, title = parse_fence_header(lstripped)
            if title:
                output.append(f"**File:** `{title}`")
            output.append(f"```{language}".rstrip())
            in_code = True
            code_indent = indent
            continue

        if not stripped:
            output.append("")
            continue

        inline_admonition = re.fullmatch(
            r"<(Note|Warning|Info|Tip|Callout)\b[^>]*>(.*)</\1>", stripped
        )
        if inline_admonition:
            label = "Note" if inline_admonition.group(1) == "Callout" else inline_admonition.group(1)
            output.append(
                f"> {label}: {clean_inline(inline_admonition.group(2))}"
            )
            continue

        if stripped in {f"<{tag}>" for tag in SKIP_TAGS} | {f"</{tag}>" for tag in SKIP_TAGS}:
            continue

        heading_match = re.match(r"<(Tab|Step|Accordion|Card)\b.*?>", stripped)
        if heading_match:
            title = extract_title_attr(stripped)
            if title:
                output.append(f"### {title}")
            href = extract_href_attr(stripped)
            if href:
                output.append(f"Link: `{href}`")
            continue

        if stripped in {f"</{tag}>" for tag in HEADING_TAGS}:
            continue

        admonition_open = re.fullmatch(r"<(Note|Warning|Info|Tip|Callout)\b[^>]*>", stripped)
        if admonition_open:
            label = "Note" if admonition_open.group(1) == "Callout" else admonition_open.group(1)
            output.append(f"> {label}")
            continue

        if stripped in {f"</{tag}>" for tag in ADMONITION_TAGS}:
            continue

        param_open = re.fullmatch(r'<ParamField(?: type="([^"]+)")?>', stripped)
        if param_open:
            block_tag = PARAM_TAG
            block_lines = []
            block_meta = {"type": param_open.group(1) or ""}
            continue

        if stripped == "</ParamField>":
            continue

        cleaned = clean_inline(raw_line)
        if cleaned:
            output.append(cleaned)

    if block_tag is not None:
        if block_tag == PARAM_TAG:
            flush_param_field(block_meta.get("type"), block_lines, output)

    while output and output[0] == "":
        output.pop(0)
    while output and output[-1] == "":
        output.pop()

    collapsed: list[str] = []
    blank_run = 0
    for line in output:
        if line == "":
            blank_run += 1
            if blank_run <= 2:
                collapsed.append(line)
            continue
        blank_run = 0
        collapsed.append(line)
    return collapsed


def ensure_clean_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def relative_doc_link(local_path: Path) -> str:
    return "../" + local_path.as_posix()


def slug_title(key: str) -> str:
    return key.replace("-", " ").title()


def write_section_files(references_dir: Path, pages: list[Page]) -> list[tuple[str, int]]:
    sections_dir = references_dir / "sections"
    sections_dir.mkdir(parents=True, exist_ok=True)

    grouped: dict[str, list[Page]] = defaultdict(list)
    for page in pages:
        grouped[page.section_key].append(page)

    section_index: list[tuple[str, int]] = []
    for key in sorted(grouped):
        info = SECTION_INFO.get(key, {"title": slug_title(key), "summary": ""})
        pages_for_section = sorted(grouped[key], key=lambda page: page.doc_path)
        lines = [f"# {info['title']}", ""]
        if info["summary"]:
            lines.extend([info["summary"], ""])
        lines.extend(
            [
                "Use this file to pick the most relevant Bun doc page before opening the page itself.",
                "",
                "## Pages",
                "",
            ]
        )
        for page in pages_for_section:
            lines.append(
                f"- [{page.title}]({relative_doc_link(page.local_path)}) - `{page.doc_path}`"
            )
        lines.append("")
        (sections_dir / f"{key}.md").write_text("\n".join(lines), encoding="utf-8")
        section_index.append((key, len(pages_for_section)))
    return section_index


def write_index_file(
    references_dir: Path,
    section_index: list[tuple[str, int]],
    page_count: int,
    requested_url: str,
    resolved_url: str,
) -> None:
    lines = [
        "# Bun Docs Reference Index",
        "",
        "This reference tree mirrors Bun's official docs and is intended to be read selectively.",
        "",
        "## How to use this reference",
        "",
        "1. Open the section overview that best matches the user's question.",
        "2. From that section file, open only the most relevant page file under `references/docs/...`.",
        "3. Prefer the smallest page set that fully answers the question.",
        "",
        "## Snapshot",
        "",
        f"- Requested URL: `{requested_url}`",
        f"- Resolved URL: `{resolved_url}`",
        f"- Generated: `{datetime.now(timezone.utc).isoformat()}`",
        f"- Page count: `{page_count}`",
        "",
        "## Sections",
        "",
    ]
    for key, count in section_index:
        info = SECTION_INFO.get(key, {"title": slug_title(key), "summary": ""})
        summary_suffix = f" {info['summary']}" if info["summary"] else ""
        lines.append(
            f"- [{info['title']}](sections/{key}.md) - `{count}` pages.{summary_suffix}"
        )
    lines.append("")
    lines.append("The full cleaned page mirror lives under `references/docs/`.")
    lines.append("")
    (references_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")


def write_metadata_file(
    references_dir: Path, pages: list[Page], requested_url: str, resolved_url: str
) -> None:
    metadata = {
        "requested_url": requested_url,
        "resolved_url": resolved_url,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "page_count": len(pages),
        "sections": sorted({page.section_key for page in pages}),
    }
    (references_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )


def write_page_files(references_dir: Path, pages: list[Page]) -> None:
    docs_dir = references_dir / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    for page in pages:
        destination = references_dir / page.local_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        cleaned = clean_page_lines(page.lines)
        destination.write_text("\n".join(cleaned) + "\n", encoding="utf-8")


def build_references(url: str, references_dir: Path) -> None:
    text, resolved_url = fetch_text(url)
    pages = parse_pages(text)
    ensure_clean_directory(references_dir / "docs")
    ensure_clean_directory(references_dir / "sections")
    write_page_files(references_dir, pages)
    section_index = write_section_files(references_dir, pages)
    write_index_file(references_dir, section_index, len(pages), url, resolved_url)
    write_metadata_file(references_dir, pages, url, resolved_url)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download and clean Bun's llms-full docs into skill reference files."
    )
    parser.add_argument("--url", default=DEFAULT_URL, help="Bun docs source URL")
    parser.add_argument(
        "--references-dir",
        default=str(Path(__file__).resolve().parents[1] / "references"),
        help="Directory where cleaned references should be written",
    )
    args = parser.parse_args()
    build_references(args.url, Path(args.references_dir))


if __name__ == "__main__":
    main()
