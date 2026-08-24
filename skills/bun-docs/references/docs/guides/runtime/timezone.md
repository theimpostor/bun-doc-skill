# Set a time zone in Bun
Source: https://bun.com/docs/guides/runtime/timezone


Bun supports programmatically setting a default time zone for the lifetime of the `bun` process. Set the `TZ` environment variable to a [valid time zone identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

> Note
When running a file with `bun`, the time zone defaults to your system's configured local time zone.

When running tests with `bun test`, Bun sets the time zone to `UTC` to make tests more deterministic.

**File:** `process.ts`
```ts
process.env.TZ = "America/New_York";
```

***

You can also set `TZ` on the command line when running a Bun command.

```sh
TZ=America/New_York bun run dev
```

***

Once `TZ` is set, every `Date` instance uses that time zone.

**File:** `process.ts`
```ts
new Date().getHours(); // => 18

process.env.TZ = "America/New_York";

new Date().getHours(); // => 21
```
