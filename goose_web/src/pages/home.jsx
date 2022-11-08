
import './pages.css'
import React from 'react'
import { useNavigate } from 'react-router-dom';
//  import { setTimeout } from "timers/promises";

function wait(ms){
    var start = new Date().getTime();
    var end = start;
    while(end < start + ms) {
      end = new Date().getTime();
   }
 }



const Home = () => {
    const navigate = useNavigate(); 
    const  pop_up = () => {
        console.log("clicked")
        document.getElementById("App").className = 'fade';
        setTimeout(() => { navigate('\Feed')}, 500);
    }
    return (
        <>
            {/* <div id="particles-js"></div>   */}
            <div id="App" style={{height:'80vh', width:'80vw', paddingTop:'40vh'}} className="App" onClick={() => pop_up()}>
                <div id='startDiv'>
                    <h1 id='startHeader1'>Welcome to SecureIT.</h1>
                    <h2 id='startHeader2'>Click anywhere to begin.</h2>
                </div>
            </div>
            
        </>
    )
}
  
  export default Home