# Context-API

1. Create a Context

```react
const userContext = createContext();
```

2. Provide the Context

```react
<userContext.Provider value={value}> {children} </userContext.Provider>
```

3. Consume the Context

```react
const value = useContext(userContext);
```

4. createContext() vs useCreateContext

```react
createContext(): It is used to create the context.
useCreateContext(): It is used to consume the context.
```

value = {value}  this value is assigned in App.jsx
value = {{movies}}