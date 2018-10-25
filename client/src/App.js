import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import axios from 'axios';

import WebSocketContainer from "./components/containers/WebSocketContainer";
import NavbarMain from './components/layout/NavbarMain.js';
import FooterMain from './components/layout/FooterMain.js';

import Home from './components/Home';
import Tasks from './components/tasks/Tasks';
import AddTask from './components/tasks/AddTask';

import store from './store';

import './App.css';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class App extends Component {
  render() {
    return (
    	<Provider store={ store }>
        <WebSocketContainer host="ws://127.0.0.1:8000/tasks/" autoconnect={true}>
      		<Router>
      			<div className="App">
  	    			<NavbarMain />
  	    			<Route exact path="/" component={ Home } />
  	    			<Route exact path="/tasks" component={ Tasks } />
  	    			<Route exact path="/tasks/add" component={ AddTask } />
              <FooterMain />
      			</div>
  	      </Router>
          </WebSocketContainer>
      </Provider>
    );
  }
}

export default App;
