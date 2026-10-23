# no-multi-str
Source: https://bun.com/docs/lint/rules/eslint/no-multi-str

Disallow strings that continue on the next line with a backslash


A backslash at the end of a line lets a quoted string continue on the next line. The line break is dropped, but the next line's indentation becomes part of the string. One space after the backslash is a syntax error that's hard to see.

Strings in JSX attributes can span lines without a backslash. They aren't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-multi-str" = "error" # or "warn"
```


## Examples

Reported:

```js
const help = "Usage: deploy <target> \
  --dry-run";
```

Not reported:

```js
const help = "Usage: deploy <target> " +
  "--dry-run";

const usage = `Usage: deploy <target>
  --dry-run`;
```

```jsx
const banner = <Banner text="Deploys are paused
  until Monday" />;
```
