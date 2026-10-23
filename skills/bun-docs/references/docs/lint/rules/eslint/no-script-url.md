# no-script-url
Source: https://bun.com/docs/lint/rules/eslint/no-script-url

Disallow `javascript:` URLs


A browser runs the text after `javascript:` as code when the URL is opened. That's `eval` under another name. The code is a string that no tool checks, and if any part of it comes from a user, it's a way to inject a script.

The rule reports a string or a template literal without `${}` that starts with `javascript:`, in upper or lower case.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-script-url" = "error" # or "warn"
```


## Examples

Reported:

```js
link.href = "javascript:void(0)";
location.href = `JavaScript:save()`;
```

Not reported:

```js
link.addEventListener("click", (event) => {
  event.preventDefault();
  save();
});
```
