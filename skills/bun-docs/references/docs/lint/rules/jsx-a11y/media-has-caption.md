# jsx-a11y/media-has-caption
Source: https://bun.com/docs/lint/rules/jsx-a11y/media-has-caption

Require `<audio>` and `<video>` to have a `<track>` with captions


People who are deaf or hard of hearing, or who watch with the sound off, can't follow a video or a recording without captions.

An `<audio>` or `<video>` needs a direct child `<track kind="captions">`. A `muted` element has no sound to caption, so it isn't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/media-has-caption" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/media-has-caption" = ["error", {
  audio = [],
  video = [], # list of strings
  track = [], # list of strings
}]
```


## Examples

Reported:

```jsx
const player = <video src="/intro.mp4" controls />;
```

A track of another kind doesn't count:

```jsx
const player = (
  <video src="/intro.mp4" controls>
    <track kind="subtitles" src="/intro.fr.vtt" />
  </video>
);
```

Not reported:

```jsx
const player = (
  <video src="/intro.mp4" controls>
    <track kind="captions" src="/intro.en.vtt" />
  </video>
);

const background = <video src="/waves.mp4" autoPlay muted />;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `audio` | `[]` | Components to check as if they were `<audio>`. |
| `video` | `[]` | Components to check as if they were `<video>`. |
| `track` | `[]` | Components that count as `<track>`. |

```jsx
const player = <Player src="/intro.mp4" />;
```

```jsx
const player = (
  <Player src="/intro.mp4">
    <Captions kind="captions" src="/intro.en.vtt" />
  </Player>
);
```
