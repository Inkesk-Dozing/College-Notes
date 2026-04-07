import React, {useState} from 'react'


const UseStateOne = () => {

    const [count , setCount] = useState(0)
    console.log("Count",count)//0

    function increase (){
        setCount(count + 1) //1  
        // count= count+1 //1
        console.log("Count",count) //0

    }

    function decrease (){
        setCount(count - 1) //1  
        // count= count-1 //-1
        console.log("Count",count) //0

    }

    function div2 (){
        setCount(count/2) //1  
        console.log("Count",count) //0

    }
    
  return (

    <>
        <div>UseStateOne</div>
        <h1>{count}</h1>
        <button onClick={increase}>Increase</button>
        <button onClick={decrease}>Decrease</button>
        <button onClick={div2}>div2</button>
        <button onClick={() => setCount(0)}>Reset</button>
    </>
  )
}

export default UseStateOne