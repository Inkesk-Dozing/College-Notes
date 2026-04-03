import React from 'react'

const Footer = () => {
    return (
        <footer className='footer'>
            {/* We use 'container' here too to keep at-most 1200px width */}
            <div className="container footer-content">
                {/* &copy; is a special HTML entity that renders the © symbol */}
                <p>&copy; 2026. All rights reserved.</p>
                <p>Made by Harsh Dev Jha</p>
            </div>
        </footer>
    )
}

export default Footer