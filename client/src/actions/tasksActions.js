import axios from 'axios';
import { GET_ERRORS, GET_TASKS, DELETE_TASK, TASKS_LOADING } from './types';

// Get all tasks
export const getTasks = () => dispatch => {
	dispatch(setTasksLoading());
	axios
		.get(`/api/tasks`)
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

// Add task
export const addTask = (taskData, history) => dispatch => {
	axios
		.post(`/api/tasks`, taskData)
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
		.delete(`/api/tasks/${id}`)
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