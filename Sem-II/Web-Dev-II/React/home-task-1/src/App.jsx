import { useState } from 'react'
import Features from './components/Features'
import Navbar from './components/Navbar'
import HeroSection from './components/HeroSection'
import Footer from './components/Footer'
import Testimonials from './components/Testimonials'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="animate-fade">
      <Navbar />
      <main>
        <HeroSection />
        {/* 'container' is a helper class to center our content and add padding */}
        <div className="container">
          <Features />
          <Testimonials />
        </div>
      </main>
      <Footer />
    </div>
  )
}

export default App
