# Bun Redis with Upstash
Source: https://bun.com/docs/guides/ecosystem/upstash


[Upstash](https://upstash.com/) is a fully managed Redis database as a service. It works with the Redis® API, so you can connect with Bun's native Redis client.

> Note: TLS is enabled by default for all Upstash Redis databases.

***

### Create a new project
Create a new project with `bun init`:

```sh
bun init bun-upstash-redis
cd bun-upstash-redis
```

### Create an Upstash Redis database
Go to the [Upstash dashboard](https://console.upstash.com/) and create a new Redis database. After completing the [getting started guide](https://upstash.com/docs/redis/overall/getstarted), you'll see your database page with connection information.

The database page displays two connection methods: HTTP and TLS. For Bun's Redis client, you need the **TLS** connection details; the URL starts with `rediss://`.

<img alt="Upstash Redis database page" />

### Connect using Bun's Redis client
Set the `REDIS_URL` environment variable in your `.env` file using the Redis endpoint (not the REST URL):

**File:** `.env`
```ini
REDIS_URL=rediss://********@********.upstash.io:6379
```

Bun's Redis client reads connection information from `REDIS_URL` by default:

**File:** `index.ts`
```ts
import { redis } from "bun";

// Reads from process.env.REDIS_URL automatically
await redis.set("counter", "0");
```

Alternatively, create a custom client with `RedisClient`:

**File:** `index.ts`
```ts
import { RedisClient } from "bun";

const redis = new RedisClient(process.env.REDIS_URL);
```

### Use the Redis client
Use the Redis client to read and write keys in your Upstash database:

**File:** `index.ts`
```ts
import { redis } from "bun";

// Get a value
let counter = await redis.get("counter");

// Set a value if it doesn't exist
if (!counter) {
	await redis.set("counter", "0");
}

// Increment the counter
await redis.incr("counter");

// Get the updated value
counter = await redis.get("counter");
console.log(counter);
```

```txt
1
```

The Redis client handles connections automatically. You don't need to connect or disconnect manually for basic operations.
