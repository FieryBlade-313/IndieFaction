import React from 'react';

class LogInBackBox extends React.Component {
    render() {
        const boxStyle = {
            position: "absolute",
            top: '0',
            left: '0',

            width: '100%',
            height: '100%',
            background: '#434242',
        };

        const innerboxStyle = {
            position: 'absolute',
            top: '8%',
            left: '4%',
            position: "fixed",
            width: '92%',
            height: '84%',
            background: '#c4c4c4',
        };


        return (
            <div style={boxStyle}><div style={innerboxStyle}></div>

                <LightGreyBox />
                <ExploreBox />
                <LoginBox />
            </div>
        );


    }
}

class LightGreyBox extends React.Component {
    render() {
        const boxStyle = {
            position: "absolute",
            top: "8%",
            right: "4%",
            height: "20%",
            width: "83%",
            backgroundColor: "#a9a9a9",
        }

        return (
            <div style={boxStyle}>

                <MessageBox />
            </div>
        );
    }
}

class ExploreBox extends React.Component {
    render() {
        const boxStyle = {
            position: "absolute",
            right: '35%',
            top: "55%",
            align: 'centre',
            fontSize: "35px",
            padding: "8px 80px",
            color: "#BBBBBB",
            backgroundColor: "#535353",
            textAlign: "centre",
            fontFamily: "BankGothic Md BT",
            boxShadow: "inset 8px 8px 30px black",
        };

        return (
            <div style={boxStyle}>Join Wth Steam</div>
        );
    }
}


class LoginBox extends React.Component {
    render() {
        const boxStyle = {
            position: "absolute",
            right: '25%',
            left: '35%',

            top: "70%",
            align: 'centre',
            fontSize: "35px",
            padding: "0px 70px",
            color: "#BBBBBB",
            backgroundColor: "#535353",
            textAlign: "centre",
            fontFamily: "BankGothic Md BT",
            boxShadow: "inset 10px 10px 60px black",

        };

        return (
            <div style={boxStyle}></div>
        );
    }
}

class MessageBox extends React.Component {
    render() {
        const boxStyle = {
            position: "absolute",
            right: '30%',
            left: '35%',

            top: "15%",
            align: 'centre',
            fontSize: "40px",
            // color: "#BBBBBB",
            textColor: "#ffffff",
            // backgroundColor: "#535353",
            textAlign: "centre",
            fontFamily: "Miltonian",
        };

        return (
            <div style={boxStyle}> Welcome  To {'\n'} Indie Faction</div>
        );
    }
}

export default LogInBackBox;