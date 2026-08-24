# Import an XML file
Source: https://bun.com/docs/guides/runtime/import-xml


Bun natively supports `.xml` imports.

**File:** `config.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<config env="production">
  <database host="localhost" port="5432" name="myapp"/>
  <server port="3000" timeout="30"/>
  <feature name="auth"/>
  <feature name="rateLimit"/>
</config>
```

***

Import the file like any other source file. The module is the parsed document: one key for the root element, `"@name"` keys for attributes, and arrays for repeated elements. Every value is a string.

**File:** `config.ts`
```ts
import doc from "./config.xml";

doc.config["@env"]; // => "production"
doc.config.database["@host"]; // => "localhost"
doc.config.server["@port"]; // => "3000"
doc.config.feature.map(f => f["@name"]); // => ["auth", "rateLimit"]
```

***

The root element is also available as a named import:

**File:** `config.ts`
```ts
import { config } from "./config.xml";

console.log(config.database["@name"]); // => "myapp"
console.log(Number(config.server["@timeout"])); // => 30
```

***

For parsing XML strings at runtime, use `Bun.XML.parse()`:

**File:** `config.ts`
```ts
const data = Bun.XML.parse(`
  <user id="7">
    <name>John Doe</name>
    <hobby>reading</hobby>
    <hobby>coding</hobby>
  </user>
`);

console.log(data.user.name); // => "John Doe"
console.log(data.user.hobby); // => ["reading", "coding"]
console.log(data.user["@id"]); // => "7"
```

***

See [XML](/docs/runtime/xml) for the rest of Bun's XML support, including the ordered `{ compact: false }` node tree and `Bun.XML.stringify()`.
