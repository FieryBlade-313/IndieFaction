import React from 'react';
import ReactDOM from 'react-dom';
import { WelcomeBox, AboutUs, DashboardColumn, GuestColumn } from './dashboard_components'
import ConsoleController from './controller'
import BackgroundBox from './homepage_components'
import LogInBackBox from './login_components'
import FlexBox from './flexbox'
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    {/* Uncomment the below part to see the Dashboard */}
    {/* <DashboardColumn />
    <WelcomeBox guest={false} />
    <AboutUs />
    <FlexBox /> */}

    {/* Uncomment the below part to see the Guest Explore Page */}
    {/* <GuestColumn />
    <WelcomeBox guest={true} />
    <AboutUs />
    <FlexBox /> */}

    {/* Uncomment the below part to see the Homepage */}
    {/* <BackgroundBox />
    <ConsoleController height={84} width={150} /> */}

    {/* Uncomment the below part to see the Login Page */}
    {/* <LogInBackBox />
    <ConsoleController height={84} width={150} /> */}

    {/* Uncomment the below part to see the Profile Page */}
    {/* <App /> */}
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
