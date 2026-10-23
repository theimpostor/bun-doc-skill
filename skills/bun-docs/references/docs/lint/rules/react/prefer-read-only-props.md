# react/prefer-read-only-props
Source: https://bun.com/docs/lint/rules/react/prefer-read-only-props

Require the props in a component's type to be `readonly`


A component must not change its props. They belong to the parent, and React doesn't render again when you assign to them. If every prop in the type is `readonly`, TypeScript rejects `props.name = "..."` when you compile.

`--fix` adds `readonly` in front of the prop.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/prefer-read-only-props" = "error" # or "warn"
```


## Examples

Reported:

```tsx
type Props = {
  name: string;
  age?: number;
};

function Profile(props: Props) {
  return <p>{props.name} ({props.age})</p>;
}
```

Not reported:

```tsx
type Props = {
  readonly name: string;
  readonly age?: number;
};

function Profile(props: Props) {
  return <p>{props.name} ({props.age})</p>;
}
```

`Readonly<Props>` isn't reported either:

```tsx
type Props = {
  name: string;
  age?: number;
};

function Profile(props: Readonly<Props>) {
  return <p>{props.name} ({props.age})</p>;
}
```
