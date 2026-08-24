# Bail early with the Bun test runner
Source: https://bun.com/docs/guides/test/bail


Use the `--bail` flag to abort a test run after the first failure, so a continuous integration run fails as early as possible.

```sh
bun test --bail
```

***

To bail after a certain number of failures, pass a number after the flag.

```sh
# bail after 10 failures
bun test --bail=10
```

***

See [`bun test`](/docs/test).
