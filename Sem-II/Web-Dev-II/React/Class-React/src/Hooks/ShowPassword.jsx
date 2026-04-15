import { useState } from 'react';

function Password() {
    const [ShowPassword, setShowPassword] = useState(false);

    return (
        <div>
            <input type={ShowPassword ? "text" : "password"} />
            <button onClick={() => setShowPassword(!ShowPassword)}>
                {ShowPassword ? "Hide" : "Show"}
            </button>
        </div>
    );

}

export default Password;