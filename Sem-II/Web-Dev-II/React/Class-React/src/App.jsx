import React from "react";
import Navbar from "./components/Navbar";
import About, { add, subtract } from "./About";
import "./App.css";
import Parent from "./PropsPassing/Parent";
import TernaryComp from "./ConceptComp/TernaryComp";
import UseStateOne from "./Hooks/UseStateOne";
import MultiCounter from "./Hooks/MultiCounter";
import Password from "./Hooks/ShowPassword";
import DarkLightTheme from "./Hooks/DarkLightTheme";
import Form from "./Hooks/FormHandling";

const App = () => {
  console.log(add(2, 3))
  console.log(subtract(2, 3))
  return (
    
    <>
      <Navbar />
      <DarkLightTheme/>
      <h1>Hello World</h1>

      <About />
      <p>Addition of {add(10, 20)}</p>
      <p>Subtraction of {subtract(10, 20)}</p>
      <p><Parent /></p>
      <TernaryComp />
      <UseStateOne />
      <hr /> 
      

      
      <MultiCounter />
      <Password/>
      <Form/>
    
    </>
    );
};

export default App;
