import React from 'react'
import { Link } from 'react-router-dom'
import { useContext } from 'react';
import { ThemeContext } from '../context/ThemeContext';

const Navbar = () => {
    const { theme, toggleTheme } = useContext(ThemeContext);
    return (
        <nav>
            <ul>
                <button onClick={toggleTheme}>
                    Switch to {theme === "light" ? "Dark 🌙" : "Light ☀️"}
                </button>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/bollywood">BollyWood</Link></li>
                <li><Link to="/hollywood">Hollywood</Link></li>
                <li><Link to="/technology">Technology</Link></li>
                <li><Link to="/fitness">Fitness</Link></li>
                <li><Link to="/food">Food</Link></li>
            </ul>

        </nav>
    )
}

export default Navbar