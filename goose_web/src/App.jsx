import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'

function App() {
  return (
    <div style={{height:'80vh', width:'80vw', paddingTop:'30vh'}} className="App" onClick={() => alert("hi")}>
      <div>
        <h1>Welcome to SecureIT.</h1>
        <h2>Click anywhere to begin.</h2>
      </div>
    </div>
  )
}

export default App
