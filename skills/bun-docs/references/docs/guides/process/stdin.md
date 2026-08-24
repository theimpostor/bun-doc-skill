# Read from stdin
Source: https://bun.com/docs/guides/process/stdin


In Bun, the `console` object is an `AsyncIterable` that yields lines from `stdin`.

**File:** `index.ts`
```ts
const prompt = "Type something: ";
process.stdout.write(prompt);
for await (const line of console) {
  console.log(`You typed: ${line}`);
  process.stdout.write(prompt);
}
```

***

Running this file starts a never-ending interactive prompt that echoes whatever you type.

```sh
bun run index.ts
```

```txt
Type something: hello
You typed: hello
Type something: hello again
You typed: hello again
```

***

Bun also exposes `stdin` as a `BunFile`, `Bun.stdin`. Use it to incrementally read large inputs piped into the `bun` process.

Chunks aren't guaranteed to be split line-by-line.

**File:** `stdin.ts`
```ts
for await (const chunk of Bun.stdin.stream()) {
  // chunk is Uint8Array
  // this converts it to text (assumes UTF-8 encoding)
  const chunkText = Buffer.from(chunk).toString();
  console.log(`Chunk: ${chunkText}`);
}
```

***

Running `stdin.ts` prints whatever is piped into it.

```sh
echo "hello" | bun run stdin.ts
```

```txt
Chunk: hello
```

***

See [Utils](/docs/runtime/utils) for more utilities.
