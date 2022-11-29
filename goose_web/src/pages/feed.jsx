import './pages.css'
import {React, useState} from 'react'
import Cards from '../components/cards'

const loginPage = () => {     
    const [show, setShow] = useState(false); 
    const pop_up = () => {
        document.getElementById("accounts").className = 'fade';
        setTimeout(() => {setShow(true)}, 500);  
    }
  return (
    <>
        {show && <Feed/> }
        {!show && <Login/>}
    </>
  )
    function Login() {
        return (
            <div id = "accounts">
                <form action = "" method = "get" >
                    <h2 style = {{fontSize: "1.6rem"}}>Sign in to secureIT</h2>
                    <div style = {{ display: "flex", flexDirection: "column"}}>
                        <input type = "text" className = "inputBox" placeholder="username" style = {{zIndex: "1"}}></input>
                        <input type = "text" className = "inputBox" placeholder = "password" ></input>
                    </div>
                    <button type = "button" onClick={() => pop_up()} style = {{ margin: "1rem"}}>Enter</button>
                </form>
            </div>
        )
    }
}

function Feed() {
    return (
        <div id = "feed">
            <h1> Here are your feeds </h1> 
            <Cards title = "Front Door" feedLink = "http://127.0.0.1:8080"/>   
        </div>
    )
}

export default loginPage
