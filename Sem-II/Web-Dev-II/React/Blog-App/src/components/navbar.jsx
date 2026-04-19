import React from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/bollywood">BollyWood</Link></li>
                <li><Link to="/hollywood">HollyWood</Link></li>
                <li><Link to="/technology">Technology</Link></li>
                <li><Link to="/fitness">Fitness</Link></li>
                <li><Link to="/food">Food</Link></li>
            </ul>
        </nav>
    )
}

export default Navbar