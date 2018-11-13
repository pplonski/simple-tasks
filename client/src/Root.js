import React from 'react';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension/developmentOnly';

import setAuthToken from './utils/setAuthToken';
import { setCurrentUser } from './actions/authActions';

import rootReducer from './reducers';
import webSocketsMiddleware from './middlewares/webSocketsMiddleware';

export default({ children, initialState={} }) => {
	const middleware = [thunk, webSocketsMiddleware];

	const store = createStore(
		rootReducer,
		initialState,
		composeWithDevTools(
			applyMiddleware(...middleware),
		)
	);

	// Check for token
	if(localStorage.authTokenKey) {
	  // Set auth token header auth
	  setAuthToken(localStorage.authTokenKey);
	  // Set user and isAuthenticated
	  store.dispatch(setCurrentUser(localStorage.authTokenKey));
	}
	
	return(
		<Provider store={store}>
			{children}
		</Provider>
	);
};


