import React from 'react'
import Data from '../Data'
import { Link } from 'react-router-dom'

const HollyWood = () => {
    const HollywoodData = Data.filter((item) => item.category === "Hollywood");

    return (
        <div className='category-page'>
            <h1>Hollywood Blogs</h1>
            <div className='blog-list'>
                {HollywoodData.map((item) => (
                    <div key={item.id} className='blog-card'>
                        <Link to={`/details/${item.id}`}>
                            <img src={item.img_url} alt={item.title} />
                            <h3>{item.title}</h3>
                        </Link>
                        <p>{item.description.slice(0, 100)}...</p>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default HollyWood
