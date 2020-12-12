import React from 'react';

class TextIndieFaction extends React.Component {
    render() {
        return (
            <div style={{ textAlign: "center", color: "#BBBBBB", fontFamily: "fs gravity", fontSize: "2em", padding: "0 5px 10px 0", position: "absolute", top: "0", margin: "10% 0px 25% 0px" }}> Indie
            Faction
            </div >
        );
    }
}

class ConsoleBox extends React.Component {
    render() {
        const BoxStyle = {
            position: "fixed",
            top: "15%",
            left: "5%",
            height: "100px",
            width: "20px",
            color: "#2E2E2E",
        }
        return (
            <div style={BoxStyle}></div>
        );
    }
}

class CircleButton extends React.Component {
    render() {
        const OuterCircle = {
            height: "86px",
            width: "86px",
            borderRadius: "43px",
            backgroundColor: "#747474",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            margin: "15px 0px",
        };
        const InnerCircle = {
            height: "60px",
            width: "60px",
            borderRadius: "30px",
            backgroundColor: "#434242",
            boxShadow: "4px 4px 15px black",
        };

        return (
            <div style={OuterCircle}>
                <div style={InnerCircle}></div>
            </div>
        );
    }
}

class SelectPlayButton extends React.Component {
    render() {
        const PlayButton = {
            borderLeft: "25px solid #C4C4C4",
            borderRight: "25px solid transparent",
            borderBottom: "25px solid transparent",
            borderTop: "25px solid transparent",
            transform: "scaleY(0.45)",
        }
        const SelectButton = {
            height: "15px",
            width: "25px",
            margin: "20px",
            backgroundColor: "#C4C4C4",
            boxShadow: "4px 4px 15px black",
        }
        return (
            <div style={{ width: "100%", margin: "15px 0px", display: "flex", justifyContent: "space-between", alignItems: "center", }}>
                <div style={SelectButton}></div>
                <div style={PlayButton}>
                </div>
            </div>
        );
    }
}

class PlusPad extends React.Component {
    render() {
        const PlusButtonBar = {
            position: "relative",
            height: "100px",
            width: "30px",
            backgroundColor: "#C4C4C4",
            boxShadow: "4px 4px 15px black",
            transform: "rotate(-90deg)",
        }
        const PlusButtonBarRotated = {
            position: "relative",
            height: "100px",
            width: "30px",
            backgroundColor: "#C4C4C4",
            boxShadow: "4px 4px 15px black",
            transform: "rotate(90deg)",
        }
        return (
            <div style={{ width: "100%", margin: "35px 0 0 0", display: "flex", justifyContent: "center", alignItems: "center", }}>
                <div>
                    <div style={PlusButtonBarRotated}>
                        <div style={PlusButtonBar}></div>
                    </div>
                </div>
            </div>
        );
    }
}

class ConsoleController extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        const BoxStyle = {
            position: "absolute",
            top: 50 - this.props.height / 2 + "%",
            left: "50px",
            height: this.props.height + "%",
            width: this.props.width + "px",
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
            backgroundColor: "#2E2E2E",
            boxShadow: "inset 4px 4px 20px black",
        };
        return (
            <div>
                <ConsoleBox />
                <div style={BoxStyle}>
                    <TextIndieFaction />
                    <CircleButton />
                    <SelectPlayButton />
                    <PlusPad />
                </div>
            </div>
        );
    }
}

export default ConsoleController;