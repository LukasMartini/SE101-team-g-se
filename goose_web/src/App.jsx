import React from 'react';
import { useState } from 'react'
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; 
import Home from './pages/home'; 
import './App.css'

function App() {
  return (
<<<<<<< Updated upstream
    <div style={{height:'80vh', width:'80vw', paddingTop:'30vh'}} className="App" onClick={() => alert("hi")}>
      <div>
        <h1>Welcome to SecureIT.</h1>
        <h2>Click anywhere to begin.</h2>
      </div>
    </div>
  )
=======
       <Router>
        <Routes>
          <Route path = '/' element={<Home/>}/>
        </Routes>
      </Router>
  );
>>>>>>> Stashed changes
}


export default App;