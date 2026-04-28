import React from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Data from '../Data.js'

const Details = () => {

    const navigate = useNavigate();

    const { id } = useParams()

    const post = Data.find((item) => item.id === parseInt(id));

    if (!post) {
        return <div>Post not found</div>
    }

    return (
        <>
            <button onClick={() => navigate(-1)}>Back</button>
            <div className='details-container'>
                <h1>{post.title}</h1>
                <img src={post.img_url} alt={post.title} style={{ width: '100%', maxWidth: '600px' }} />
                {post.rating && <p>Rating: {post.rating}</p>}
                <p>{post.description}</p>
            </div>
        </>
    )
}

export default Details
