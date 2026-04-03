import React from 'react'

const Navbar = () => {
    return (
        <nav className="navbar glass">
            <div className="container nav-container">
                <div className="logo">Home-Task-1</div>
                <ul className="nav-links">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#features">Features</a></li>
                    <li><a href="#testimonials">Testimonials</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>
        </nav>
    )
}

export default Navbar