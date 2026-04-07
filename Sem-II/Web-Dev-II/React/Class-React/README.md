# Note 

1. First Letter of the Component must be capital.
2. Diffing Algo anf Reconciliation
3. Only one component (or function) is allowed to default export in a file.
4. Wrap named export components in - {} - 

```js
const Demo = () => {
    return "Hello World"
}
export {Demo}
```

```jsx
// Default Export
export default function App() {
    return <h1>App</h1>;
}

// Named Export
export function About() {
    return <h1>About</h1>;
}
```

5. Lifecycle in other components:
- Class component uses life cycle methods to perform.
- Life cycle methods have unnecessary boilerplate code so the application gets complex and hard to manage.
- Lifecycle Methods:
    - Mount 
    - Update
    - Unmount
- So thats why we shifted to functional components.

6. We cannot re-render normal variable in JSX.

7. Inside onclick or any event just write the function name, no need of ().

# HOOKS

- Hooks are function's, predefined function's 
- Hooks allows to use state and other features without writing a class.
> There are 2 rules ro use Hooks:-  
>1. Only call hooks at the top level.  
>2. Only call hooks from React function components or custom hooks.




<!-- # React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project. -->
