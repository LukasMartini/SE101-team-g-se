import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'

function pop_up() {
  console.log("clicked")
  // document.getElementById("App").classList.toggle("fade")
  document.getElementById("App").className = 'fade';
  sleep(300)
  document.getElementById("App").remove()
}

function App() {
  return (
    <div id="App" style={{height:'80vh', width:'80vw', paddingTop:'30vh'}} className="App" onClick={() => pop_up()}>
      <div id='startDiv'>
        <h1 id='startHeader1'>Welcome to SecureIT.</h1>
        <h2 id='startHeader2'>Click anywhere to begin.</h2>
      </div>
    </div>
  )
}

export default App
