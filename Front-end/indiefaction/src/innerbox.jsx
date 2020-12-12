import React, { Component, Fragment } from 'react';
import './css/innerbox.css'


class InnerBox extends Component {

    render() { 
        return (
                <React.Fragment>
                    <div className='content'></div>
                    <p id='text'>{this.props.name}</p>
                </React.Fragment>
        );
    }
}
 
export default InnerBox;