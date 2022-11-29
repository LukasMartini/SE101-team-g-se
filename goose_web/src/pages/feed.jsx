import './pages.css'
import {React, useState} from 'react'
import Cards from '../components/cards'
import { useNavigate } from 'react-router-dom';

const Feed = () => {
    return (
        <div className = "feedContainer fadeIn">
            <div>
                <h1> Here are your feeds </h1> 
                
            </div>
            <Cards title = "Front Door" feedLink = "http://se101.alakhpc.com:8080"/>   
        </div>
    )
}
  
  export default Feed