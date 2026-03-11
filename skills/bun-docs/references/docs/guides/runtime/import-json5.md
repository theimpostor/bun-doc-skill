# Import a JSON5 file
Source: https://bun.com/docs/guides/runtime/import-json5


Bun natively supports `.json5` imports.

**File:** `config.json5`
```json5
{
  // Comments are allowed
  database: {
    host: "localhost",
    port: 5432,
    name: "myapp",
  },

  server: {
    port: 3000,
    timeout: 30,
  },

  features: {
    auth: true,
    rateLimit: true,
  },
}
```

***

Import the file like any other source file.

**File:** `config.ts`
```ts
import config from "./config.json5";

config.database.host; // => "localhost"
config.server.port; // => 3000
config.features.auth; // => true
```

***

You can also use named imports to destructure top-level properties:

**File:** `config.ts`
```ts
import { database, server, features } from "./config.json5";

console.log(database.name); // => "myapp"
console.log(server.timeout); // => 30
console.log(features.rateLimit); // => true
```

***

For parsing JSON5 strings at runtime, use `Bun.JSON5.parse()`:

**File:** `config.ts`
```ts
const data = JSON5.parse(`{
  name: 'John Doe',
  age: 30,
  hobbies: [
    'reading',
    'coding',
  ],
}`);

console.log(data.name); // => "John Doe"
console.log(data.hobbies); // => ["reading", "coding"]
```

***

See [Docs > API > JSON5](/runtime/json5) for complete documentation on JSON5 support in Bun.
