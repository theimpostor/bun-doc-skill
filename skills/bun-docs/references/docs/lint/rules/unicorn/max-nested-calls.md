# unicorn/max-nested-calls
Source: https://bun.com/docs/lint/rules/unicorn/max-nested-calls

Enforce a maximum depth of calls nested in the arguments of other calls


Nested calls run from the inside out, so you read `save(normalize(parse(read(file))))` backwards, counting parentheses on the way. Past a few levels, the code is easier to follow if you put a step in the middle into a well-named variable.

A call counts as nested when it's in an argument of another call or of a `new` expression. By default up to 3 levels are allowed, and each deeper call is reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/max-nested-calls" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/max-nested-calls" = ["error", {
  max = 3,
}]
```


## Examples

Reported:

```js
save(normalize(parse(read(file))));
```

Not reported:

```js
const config = parse(read(file));
save(normalize(config));
```

A method chain isn't nesting:

```js
const total = text.trim().split(",").map(Number).filter(Boolean).reduce(add);
```

The count starts again inside a function, a class or JSX:

```js
schedule(retry(withTimeout(() => save(normalize(config)))));
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `max` | `3` | The deepest nesting that's allowed. |

```js
save(normalize(parse(text)));
```

```js
save(normalize(parse(read(file))));
```
