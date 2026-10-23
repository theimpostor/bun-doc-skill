# unicorn/prefer-dom-node-remove
Source: https://bun.com/docs/lint/rules/unicorn/prefer-dom-node-remove

Require `child.remove()` instead of `parent.removeChild(child)`


`removeChild()` makes you find a node's parent before you can remove the node, and it throws if that isn't the node's parent. You call `remove()` on the node itself.

`removeChild()` returns the node it removed and `remove()` returns `undefined`. If you need the node afterwards, keep your own reference to it.

The rule doesn't know types. It reports every call to a method named `removeChild` with one argument that could be a node.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-dom-node-remove" = "error" # or "warn"
```


## Examples

Reported:

```js
item.parentNode.removeChild(item);
list.removeChild(list.firstChild);
```

Not reported:

```js
item.remove();
list.firstChild.remove();
```
