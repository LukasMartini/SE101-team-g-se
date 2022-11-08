import React from 'react';
import { useState } from 'react'
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; 
import Home from './pages/home'; 
import Feed from './pages/feed'; 
import './App.css'

function App() {
  return (
    <Router>
      <Routes>
        <Route path = '/' element={<Home/>}/>
        <Route path = '/Feed' element={<Feed/>}/>
      </Routes>
    </Router>
  )
}


export default App;