import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

import { signOutUser } from '../../actions/authActions';

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

  onLogoutClick(e) {
    e.preventDefault();
    //this.props.clearCurrentProfile();
    this.props.signOutUser();
  }

  render() {
    const { isAuthenticated, user } = this.props.auth;

    const guestLinks = (
      <Nav className="ml-auto" navbar>
        <NavItem>
          <Link to="/sign-in/" className="nav-link">Sign In</Link>
        </NavItem>
        <NavItem>
          <Link to="/sign-up/" className="nav-link">Sign Up</Link>
        </NavItem>
      </Nav>
    );

    const authLinks = (
      <Nav className="ml-auto" navbar>
        <NavItem>
          <a href="#" className="nav-link" onClick={this.onLogoutClick.bind(this)}>Sign Out ({user.username})</a>
        </NavItem>
      </Nav>
    )

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
          { isAuthenticated ? authLinks : guestLinks }
        </Collapse>
      </Navbar>
    );
  }
}

NavbarMain.propTypes = {
  auth: PropTypes.object.isRequired
}

const mapStateToProps = (state) => ({
  auth: state.auth
})

export default connect(mapStateToProps, { signOutUser })(NavbarMain);