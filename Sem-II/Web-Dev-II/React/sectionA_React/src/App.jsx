import React from "react";
import Navbar from "./components/Navbar";
import About, { add, subtract } from "./About";
import "./App.css";

const App = () => {
  console.log(add(2, 3))
  console.log(subtract(2, 3))
  return (
    <>
      <Navbar />
      <h1>Hello World</h1>
      <About />
      <p>Addition of {add(10, 20)}</p>
      <p>Subtraction of {subtract(10, 20)}</p>
    </>
  );
};

export default App;
