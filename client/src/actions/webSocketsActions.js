import {
	WEBSOCKET_CONNECT,
	WEBSOCKET_CONNECTING,
	WEBSOCKET_CONNECTED,
	WEBSOCKET_DISCONNECT,
	WEBSOCKET_DISCONNECTED,
	WEBSOCKET_MESSAGE
} from './types';

export const webSocketConnect = (host) => {
  return { type: WEBSOCKET_CONNECT, host };
};
export const webSocketConnecting = (host) => {
  return { type: WEBSOCKET_CONNECTING, host };
};
export const webSocketConnected = (host) => {
  return { type: WEBSOCKET_CONNECTED, host, };
};
export const webSocketDisconnect = (host) => {
  return { type: WEBSOCKET_DISCONNECT, host };
};
export const webSocketDisconnected = (host) => {
  return { type: WEBSOCKET_DISCONNECTED, host };
};
export const webSocketMessage = (host, payload) => {
	//console.log(payload)
  return { type: WEBSOCKET_MESSAGE, host, payload };
};