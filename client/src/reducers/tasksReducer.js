import { TASKS_LOADING, GET_TASKS, DELETE_TASK } from '../actions/types';
import { WEBSOCKET_MESSAGE } from '../actions/types';

const initialState = {
	tasks: null,
	loading: false
}

export default function(state = initialState, action) {
	switch(action.type) {
		case TASKS_LOADING:
			return {
				...state,
				loading: true
			}
		case GET_TASKS:
			return {
				...state,
				tasks: action.payload,
				loading: false
			}
		case DELETE_TASK:
			console.log(state.tasks.filter(task => task.id !== action.payload))
			console.log(action.payload)
			return {
				...state,
				tasks: state.tasks.filter(task => task.id !== action.payload)
			}
		case WEBSOCKET_MESSAGE:
			console.log(action.payload)

			function updateObjectInArray(array, action) {
				if(array) {
					return array.map( (item, index) => {
		        if(item.id === action.payload.data.db_id) {
			        if(action.payload.data.state==='PROGRESS') {
			        	return {
		            	...item,
		            	progress: action.payload.data.progress
		            }
			        }
			        if(action.payload.data.state==='SUCCESS') {
			        	console.log('SUCCESS');
			        	return {
		            	...item,
		            	progress: 100,
		            	state: 'SUCCESS'
		            }
							}
		        }
		 				
		        return {
		        	...item
		        	//...action.item
		        }
			    });
				}
		    
			}

			return {
				...state,
				tasks: updateObjectInArray(state.tasks, action)
			}
		default:
			return state;
	}
}