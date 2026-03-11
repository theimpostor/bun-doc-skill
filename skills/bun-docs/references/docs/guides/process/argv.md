# Parse command-line arguments
Source: https://bun.com/docs/guides/process/argv


The *argument vector* is the list of arguments passed to the program when it is run. It is available as `Bun.argv`.

**File:** `cli.ts`
```ts
console.log(Bun.argv);
```

***

Running this file with arguments results in the following:

```sh
bun run cli.ts --flag1 --flag2 value
```

```txt
[ '/path/to/bun', '/path/to/cli.ts', '--flag1', '--flag2', 'value' ]
```

***

To parse `argv` into a more useful format, `util.parseArgs` would be helpful.

Example:

**File:** `cli.ts`
```ts
import { parseArgs } from "util";

const { values, positionals } = parseArgs({
  args: Bun.argv,
  options: {
    flag1: {
      type: "boolean",
    },
    flag2: {
      type: "string",
    },
  },
  strict: true,
  allowPositionals: true,
});

console.log(values);
console.log(positionals);
```

***

then it outputs

```sh
bun run cli.ts --flag1 --flag2 value
```

```txt
{
  flag1: true,
  flag2: "value",
}
[ "/path/to/bun", "/path/to/cli.ts" ]
```
