import React, { Component } from "react";
import { connect } from "react-redux";
import { webSocketConnect } from "../../actions/webSocketsActions";


class WebSocketContainer extends Component {
  constructor(props) {
    super(props);
    this.autoconnect = !!props.autoconnect;
  }

  componentDidMount() {
    if (this.autoconnect) {
      this.props.webSocketConnect(this.props.host);
    }
  }

  render() {
    return <div>{this.props.children}</div>
  }
}


const mapStateToProps = (state) => {
  return {
    webSocketsEvents: state.webSocketsReducer
  }
};

const mapDispatchToProps = {webSocketConnect};

export default connect(mapStateToProps, mapDispatchToProps)(WebSocketContainer);