import React, { Component } from 'react';
import InnerBox from './innerbox'
import './css/flexbox.css';
import axios from 'axios';

class FlexBox extends Component {
    constructor(props){
        super(props)
        this.state = {
            ceditions : [],
        }
    }

    componentDidMount(){
        axios.get('http://localhost:8000/cedition/api/collector_edition/random?n=6')
        .then(response => {
            this.setState({ceditions: response.data})
        })
        .catch(error =>{
            console.log(error);
        }
        )
    }


    render() {
        const collec_name =  this.state.ceditions;
        let val;
        val = collec_name.map((cedition)=> <div className='box flexbox-item'> <InnerBox name={cedition.name}/></div>);
        return (
            <div>
                <div className='container-1'>
                    { val }
                </div>
            </div>

          );
    }
}
 
export default FlexBox;