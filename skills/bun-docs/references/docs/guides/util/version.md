# Get the current Bun version
Source: https://bun.com/docs/guides/util/version


`Bun.version` contains the current version of Bun in semver format.

**File:** `index.ts`
```ts
Bun.version; // => "1.3.3"
```

***

`Bun.revision` contains the exact `git` commit of [`oven-sh/bun`](https://github.com/oven-sh/bun) that was compiled to produce this Bun binary.

**File:** `index.ts`
```ts
Bun.revision; // => "49231b2cb9aa48497ab966fc0bb6b742dacc4994"
```

***

See [Utils](/docs/runtime/utils).
