import { TASKS_LOADING, GET_TASKS, GET_COMPLETED_TASK, DELETE_TASK } from '../actions/types';
import { WEBSOCKET_MESSAGE } from '../actions/types';

const initialState = {
	tasks: null,
	loading: false,
	completedTask: ''
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
		case GET_COMPLETED_TASK:
			function updateCompletedTaskInArray(array, action) {
				//console.log(array);
				console.log(action);
				if(array) {
					return array.map( (item, index) => {
						if (item.id !== action.payload.id) {
				      // This isn't the item we care about - keep it as-is
				      return item
				    }
				    // Otherwise, this is the one we want - return an updated value
				    return {
				      ...item,
				      ...action.payload
				    }
					});
				}
			}
			//updateCompletedTaskInArray()
			return {
				...state,
				tasks: updateCompletedTaskInArray(state.tasks, action)
			}
		case DELETE_TASK:
			console.log(state.tasks.filter(task => task.id !== action.payload))
			console.log(action.payload)
			return {
				...state,
				tasks: state.tasks.filter(task => task.id !== action.payload)
			}
		case WEBSOCKET_MESSAGE:
			//console.log(action.payload)

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
			        	//console.log('SUCCESS');
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

			function getCompletedTaskId(action) {
				if(action.payload.data.state==='SUCCESS') {
        	return action.payload.data.db_id
        }
        return '';
			}

			return {
				...state,
				tasks: updateObjectInArray(state.tasks, action),
				completedTask: getCompletedTaskId(action)
			}
		default:
			return state;
	}
}