# Import a TOML file
Source: https://bun.com/docs/guides/runtime/import-toml


Bun natively supports importing `.toml` files.

**File:** `data.toml`
```toml
name = "bun"
version = "1.0.0"

[author]
name = "John Dough"
email = "john@dough.com"
```

***

Import the file like any other source file.

**File:** `data.ts`
```ts
import data from "./data.toml";

data.name; // => "bun"
data.version; // => "1.0.0"
data.author.name; // => "John Dough"
```

***

See [TypeScript](/docs/runtime/typescript) for more on using TypeScript with Bun.
