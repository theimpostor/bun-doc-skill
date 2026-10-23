# no-self-assign
Source: https://bun.com/docs/lint/rules/eslint/no-self-assign

Disallow assigning a variable or a property to itself


`name = name` does nothing. It's usually left over from a refactor, or a typo for `this.name = name`.

The rule checks `=`, `&&=`, `||=` and `??=`, and looks inside destructuring. `count += count` isn't reported, because it changes the value.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-self-assign" = "off" # or "error"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-self-assign" = ["warn", {
  props = true,
}]
```


## Examples

Reported:

```js
function rename(user, name) {
  name = name;
  user.name = user.name;
  [user, name] = [user, "guest"];
}
```

Not reported:

```js
function rename(user, name) {
  user.name = name;
  [user, name] = [name, user];
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `props` | `true` | Also report properties, such as `user.name = user.name`. |

Turn `props` off if your code assigns a property to itself to run its setter:

```js
video.src = video.src; // loads the video again
```
