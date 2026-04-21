import React from 'react'
import { NavLink } from 'react-router-dom'

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li><NavLink to="/">Home</NavLink></li>
                <li><NavLink to="/bollywood">BollyWood</NavLink></li>
                <li><NavLink to="/hollywood">HollyWood</NavLink></li>
                <li><NavLink to="/technology">Technology</NavLink></li>
                <li><NavLink to="/fitness">Fitness</NavLink></li>
                <li><NavLink to="/food">Food</NavLink></li>
            </ul>
        </nav>
    )
}

export default Navbar