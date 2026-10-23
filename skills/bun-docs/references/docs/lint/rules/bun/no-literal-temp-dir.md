# bun/no-literal-temp-dir
Source: https://bun.com/docs/lint/rules/bun/no-literal-temp-dir

Disallow hard-coded temporary directories such as `/tmp` in favor of `os.tmpdir()`


Windows has no `/tmp`, and on other systems `TMPDIR` can point somewhere else, as it does for every user on macOS. A path that starts with `/tmp` ignores that. `os.tmpdir()` returns the directory that the system wants you to use.

The rule reports a string or a template that's one of the directories or starts with one followed by `/`. Text and attribute strings in JSX aren't checked.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-literal-temp-dir" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-literal-temp-dir" = ["error", {
  directories = ["/tmp", "/var/tmp"],
}]
```


## Examples

Reported:

```js
import { writeFileSync } from "node:fs";

writeFileSync("/tmp/report.json", JSON.stringify(report));
writeFileSync(`/var/tmp/${name}.log`, lines.join("\n"));
```

Not reported:

```js
import { writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

writeFileSync(join(tmpdir(), "report.json"), JSON.stringify(report));
```

A name that only begins with the same letters is fine:

```js
const template = "/tmpl/email.html";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `directories` | `["/tmp", "/var/tmp"]` | The directories to report. It replaces the default list. |

```js
const socket = "/private/tmp/worker.sock";
```
