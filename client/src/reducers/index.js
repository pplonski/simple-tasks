import { combineReducers } from 'redux';
import errorsReducer from './errorsReducer';
import tasksReducer from './tasksReducer';
import webSocketsReducer from './webSocketsReducer';

export default combineReducers({
	errors: errorsReducer,
	tasks: tasksReducer,
	webSocket: webSocketsReducer
});