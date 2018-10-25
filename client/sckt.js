
var WebSocket = require('ws')
// Create a socket instance
var socket = new WebSocket('ws://0.0.0.0:9000/tasks/');


// Open the socket
socket.onopen = function(event) {

    // Send an initial message
    socket.send('I am the client and I\'m listening!', 'aa');
	// To close the socket....
	//socket.close()

    // Listen for messages
    socket.onmessage = function(event) {
        console.log('Client received a message');
        console.log(event['data'])
    };

    // Listen for socket closes
    socket.onclose = function(event) {
        console.log('Client notified socket has closed');
    };

};
