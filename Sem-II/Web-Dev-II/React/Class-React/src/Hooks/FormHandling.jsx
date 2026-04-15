// import { useState } from "react";

// function Form() {
//   const [name, setName] = useState("");

//   return (
//     <div>
//       <input
//         type="text"
//         placeholder="Enter name"
//         onChange={(e) => setName(e.target.value)}
//       />
//       <h2>Hello, {name}</h2>
//     </div>
//   );
// }

// export default Form;


import { useState } from "react";

function Form() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
  });

  function handleChange(e) {
    const { name, value } = e.target;

    setFormData({
    ...formData,   // Spread operator to copy existing formData - Destructuring to 
    // get name and value from event target
      [name]: value,
    });
  }

  return (
    <>
      <input
        type="text"
        name="name"
        placeholder="Enter name"
        value={formData.name}
        onChange={handleChange}
      />

      <input
        type="email"
        name="email"
        placeholder="Enter email"
        value={formData.email}
        onChange={handleChange}
      />

      <input
        type="password"
        name="password"
        placeholder="Enter password"
        value={formData.password}
        onChange={handleChange}
      />

      <h3>{JSON.stringify(formData)}</h3>
    </>
  );
}

export default Form;