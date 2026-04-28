import React from 'react'
import Data from '../Data'
import { Link } from 'react-router-dom'

const BollyWood = () => {
    const BollywoodData = Data.filter((item) => item.category === "Bollywood");

    return (
        <div className='category-page'>
            <h1>Bollywood Blogs</h1>
            <div className='blog-list'>
                {BollywoodData.map((item) => (
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

export default BollyWood

