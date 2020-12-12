import React, { Component } from 'react'
import biologo from './public/image/biopicimg.jpg'

class About extends Component {
    render() {
        return (
            <section id="container-about" className="container-about">
                    <h1>About Me</h1> 

                    <img src={biologo} width="180" height="180" alt="abtimg"/>
                    <p>This is where about the person will be.
                    </p>
                
            </section>
        )
    }
}

export default About
