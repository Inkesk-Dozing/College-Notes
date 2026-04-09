
*JavaScript Interview Preparation Questions/Question Bank:*

Q1. What is the difference between var, let, and const?

Q2. Explain the different types of operators in JavaScript.
Examples:
* Arithmetic Operators
* Assignment Operators
* Comparison Operators
* Logical Operators
* Bitwise Operators
* Ternary Operator
* Type Operators

Q3. What is the difference between == and ===?

Q4. What is Hoisting and TDZ (Temporal Dead Zone)?

Q5. Explain different Array methods in JavaScript.
Important comparisons:
* map() vs filter() vs reduce()
* map() vs forEach()
* find() vs filter()
* some() vs every()

Q6. Explain String methods and Object methods in JavaScript.

Q7. Types of Functions in JavaScript
* Regular Function
* Arrow Function
* First-Class Function
* Higher-Order Function
* Callback Function
* Self-Invoking Function (IIFE – Immediately Invoked Function Expression)
* Anonymous Function

2nd Sem Onwards:

Q8. What is the difference between setTimeout() and setInterval()?

Q9. What is the difference between DOM and HTML?What are the uses of the DOM?

Q10. What is the difference between:
* textContent
* innerHTML
* innerText


Q11. What is the difference between:
* getElementById()
* getElementsByClassName()
* query selector and queryselectorall

Q12. Create element, append element, remove element using DOM.

Q13. Explain Event Handling in JavaScript
* addEventListener() with implementation          

Q14. Form Validation using Dom:
    * onclick
    * onchange
    * onsubmit
Q15. Explain Execution Context and Call Stack.How does JavaScript code execute?

Q16. What is Callback Hell? Explain its disadvantages.

Q17. Explain the Lifecycle of a Promise.
Answer flow:
1. Start with Callback Hell problem
2. Define Promise
3. Explain Promise states
    * Pending
    * Fulfilled
    * Rejected
4. Promise consumers:
    * .then()
    * .catch()
    * .finally()
5. Implementation example

Q18. Explain the Event Loop and how asynchronous code executes in the execution context.

Q19. What is Promise Chaining and its disadvantages?

Q20. Explain Async and Await.Why is it more efficient and readable than Promise chaining?



<!-- Guess the Output and Explain the Reason in Details (Concepts to cover:callstack, event loop, micro task and macro task queue) 

Q21. 
console.log("A");

setTimeout(() => {
  console.log("B");
}, 1000);

Promise.resolve().then(() => {
  console.log("C");
});

console.log("D");

Q22.
console.log("1");

Promise.resolve().then(() => {
  console.log("2");
});

Promise.resolve().then(() => {
  console.log("3");
});

console.log("4");

Q23.
setTimeout(() => {
  console.log("Timeout 1");

  Promise.resolve().then(() => {
    console.log("Promise inside Timeout");
  });

}, 0);

Promise.resolve().then(() => {
  console.log("Promise 1");
});

Q24.
console.log("1");

setTimeout(() => console.log("2"), 0);

Promise.resolve().then(() => {
  console.log("3");
  Promise.resolve().then(() => {
    console.log("4");
  });
});

console.log("5");

Q25.
console.log("A");

new Promise((resolve) => {
  console.log("B");
  resolve();
  console.log("C");
}).then(() => {
  console.log("D");
});

console.log("E"); -->



26. What is REACT and explain features of react.


27. What is virtual DOM 

28. What is single page application.The difference between SPA and MPA (multi page application).

29. Explain one way data binding (inn REACT).

30. How JSX works in REACT, what is the need of babel and what is it.

31. Explain Lifecycle methods and its disadvantages.

32. How to tackle lifecycle methods by using 'useEffect' hook.

33. 


<!-- # Questions

## Sem II

1.Difference between var,let and const.  
2.Explain different types of JS operators.  
3.Difference between == and ===.  
4.What is hoisting and TDZ.  
5.Explain different Array functions in JS.  
    map v/s reduce v/s filter  
    find v/s filter  
    map v/s foreach  
    sum v/s every  
6.Difference between string , obj method  
7.Types of Functions.  
&emsp;7.1&nbsp; Regular Function  
&emsp;7.2&nbsp; Arrow Function  
&emsp;7.3&nbsp; Fast class function  
&emsp;7.4&nbsp; Higher Order Function  
&emsp;7.5&nbsp; Callback Function  
&emsp;7.6&nbsp; Anonymous Function  
&emsp;7.7&nbsp; Self Invoking Function (IIFE - Immediately Invoked Functions Expression)  
8.Difference between spread operator and rest parameter  
9.What is nullish coalescing operator  
10.Difference between setInterval and setTimeout.  
11.What is DOM?
12.Difference Between 'getElementById' and 'getElementsByClassName'.  
13.Differnce Between 'query' and 'query all'
14.

```md

1. What is callback hell?solutions for it (promise chaining)
2. What is await waitign for -> fir promises to get resolved or rejected
3. Whenever you call async func what you get in return. ->promises will be returned that are nothing but data -> 
   data will be returned in form of promises.
4. 

``` -->
