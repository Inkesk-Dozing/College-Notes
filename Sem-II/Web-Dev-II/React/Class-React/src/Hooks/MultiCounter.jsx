import React, { useState } from 'react'

const MultiCounter = () => {

    const [count, setCount] = useState([0, 0])
    console.log(count); //[0,0]
    // const[num,setNum] = useState(0);

    const increment = (index) => {
        setCount((prev) => {
            const newCount = [...prev];
            console.log(newCount, "line 12") //[0,0]
            newCount[index] += 1;
            return newCount
        })
    }

    console.log(count);
    return (
        <>
            <div>MultiCounter</div>
            <>
                {count.map((counter, index) => (
                    <div key={index}>
                        <h1>Count:{counter}</h1>
                        <button onClick={() => increment(index)}>Increment</button>
                    </div>
                ))}
            </>
            {/* <h1>Count:{count}</h1>
    <button onClick={()=>setCount(count+1)}>Count1</button>
    <h1>Num:{num}</h1>
    <button onClick={()=>setNum(num+1)}>Count2</button> */}
        </>
    )
}

export default MultiCounter