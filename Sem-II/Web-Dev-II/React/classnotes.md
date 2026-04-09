
[Notes](https://sp-krmu-source.github.io/React-Notes/#class-components)

2 virtual dom /

virtual dom 1 and virtual dom 2 when gets compared to each other according to users change 
is knows as DIFFING ALGORITHM

virtual dom 1 is copy of Real DOm , Virtual dom 2 will manage the changes

when virtual dom 1 changes into Real DOM 1 then it is called as RECONCILIATION.

<> = called React fragement for multiple line of code.

Props-Drilling : 
  - Sending props from child to grandchild in heirarchal order , such data may or may not be needed by the sub heirarchy and will become inefficient .
  - To cater to this we use 'Context-API'

Flag Variable
  Containing Value 

What is State ?
  -

Mount - UPdate -Unmount = CRUD
  - Lifecycle methods

### React Hooks
Hooks are functions that let you “hook into” React state and lifecycle features from function components. They were introduced in React 16.8.

**1. useState Hook**
- Used to add state to a functional component.
- Returns an array with two elements: the **current state value** and a **function to update it**.
- Usage: `const [count, setCount] = useState(0);`
- When the state updater function is called, React re-renders the component to reflect the change.

**2. useEffect Hook**
- Handles side effects like data fetching, manual DOM manipulation, or timers.
- It runs after every render by default, but can be restricted using a dependency array `[]`.

**Key Concepts:**
- **Props**: Short for properties; they are read-only data passed from a parent component to a child component.
- **State**: A built-in React object that is used to contain data or information about the component. State is private and fully controlled by the component.
- **One-Way Data Flow**: Data in React flows in one direction—from parent to child through props.
- **Rules of Hooks**: 
  - Call Hooks only at the **Top Level**.
  - Call Hooks only from **React Function Components** or **Custom Hooks**.



