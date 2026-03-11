# Extract links from a webpage using HTMLRewriter
Source: https://bun.com/docs/guides/html-rewriter/extract-links


## Extract links from a webpage

Bun's [HTMLRewriter](/runtime/html-rewriter) API can be used to efficiently extract links from HTML content. It works by chaining together CSS selectors to match the elements, text, and attributes you want to process. This is a simple example of how to extract links from a webpage. You can pass `.transform` a `Response`, `Blob`, or `string`.

**File:** `extract-links.ts`
```ts
async function extractLinks(url: string) {
  const links = new Set<string>();
  const response = await fetch(url);

  const rewriter = new HTMLRewriter().on("a[href]", {
    element(el) {
      const href = el.getAttribute("href");
      if (href) {
        links.add(href);
      }
    },
  });

  // Wait for the response to be processed
  await rewriter.transform(response).blob();
  console.log([...links]); // ["https://bun.com", "/docs", ...]
}

// Extract all links from the Bun website
await extractLinks("https://bun.com");
```

***

## Convert relative URLs to absolute

When scraping websites, you often want to convert relative URLs (like `/docs`) to absolute URLs. Here's how to handle URL resolution:

**File:** `extract-links.ts`
```ts
async function extractLinksFromURL(url: string) {
  const response = await fetch(url);
  const links = new Set<string>();

  const rewriter = new HTMLRewriter().on("a[href]", {
    element(el) {
      const href = el.getAttribute("href");
      if (href) {
        // Convert relative URLs to absolute
        try {
          const absoluteURL = new URL(href, url).href;
          links.add(absoluteURL);
        } catch {
          links.add(href);
        }
      }
    },
  });

  // Wait for the response to be processed
  await rewriter.transform(response).blob();
  return [...links];
}

const websiteLinks = await extractLinksFromURL("https://example.com");
```

***

See [Docs > API > HTMLRewriter](/runtime/html-rewriter) for complete documentation on HTML transformation with Bun.
