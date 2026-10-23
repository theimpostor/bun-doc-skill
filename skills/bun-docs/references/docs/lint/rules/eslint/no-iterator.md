# no-iterator
Source: https://bun.com/docs/lint/rules/eslint/no-iterator

Disallow the `__iterator__` property


No current engine looks at a property called `__iterator__`. An object that defines it isn't iterable, and `for (const song of playlist)` throws a `TypeError`. `for...of`, spread and destructuring call `[Symbol.iterator]` instead.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-iterator" = "error" # or "warn"
```


## Examples

Reported:

```js
Playlist.prototype.__iterator__ = function () {
  return new SongIterator(this);
};

const iterate = playlist["__iterator__"];
```

Not reported:

```js
Playlist.prototype[Symbol.iterator] = function* () {
  yield* this.songs;
};

const iterate = playlist[Symbol.iterator];
```
