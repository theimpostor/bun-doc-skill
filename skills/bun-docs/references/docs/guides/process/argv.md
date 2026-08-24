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
[ "/path/to/bun", "/path/to/cli.ts", "--flag1", "--flag2", "value" ]
```

***

To parse `argv` into a more useful format, use `util.parseArgs`.

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

Running `cli.ts` with the same arguments prints the parsed values.

```sh
bun run cli.ts --flag1 --flag2 value
```

```txt
[Object: null prototype] {
  flag1: true,
  flag2: "value",
}
[ "/path/to/bun", "/path/to/cli.ts" ]
```
