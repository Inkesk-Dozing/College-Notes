import React from 'react'

const Child = ({ name, hello }) => {
    return (
        <>
            <div>Rendered in Child Component : {name}</div>
            <button onClick={hello}>Click Me</button>
        </>
    )
}

export default Child