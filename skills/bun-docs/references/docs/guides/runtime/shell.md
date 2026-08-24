# Run a Shell Command
Source: https://bun.com/docs/guides/runtime/shell


Bun Shell is a cross-platform bash-like shell built into Bun.

It runs shell commands from JavaScript and TypeScript. To get started, import the `$` function from the `bun` package.

**File:** `foo.ts`
```ts
import { $ } from "bun";

await $`echo Hello, world!`; // => "Hello, world!"
```

***

The `$` function is a tagged template literal that runs the command and returns a promise that resolves with the command's output.

**File:** `foo.ts`
```ts
import { $ } from "bun";

const output = await $`ls -l`.text();
console.log(output);
```

***

To iterate over each line of the output, use the `lines` method.

**File:** `foo.ts`
```ts
import { $ } from "bun";

for await (const line of $`ls -l`.lines()) {
  console.log(line);
}
```

***

See [Bun Shell](/docs/runtime/shell).
