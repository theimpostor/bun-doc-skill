# react/jsx-no-constructed-context-values
Source: https://bun.com/docs/lint/rules/react/jsx-no-constructed-context-values

Disallow context provider values that are created anew on every render


React compares a context's `value` by identity. An object, array or function that's created while the component renders is a new value every time. So every consumer of the context renders again each time this component does, even if nothing in the value changed.

The rule looks at the `value` of `<Something.Provider>`, and of `<Something>` where `Something` is the result of `createContext()`. It reports objects, arrays, functions, classes, `new` expressions, regular expressions and JSX, whether they're written in the prop or kept in one of the component's variables.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-no-constructed-context-values" = "error" # or "warn"
```


## Examples

Reported:

```jsx
function App({ user, children }) {
  return (
    <UserContext.Provider value={{ user, isAdmin: user.role === "admin" }}>
      {children}
    </UserContext.Provider>
  );
}
```

```jsx
const LogoutContext = createContext(null);

function App({ user, children }) {
  const logout = () => signOut(user);
  return <LogoutContext value={logout}>{children}</LogoutContext>;
}
```

Not reported:

```jsx
function App({ user, children }) {
  const value = useMemo(() => ({ user, isAdmin: user.role === "admin" }), [user]);
  return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
}
```

```jsx
const LogoutContext = createContext(null);

function App({ user, children }) {
  const logout = useCallback(() => signOut(user), [user]);
  return <LogoutContext value={logout}>{children}</LogoutContext>;
}
```

A value that's created once, outside the component, is fine too:

```jsx
const theme = { color: "blue" };

function App({ children }) {
  return <ThemeContext.Provider value={theme}>{children}</ThemeContext.Provider>;
}
```
