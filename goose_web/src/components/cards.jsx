import React from 'react'
import { useNavigate } from 'react-router-dom';
import './cards.css'

function cards({title, img, feedLink, onClick}) {
    // const navigate = useNavigate(); 
    return (
        <div className = "cardContainer" onClick = {onClick}>
            <h2 style = {{ fontWeight: '600' }}> {title} </h2>
            <img src = "./logo.png" style = {{objectFit: 'contain', width: '5rem', height: '5rem', filter: 'invert(100%)'}}/> 
        </div> 
    )
}

export default cards