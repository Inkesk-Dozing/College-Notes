import React from 'react'

const Features = () => {
    const features = [
        { title: "Smooth Transitions", desc: "Buttery smooth animations for a premium feel." },
        { title: "Responsive Design", desc: "Looks great on any device, from mobile to desktop." },
        { title: "Glassmorphism", desc: "Modern frosted glass effects for depth." },
        { title: "Hover Effects", desc: "Interactive elements that respond to your touch." }
    ]

    return (
        <section className='features-section'>
            <h2 className='section-title'>Core Features</h2>
            <div className='features-grid'>
                {features.map((f, i) => (
                    <div key={i} className='feature-card'>
                        <h3>{f.title}</h3>
                        <p>{f.desc}</p>
                    </div>
                ))}
            </div>
        </section>
    )
}

export default Features