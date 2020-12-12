import React from 'react';
import craft from './assets/Craft.png';
import profile from './assets/Profile.png';
import explore from './assets/Explore.png';

class WelcomeBox extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        const boxStyle = {
            position: "fixed",
            right: 0,
            top: "15%",
            fontSize: "20px",
            padding: "20px",
            color: "#BBBBBB",
            backgroundColor: "#2F3638",
            textAlign: "centre",
            fontFamily: "BankGothic Md BT",
        };
        const shadowOverlay = {
            width: "100%",
            height: "100%",
            position: "absolute",
            top: 0,
            left: 0,
            boxShadow: "inset 5px 5px 10px #0F0F0F",
        };
        return (
            <div style={boxStyle}>Welcome {this.props.guest ? "Guest" : "User"}<div style={shadowOverlay}></div></div>
        );
    }
}

class AboutUs extends React.Component {
    render() {
        const BoxStyle = {
            position: "fixed",
            bottom: 0,
            right: 0,
            borderRadius: "150px 0 0 0",
            height: "100px",
            width: "100px",
            padding: "20px",
            color: "#BBBBBB",
            backgroundColor: "#2F3638",
            fontFamily: "BankGothic Md BT",
        }
        const shadowOverlay = {
            width: "100%",
            height: "100%",
            position: "absolute",
            top: 0,
            left: 0,
            borderRadius: "150px 0 0 0",
            boxShadow: "inset 5px 5px 20px #0F0F0F",
        };
        return (
            <div style={BoxStyle}><div style={shadowOverlay}></div><div style={{ position: "absolute", bottom: "40px", right: "10px" }}>About US</div></div>
        );
    }
}

class Icon extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div style={{ textAlign: "center", color: "#BBBBBB", fontFamily: "BankGothic Md BT" }}>
                <img style={{ width: "40%", padding: "20px" }} src={this.props.logo} />
                {this.props.IconText}
            </div >
        );
    }
}

class TextIndieFaction extends React.Component {
    render() {
        return (
            <div style={{ textAlign: "center", color: "#BBBBBB", fontFamily: "fs gravity", fontSize: "2em", padding: "0 5px 10px 0", }}> Indie
            Faction
            </div >
        );
    }
}

class DashboardColumn extends React.Component {
    render() {
        const BoxStyle = {
            position: "fixed",
            top: 0,
            left: 0,
            height: "100%",
            width: "110px",
            backgroundColor: "#2F3638",
        }
        const shadowOverlay = {
            width: "100%",
            height: "100%",
            position: "absolute",
            top: 0,
            left: 0,
            boxShadow: "inset -5px 0px 20px #0F0F0F",
            display: "flex",
            justifyContent: "center",
            flexDirection: "column"
        };
        return (
            <div style={BoxStyle}>
                <div style={shadowOverlay}>
                    <TextIndieFaction />
                    <Icon logo={craft} IconText={"Craft"} />
                    <Icon logo={profile} IconText={"Profile"} />
                    <Icon logo={explore} IconText={"Explore"} />
                </div>
            </div>
        );
    }
}

class GuestColumn extends React.Component {
    render() {
        const BoxStyle = {
            position: "fixed",
            top: 0,
            left: 0,
            height: "100%",
            width: "110px",
            backgroundColor: "#2F3638",
        }
        const shadowOverlay = {
            width: "100%",
            height: "100%",
            position: "absolute",
            top: 0,
            left: 0,
            boxShadow: "inset -5px 0px 20px #0F0F0F",
            display: "flex",
            justifyContent: "center",
            flexDirection: "column",
        };
        return (
            <div style={BoxStyle}>
                <div style={shadowOverlay}>
                    <TextIndieFaction />
                    <div style={{ textAlign: "center", color: "#BBBBBB", fontFamily: "Montserrat", fontSize: "0.8em", padding: "0 5px 10px 0", }}>Guest Mode</div>
                </div>
            </div>
        );
    }
}

export { WelcomeBox, AboutUs, DashboardColumn, GuestColumn }