# jsx-a11y/iframe-has-title
Source: https://bun.com/docs/lint/rules/jsx-a11y/iframe-has-title

Require a `title` on `iframe` elements


A screen reader announces an `iframe` by its `title`. Without one, it reads the URL or says "frame", and the person has to go into the frame to find out whether it's a video, a map or an ad.

An empty string, `null`, `undefined`, a number, `true` and `false` don't count as a title. Neither does a spread, so `<iframe {...props} />` is reported even if `props` has a `title`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/iframe-has-title" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const map = <iframe src={mapUrl} />;
const video = <iframe src={videoUrl} title="" />;
const widget = <iframe {...frameProps} />;
```

Not reported:

```jsx
const map = <iframe src={mapUrl} title="Map of our offices" />;
const video = <iframe src={videoUrl} title={clip.name} />;
const widget = <iframe {...frameProps} title={`Preview of ${page.name}`} />;
```

In braces, the rule accepts a string, a template, a variable, a property such as `clip.name`, a call, `a ? b : c`, and `||`, `&&` or `??`. Any other expression is reported, including a title that's built with `+`, read through `?.` or cast with `as`. Use a template or a variable:

```jsx
const map = <iframe src={mapUrl} title={"Map of " + city} />;
const video = <iframe src={videoUrl} title={clip?.name} />;
```

```jsx
const map = <iframe src={mapUrl} title={`Map of ${city}`} />;
const video = <iframe src={videoUrl} title={clipName} />;
```
