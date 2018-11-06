import React from 'react';
import { shallow } from 'enzyme';
import Tasks from '../Tasks';


function setup() {
  const props = {
    getTasks: jest.fn()
  }

  const enzymeWrapper = shallow(<Tasks {...props} />)
  return {
    props,
    enzymeWrapper
  }
}


describe('Tasks', () => {
  describe('Render', () => {
    it('should render self and subcomponents', () => {
       console.log('a');
       const { props, enzymeWrapper } = setup()
    })
  })
})
