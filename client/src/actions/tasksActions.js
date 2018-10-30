import axios from 'axios';
import { GET_ERRORS, GET_TASKS, GET_COMPLETED_TASK, DELETE_TASK, TASKS_LOADING } from './types';

let apiUrl;
(process.env.REACT_APP_API_URL!==undefined) ? apiUrl=process.env.REACT_APP_API_URL : apiUrl=""

// Get all tasks
export const getTasks = () => dispatch => {
	dispatch(setTasksLoading());
	axios
		.get(`${apiUrl}/api/tasks`)
		.then(res => 
			dispatch({
				type: GET_TASKS,
				payload: res.data
			})
		)
		.catch(err =>
			dispatch({
				type: GET_TASKS,
				payload: null
			})
		);
}

// Get completed task
export const getCompletedTask = (id) => dispatch => {
	axios
		.get(`${apiUrl}/api/tasks/${id}`)
		.then(res => 
			dispatch({
				type: GET_COMPLETED_TASK,
				payload: res.data
			})
		)
		.catch(err =>
			dispatch({
				type: GET_COMPLETED_TASK,
				payload: null
			})
		);
}

// Add task
export const addTask = (taskData, history) => dispatch => {
	axios
		.post(`${apiUrl}/api/tasks`, taskData)
		.then(res => history.push('/tasks'))
		.catch(err =>
			dispatch({
				type: GET_ERRORS,
				payload: err.response.data
			})
		);
}

// Delete task
export const deleteTask = (id) => dispatch => {
	//dispatch(setTasksLoading());
	axios
		.delete(`${apiUrl}/api/tasks/${id}`)
		.then(res => 
			dispatch({
				type: DELETE_TASK,
				payload: id
			})
		)
		.catch(err =>
			dispatch({
				type: GET_ERRORS,
				payload: err.response.data
			})
		)

}

// Tasks loading
export const setTasksLoading = () => {
	return {
		type: TASKS_LOADING
	}
}