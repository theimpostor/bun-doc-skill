# Import a YAML file
Source: https://bun.com/docs/guides/runtime/import-yaml


Bun natively supports `.yaml` and `.yml` imports.

**File:** `config.yaml`
```yaml
database:
  host: localhost
  port: 5432
  name: myapp

server:
  port: 3000
  timeout: 30

features:
  auth: true
  rateLimit: true
```

***

Import the file like any other source file.

**File:** `config.ts`
```ts
import config from "./config.yaml";

config.database.host; // => "localhost"
config.server.port; // => 3000
config.features.auth; // => true
```

***

You can also use named imports to destructure top-level properties:

**File:** `config.ts`
```ts
import { database, server, features } from "./config.yaml";

console.log(database.name); // => "myapp"
console.log(server.timeout); // => 30
console.log(features.rateLimit); // => true
```

***

Bun also supports [Import Attributes](https://github.com/tc39/proposal-import-attributes) syntax:

**File:** `config.ts`
```ts
import config from "./config.yaml" with { type: "yaml" };

config.database.port; // => 5432
```

***

For parsing YAML strings at runtime, use `Bun.YAML.parse()`:

**File:** `config.ts`
```ts
const yamlString = `
name: John Doe
age: 30
hobbies:
  - reading
  - coding
`;

const data = Bun.YAML.parse(yamlString);
console.log(data.name); // => "John Doe"
console.log(data.hobbies); // => ["reading", "coding"]
```

***

## TypeScript Support

To add TypeScript support for your YAML imports, create a declaration file with `.d.ts` appended to the YAML filename (e.g., `config.yaml` → `config.yaml.d.ts`);

**File:** `config.yaml.d.ts`
```ts
const contents: {
  database: {
    host: string;
    port: number;
    name: string;
  };
  server: {
    port: number;
    timeout: number;
  };
  features: {
    auth: boolean;
    rateLimit: boolean;
  };
};

export = contents;
```

***

See [Docs > API > YAML](/runtime/yaml) for complete documentation on YAML support in Bun.
