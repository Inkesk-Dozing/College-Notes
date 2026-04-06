import React from 'react';
import Child from './Child';

const Parent = () => {
    const fullName = "Krishyangi Dixit";

    function Alert() {
        alert("Button Clicked")
    }


    return (
        <>
            <div>Rendered in Parent Component : {fullName}</div>
            <Child name={fullName} hello={Alert} />
        </>

    )
}

export default Parent
