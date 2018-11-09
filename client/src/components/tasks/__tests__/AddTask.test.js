import React from 'react';
import { shallow, mount } from 'enzyme';
import { MemoryRouter } from 'react-router-dom';
import moxios from 'moxios';

import Root from '../../../Root';
import AddTask from '../AddTask';

let wrapped;
beforeEach(() => {
  wrapped = mount(
    <Root>
      <MemoryRouter>
        <AddTask />
      </MemoryRouter>
    </Root>
  );
  moxios.install();
});

afterEach(() => {
  wrapped.unmount();
  moxios.uninstall();
});

it('should render propertly', () => {
  expect(wrapped.find('h1').text()).toBe('Add task');
  expect(wrapped.find('input.btn').props().value).toBe('Submit');
});

describe('form area', () => {
	it('renders errors when empty form is submitted', (done) => {
		wrapped.find('form').simulate('submit');
		wrapped.update();

		moxios.wait(() => {
	  	let request = moxios.requests.mostRecent()
	   	request.respondWith({
        status: 400,
        response: {"params":{"arg1":["required field"],"arg2":["required field"]}}
      }).then(function () {
      	wrapped.update();
        //console.log('error field: ' + JSON.stringify( wrapped.find('form').html()) )
        expect(wrapped.find('div.invalid-feedback').first().text()).toBe("required field")

        //console.log(JSON.stringify( wrapped.find('.form-control').first().hasClass('is-invalid') ))
        expect(wrapped.find('.form-control').first().hasClass('is-invalid')).toEqual(true);

        done()
      })
		});
	});

	it('renders errors when form is submitted and server is not responding', (done) => {
		wrapped.find('form').simulate('submit');
		wrapped.update();

		moxios.wait(() => {
			let request = moxios.requests.mostRecent()
			request.respondWith({
				status: 500
			}).then(() => {
				wrapped.update();
				//console.log(JSON.stringify( wrapped.find('form').html()) )
				done()
			})
		});
	});	
});