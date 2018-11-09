import React from 'react';
import { shallow, mount } from 'enzyme';
import { MemoryRouter } from 'react-router-dom';

import Root from '../../../Root';
import Tasks from '../Tasks';

let wrapped;
beforeEach(() => {
  wrapped = mount(
    <Root>
      <MemoryRouter>
        <Tasks />
      </MemoryRouter>
    </Root>
  );
});

afterEach(() => {
  wrapped.unmount();
});

it('should render propertly', () => {
  expect(wrapped.find('h1').text()).toBe('Tasks');
  expect(wrapped.find('a').text()).toBe('Add task');
});

// function setup() {
//   const props = {
//     getTasks: jest.fn()
//   }

//   const enzymeWrapper = shallow(
//     <Root>
//       <Tasks {...props} />
//     </Root>
//   )
  
//   return {
//     props,
//     enzymeWrapper
//   }
// }

// describe('Tasks component', () => {
//   describe('Render', () => {
//     it('should render self and subcomponents', () => {
//        const { props, enzymeWrapper } = setup();
//        //console.log(props);
//        console.log(enzymeWrapper);
//     })
//   })
// })
