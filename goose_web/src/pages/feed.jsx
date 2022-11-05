import './pages.css'
import {React, useState} from 'react'
import Cards from '../components/cards'
import { useNavigate } from 'react-router-dom';

const Feed = () => {
    return (
        <>
            <div style={{position: 'fixed', top: '50%', left: '50%', transform: 'translate(-50%, -50%)'}} >
                <h1> Here are your feeds </h1> 
                <Cards title = "Front Door"/> 
            </div>
        </>
    )
}
  
  export default Feed