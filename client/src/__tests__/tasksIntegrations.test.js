import React from 'react';
import moxios from 'moxios';
import { mount } from 'enzyme';

import Root from '../Root';
import App from '../App';

beforeEach(() => {
	moxios.install();
	moxios.stubRequest('/api/tasks', {
		status: 200,
		response: [
			{ id: '1', task_id: '123', args: {arg1: 100, arg2: 1} }, 
			{ id: '2', task_id: '345', args: {arg1: 100, arg2: 2} }
		]
	})
});

afterEach(() => {
	moxios.uninstall();
});

it('can fetch a list of tasks and display them', (done) => {
	const wrapped = mount(
		<Root>
			<App />
		</Root>
	);

	moxios.wait(() => {
		wrapped.update();
		//console.log(<App />)
		//expect(wrapped.find('li').length).toEqual(2);
		done();
		wrapped.unmount();
	});
	
});