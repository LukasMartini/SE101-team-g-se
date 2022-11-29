
import './pages.css'
import React from 'react'
import { useNavigate } from 'react-router-dom';
//  import { setTimeout } from "timers/promises";



const Home = () => {
    const navigate = useNavigate(); 
    const  pop_up = () => {
        document.getElementById("App").className = 'fade';
        setTimeout(() => { navigate('\Feed')}, 500);
    }
    return (
        <>
            {/* <div id="particles-js"></div>   */}
            <div id="App" style={{height:'100vh', width:'100vw', paddingTop:'35vh'}} className="App" onClick={() => pop_up()}>
                <div id='startDiv'>
                    <h1 id='startHeader1'>Welcome to SecureIT.</h1>
                    <h2 id='startHeader2'>Click anywhere to begin.</h2>
                </div>
            </div>
            
        </>
    )
}
  
  export default Home