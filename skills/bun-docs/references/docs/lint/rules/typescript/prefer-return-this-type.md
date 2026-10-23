# @typescript-eslint/prefer-return-this-type
Source: https://bun.com/docs/lint/rules/typescript/prefer-return-this-type

Require the return type `this` for a method that returns `this`


A method that returns `this` lets you chain calls. If its return type is the class name, the chain breaks for subclasses. `new UserQuery().where("active")` has the type `Query`, so the methods that `UserQuery` adds are gone. With the return type `this`, the call keeps the type of the object it was called on.

The rule checks methods, getters, and fields that hold a function. A member is reported if its return type names the class, it returns `this`, and it never returns another object of the class.

`--fix` replaces the class name with `this`.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-return-this-type" = "error" # or "warn"
```


## Examples

Reported:

```ts
class Query {
  where(condition: string): Query {
    return this;
  }

  limit = (count: number): Query => this;
}
```

Not reported:

```ts
class Query {
  where(condition: string): this {
    return this;
  }

  limit = (count: number): this => this;

  clone(): Query {
    return new Query();
  }
}

class UserQuery extends Query {
  admins() {
    return this.where("admin");
  }
}

new UserQuery().where("active").admins();
```
