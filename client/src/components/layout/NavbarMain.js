import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  Nav,
  NavItem,
  //NavLink,
  //UncontrolledDropdown,
  //DropdownToggle,
  //DropdownMenu,
  //DropdownItem 
} from 'reactstrap';

class NavbarMain extends React.Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  render() {

    return (
      <Navbar color="light" light expand="md" className="mb-3">
        
        <Link to="/" className="navbar-brand">Simple Tasks</Link>
        <NavbarToggler onClick={this.toggle} />
        <Collapse isOpen={this.state.isOpen} navbar>
          <Nav className="mr-auto" navbar>
            <NavItem>
              <Link to="/tasks/" className="nav-link">Tasks</Link>
            </NavItem>
          </Nav>
          <Nav className="ml-auto" navbar>
          </Nav>
        </Collapse>
      </Navbar>
    );
  }
}

export default connect(null)(NavbarMain);