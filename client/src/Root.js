import React from 'react';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension/developmentOnly';

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
	
	return(
		<Provider store={store}>
			{children}
		</Provider>
	);
};


