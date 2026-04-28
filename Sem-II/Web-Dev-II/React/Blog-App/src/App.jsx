import React from 'react'
import './App.css'
import Home from './components/home'
import About from './components/about'
import Contact from './components/contact'
import Navbar from './components/navbar'
import BollyWood from './components/BollyWood'
import HollyWood from './components/HollyWood'
import Technology from './components/Technology'
import Fitness from './components/Fitness'
import Food from './components/Food'
import { BrowserRouter, Routes, Route } from 'react-router-dom'


import Data from './Data.js'
import Details from './components/Details'

const App = () => {
    return (
        <BrowserRouter>
            <Navbar />

            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/contact" element={<Contact />} />
                <Route path="/bollywood" element={<BollyWood />} />
                <Route path="/hollywood" element={<HollyWood />} />
                <Route path="/technology" element={<Technology />} />
                <Route path="/fitness" element={<Fitness />} />
                <Route path="/food" element={<Food />} />
                <Route path="/details/:id" element={<Details />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App