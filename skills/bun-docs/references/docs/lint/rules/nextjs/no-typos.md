# @next/next/no-typos
Source: https://bun.com/docs/lint/rules/nextjs/no-typos

Disallow misspellings of `getStaticProps`, `getStaticPaths` and `getServerSideProps`


Next.js finds a page's data fetching functions by their exact names. If you export `getStaticProp` or `getserverSideProps`, nothing complains. The function is never called and the page renders without its props.

The rule checks files under a `pages` directory, except `pages/api`. It reports an exported function or variable with a name that's one character away from `getStaticProps`, `getStaticPaths` or `getServerSideProps`.

`--fix-suggestions` corrects the name.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-typos" = "error" # or "warn"
```


## Examples

Reported:

```jsx
export async function getStaticProp() {
  return { props: { posts: await loadPosts() } };
}

export default function Posts({ posts }) {
  return <PostList posts={posts} />;
}
```

```jsx
export const getserverSideProps = async ({ req }) => {
  return { props: { user: await loadUser(req) } };
};
```

Not reported:

```jsx
export async function getStaticProps() {
  return { props: { posts: await loadPosts() } };
}

export default function Posts({ posts }) {
  return <PostList posts={posts} />;
}
```

Outside `pages`, the names mean nothing to Next.js:

```js
export async function getStaticProp() {
  return loadPosts();
}
```
