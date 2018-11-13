import { combineReducers } from 'redux';
import authReducer from './authReducer';
import errorsReducer from './errorsReducer';
import tasksReducer from './tasksReducer';
import webSocketsReducer from './webSocketsReducer';

export default combineReducers({
	auth: authReducer,
	errors: errorsReducer,
	tasks: tasksReducer,
	webSocket: webSocketsReducer
});