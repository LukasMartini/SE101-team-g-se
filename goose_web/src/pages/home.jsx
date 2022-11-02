import './pages.css'
import React from 'react'
import { useNavigate } from 'react-router-dom';
// import { setTimeout } from "timers/promises";

function wait(ms){
    var start = new Date().getTime();
    var end = start;
    while(end < start + ms) {
      end = new Date().getTime();
   }
 }

function pop_up() {
    console.log("clicked")
    // document.getElementById("App").classList.toggle("fade")
    document.getElementById("App").className = 'fade';
    // setTimeout(() => removeTarget.remove(), 1000);
    // wait(ms)
    location.href="feed"
}

const Home = () => {
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