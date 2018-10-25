import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension/developmentOnly';

import rootReducer from './reducers';
import webSocketsMiddleware from './middlewares/webSocketsMiddleware';

const initialState = {};

const middleware = [thunk, webSocketsMiddleware];

const store = createStore(
	rootReducer,
	initialState,
	composeWithDevTools(
		applyMiddleware(...middleware),
	)
);

export default store;
