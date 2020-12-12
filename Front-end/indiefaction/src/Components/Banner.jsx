import React, { Component } from 'react'
import logo from '../Components/public/image/maxresdefault.jpg';



class Banner extends Component {
    render() {
        return (
            <section className="container-banner">

                    <a href="#home"><img id="profilepic" src={logo}  width="170" height="170" alt="profilepic"/></a>
                    <h1> Hi! I am Samandeep </h1>
                    <p id="paragarph1"> Creator <br/>
                    <p>Date of Joining: 10 December 2020</p>
                    </p>
                    
                    
            </section>
        )
    }
}

export default Banner


