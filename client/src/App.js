import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
//import { Provider } from 'react-redux';
import axios from 'axios';

import Root from './Root';
import WebSocketContainer from "./components/containers/WebSocketContainer";
import NavbarMain from './components/layout/NavbarMain.js';
import FooterMain from './components/layout/FooterMain.js';

import Home from './components/Home';
import Tasks from './components/tasks/Tasks';
import AddTask from './components/tasks/AddTask';

//import store from './store';

import './App.css';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

let webSocketUrl;
(process.env.REACT_APP_WEBSOCKET_URL!==undefined) ? webSocketUrl=process.env.REACT_APP_WEBSOCKET_URL : webSocketUrl="ws://"+window.location.hostname+":"+window.location.port+"/websockets/tasks/"

//console.log("url->", webSocketUrl, window.location.hostname, window.location.port);

class App extends Component {
  render() {
    return (
    	<Root>
    		<Router>
    			<div className="App">
	    			<NavbarMain />
	    			<Route exact path="/" component={ Home } />
            <Switch>
              <WebSocketContainer host={ webSocketUrl } autoconnect={true}>
  	    			  <Route exact path="/tasks" component={ Tasks } />
              </WebSocketContainer>
            </Switch>
	    			<Route exact path="/tasks/add" component={ AddTask } />
            <FooterMain />
    			</div>
	      </Router>
      </Root>
    );
  }
}

export default App;
