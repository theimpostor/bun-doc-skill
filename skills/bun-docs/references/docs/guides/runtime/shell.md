# Run a Shell Command
Source: https://bun.com/docs/guides/runtime/shell


Bun Shell is a cross-platform bash-like shell built in to Bun.

It runs shell commands in JavaScript and TypeScript. To get started, import the `$` function from the `bun` package and use it to run shell commands.

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

To get each line of the output as an array, use the `lines` method.

**File:** `foo.ts`
```ts
import { $ } from "bun";

for await (const line of $`ls -l`.lines()) {
  console.log(line);
}
```

***

See [Docs > API > Shell](/runtime/shell) for complete documentation.
