import * as webSocketsActions from "./../actions/webSocketsActions";
import {
  WEBSOCKET_CONNECT,
  WEBSOCKET_DISCONNECT
} from '../actions/types';


const webSocketsMiddleware = (function () {
  let socket = null;

  /**
   * Handler for when the WebSocket opens
   */
  const onOpen = (ws, store, host) => event => {
    // Authenticate with Backend... somehow...
    store.dispatch(webSocketsActions.webSocketConnected(host))
  };

  /**
   * Handler for when the WebSocket closes
   */
  const onClose = (ws, store, host) => event => {
    store.dispatch(webSocketsActions.webSocketDisconnected(host))
    console.log('Socket is closed. Reconnect will be attempted in 5 second.', event.reason);
    setTimeout(() => {
      store.dispatch(webSocketsActions.webSocketConnect(host));
    }, 5000);
    
  };

  /**
   * Handler for when a message has been received from the server.
   */
  const onMessage = (ws, store) => event => {
    const payload = JSON.parse(event.data);
    store.dispatch(webSocketsActions.webSocketMessage(event.host, payload))
  };

  /**
   * Middleware
   */
  return store => next => action => {
    switch (action.type) {

      case WEBSOCKET_CONNECT:
        if (socket !== null) {
          socket.close()
        }

        // Pass action along
        next(action);

        // Tell the store that we're busy connecting...
        store.dispatch(webSocketsActions.webSocketConnecting(action.host));

        // Attempt to connect to the remote host...
        socket = new WebSocket(action.host);

        // Set up WebSocket handlers
        socket.onmessage = onMessage(socket, store);
        socket.onclose = onClose(socket, store, action.host);
        socket.onopen = onOpen(socket, store, action.host);

        break;

      case WEBSOCKET_DISCONNECT:
        if (socket !== null) {
          socket.close()
        }
        socket = null;

        // Tell the store that we've been disconnected...
        store.dispatch(webSocketsActions.webSocketDisconnected(action.host));

        break;

      default:
        return next(action);
    }
  };
})();

export default webSocketsMiddleware;