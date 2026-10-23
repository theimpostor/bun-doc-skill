# jsx-a11y/no-distracting-elements
Source: https://bun.com/docs/lint/rules/jsx-a11y/no-distracting-elements

Disallow `<marquee>` and `<blink>`


Text that scrolls or flashes by itself is hard to read for people with low vision or a cognitive disability, and they can't pause it. Both elements are also deprecated, and browsers no longer make `<blink>` blink.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/no-distracting-elements" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/no-distracting-elements" = ["error", {
  elements = ["marquee", "blink"],
}]
```


## Examples

Reported:

```jsx
const banner = <marquee>Free shipping this week</marquee>;
const warning = <blink>Sale ends today</blink>;
```

Not reported:

```jsx
const banner = <p className="banner">Free shipping this week</p>;
const warning = <strong>Sale ends today</strong>;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `elements` | `["marquee", "blink"]` | Which of the two elements to report. |

```jsx
const banner = <marquee>Free shipping this week</marquee>;
```
