# react/no-find-dom-node
Source: https://bun.com/docs/lint/rules/react/no-find-dom-node

Disallow `findDOMNode`


`findDOMNode` reaches into a component and returns whatever DOM node it happens to render first. The caller breaks when the component changes its markup. It doesn't work with function components, React warns about it in strict mode, and React 19 removed it.

Attach a ref to the element you need.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-find-dom-node" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { findDOMNode } from "react-dom";

class SearchBox extends React.Component {
  componentDidMount() {
    findDOMNode(this).focus();
  }

  render() {
    return <input type="search" />;
  }
}
```

Not reported:

```jsx
class SearchBox extends React.Component {
  input = React.createRef();

  componentDidMount() {
    this.input.current.focus();
  }

  render() {
    return <input type="search" ref={this.input} />;
  }
}
```
