# react/jsx-fragments
Source: https://bun.com/docs/lint/rules/react/jsx-fragments

Enforce `<>` or `<React.Fragment>` for React fragments


`<>...</>` and `<React.Fragment>...</React.Fragment>` do the same thing. Mixing them makes readers wonder if there's a difference. By default the rule asks for the short form.

A fragment with a prop such as `key` is never reported, because the short form can't take props. A plain `<Fragment>` counts if `Fragment` comes from `"react"` or from `React`.

`--fix` rewrites the fragment to the other form.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-fragments" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-fragments" = ["error", "syntax"] # "syntax" or "element"
```


## Examples

Reported:

```jsx
import React, { Fragment } from "react";

const name = (
  <React.Fragment>
    <First />
    <Last />
  </React.Fragment>
);

const address = (
  <Fragment>
    <Street />
    <City />
  </Fragment>
);
```

Not reported:

```jsx
import React from "react";

const name = (
  <>
    <First />
    <Last />
  </>
);

const rows = users.map(user => (
  <React.Fragment key={user.id}>
    <dt>{user.name}</dt>
    <dd>{user.email}</dd>
  </React.Fragment>
));
```

## Options

| Option | What it does |
| --- | --- |
| `"syntax"` (default) | Require `<>...</>` wherever the fragment has no props. |
| `"element"` | Require `<React.Fragment>...</React.Fragment>`. |

```jsx
const name = (
  <>
    <First />
    <Last />
  </>
);
```

```jsx
import React from "react";

const name = (
  <React.Fragment>
    <First />
    <Last />
  </React.Fragment>
);
```
