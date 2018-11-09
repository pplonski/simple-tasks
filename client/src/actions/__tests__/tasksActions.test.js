import configureMockStore from 'redux-mock-store'
import thunk from 'redux-thunk';
import moxios from 'moxios';

import * as actions from '../tasksActions';
import * as types from '../types';

const middlewares = [thunk]
const mockStore = configureMockStore(middlewares)

describe('async actions', () => {
	beforeEach(() => {
    moxios.install();
  })
  afterEach(() => {
    moxios.uninstall();
  })

  it('should create an action with correct types and payload when tasks are fetched', (done) => {
    const expectedActions = [
      { type: types.TASKS_LOADING },
      { 
      	type: types.GET_TASKS, 
      	payload: [
      		{ id: '1', task_id: '123', args: {"arg1": 100, "arg2": 1} }, 
      		{ id: '2', task_id: '345', args: {"arg1": 100, "arg2": 2} } 
      	]  
      }
    ]

    const store = mockStore({ tasks: [] })
		store.dispatch(actions.getTasks());

	  moxios.wait(() => {
	  	let request = moxios.requests.mostRecent()
	   	request.respondWith({
        status: 200,
        response: [
          { id: '1', task_id: '123', args: {"arg1": 100, "arg2": 1} }, 
          { id: '2', task_id: '345', args: {"arg1": 100, "arg2": 2} } 
        ]
      }).then(function () {
        expect(store.getActions()).toEqual(expectedActions)
        done()
      })
		});

  })
  it('should create an action with correct type and payload when completed task is fetched', () => {
		const expectedAction = [
      { 
      	type: types.GET_COMPLETED_TASK, 
      	payload: [
      		{ id: '1', task_id: '123', args: {"arg1": 100, "arg2": 1} }
      	]
      }
    ]

    const store = mockStore({ tasks: [] })
		store.dispatch(actions.getCompletedTask());

		moxios.wait(() => {
	  	let request = moxios.requests.mostRecent()
	   	request.respondWith({
        status: 200,
        response: [
          { id: '1', task_id: '123', args: {"arg1": 100, "arg2": 1} }
        ]
      }).then(function () {
        expect(store.getActions()).toEqual(expectedActions)
        done()
      })
		});

	});
})

describe('actions', () => {
  it('should create an action to set tasks loading state to true', () => {
    const expectedAction = {
      type: types.TASKS_LOADING
    }
    expect(actions.setTasksLoading()).toEqual(expectedAction)
  })
})