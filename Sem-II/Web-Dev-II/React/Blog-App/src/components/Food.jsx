import React from 'react'
import Data from '../Data'
import { Link } from 'react-router-dom'

const Food = () => {
    const FoodData = Data.filter((item) => item.category === "Food");

    return (
        <div className='category-page'>
            <h1>Food Blogs</h1>
            <div className='blog-list'>
                {FoodData.map((item) => (
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

export default Food
