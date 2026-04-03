import React from 'react'

const Testimonials = () => {
    // Just like Features, we store testimonial data in an array for easy updates
    const testimonials = [
        { name: "John Doe", text: "The UI is absolutely stunning. My users love the new look!" },
        { name: "Jane Smith", text: "Incredible attention to detail. The transitions are flawless." }
    ]

    return (
        <section className='testimonials-section'>
            <h2 className='section-title'>What People Say</h2>

            <div className='testimonials-grid'>
                {testimonials.map((t, i) => (
                    <div key={i} className='testimonial-card'>
                        <p className='testimonial-text'>"{t.text}"</p>
                        <p className='testimonial-name'>- {t.name}</p>
                    </div>
                ))}
            </div>
        </section>
    )
}

export default Testimonials