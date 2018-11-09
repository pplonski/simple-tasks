import reducer from '../tasksReducer';
import * as types from '../../actions/types';

describe('tasks reducer', () => {
	it('should return the initial state', () => {
		expect(reducer(undefined, {})).toEqual({
			tasks: null,
			loading: false,
			completedTask: ''
		})
	})

	it('should handle GET_TASKS', () => {
		expect(
			reducer(undefined, {
				type: types.GET_TASKS,
				payload: [{ id: '1', task_id: '123', args: {"arg1": 100, "arg2": 1} }]
			})
		).toEqual(
			{
				tasks: [{ id: '1', task_id: '123', args: {"arg1": 100, "arg2": 1} }],
				loading: false,
				completedTask: ''
			}
		)
	})
})