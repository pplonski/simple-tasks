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
  // static getDerivedStateFromProps(props) {
  //   console.log(props);
  //   if(props.webSockets.status==='disconnected') {
  //     console.log('disconnected!!!');
  //     props.webSocketConnect(props.host);
  //   }
  //   return null
  // }
  
  render() {
    //console.log(this.props.webSocketsEvents)
    return <div>{this.props.children}</div>
  }
}


const mapStateToProps = (state) => {
  //console.log(state.webSocket)
  return {
    webSockets: state.webSocket
  }
};

const mapDispatchToProps = {webSocketConnect};

export default connect(mapStateToProps, mapDispatchToProps)(WebSocketContainer);