# react-hooks/memoized-effect-dependencies
Source: https://bun.com/docs/lint/rules/react/memoized-effect-dependencies

Require the dependencies of an effect to be memoized


An object or function that's created during render is new every time, so an effect that depends on it runs after every render. React Compiler has a check for that.

`bun lint` doesn't run that check, so this rule reports nothing. It exists because `eslint-plugin-react-hooks` has a rule with this name, and a config that names it needs to keep working.


## Examples

Not reported:

```jsx
import { useEffect } from "react";

function Chat({ roomId }) {
  const options = { roomId };
  useEffect(() => {
    connect(options);
  }, [options]);
}
```
