import {
  WEBSOCKET_CONNECT,
  WEBSOCKET_CONNECTING,
  WEBSOCKET_CONNECTED,
  //WS_DISCONNECT,
  WEBSOCKET_DISCONNECTED,
  //WS_MESSAGE
} from '../actions/types';

const initialState = {
  host: null,
  status: null
}

function webSocketsReducer(state = initialState, action) {
  //console.log(action.type);
  switch (action.type) {
    case WEBSOCKET_CONNECT:
      return {
        ...state,
        host: action.host,
        status: 'connect'
      }
    case WEBSOCKET_CONNECTING:
      return {
        ...state,
        host: action.host,
        status: 'connecting'
      }
    case WEBSOCKET_CONNECTED:
      return {
        ...state,
        host: action.host,
        status: 'connected'
      }
    case WEBSOCKET_DISCONNECTED:
      return {
        ...state,
        host: action.host,
        status: 'disconnected'
      }
    default:
      return state;
  }
}

export default webSocketsReducer;