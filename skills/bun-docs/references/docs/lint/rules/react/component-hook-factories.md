# react-hooks/component-hook-factories
Source: https://bun.com/docs/lint/rules/react/component-hook-factories

Deprecated: reports nothing, and is kept so that older configs still load


This rule reports nothing. It was about functions that create a component or a hook each time they're called, and `eslint-plugin-react-hooks` removed the check in version 7.1.0 but kept the name. `bun lint` does the same, so a config that still mentions the rule keeps working.

You can delete it from your config.


## Examples

Not reported:

```jsx
function makeButton(color) {
  return function Button({ children }) {
    return <button type="button" style={{ color }}>{children}</button>;
  };
}
```
