import React from 'react';
import { connect } from 'react-redux';
import classnames from 'classnames';
import PropTypes from 'prop-types';

import { webSocketDisconnect } from '../../actions/webSocketsActions';

class FooterMain extends React.Component {
  onWebsocketDisconnectClick() {
    this.props.webSocketDisconnect();
  }
  render() {
    const { status } = this.props.webSocket;

    return (
      <footer className="footer">
        <div className="container-fluid">
          <div className="text-muted"><span className="badge badge-light">WebSocket status:</span> 
            <span 
              className={
                classnames( 'badge', 
                {'badge-success': ( status === 'connected' )},
                {'badge-info': ( status === 'connecting' )},
                {'badge-danger': ( status === 'disconnected' )}
              )}
              onClick={this.onWebsocketDisconnectClick.bind(this)}
            >
              {status}
            </span>
          </div>
        </div>
      </footer>
    );
  }
}

FooterMain.propTypes = {
  webSocket: PropTypes.object.isRequired
}

const mapStateToProps = (state) => ({
  webSocket: state.webSocket
})

export default connect(mapStateToProps, {webSocketDisconnect})(FooterMain);