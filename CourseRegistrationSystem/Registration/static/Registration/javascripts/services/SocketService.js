app.factory("SocketService", function() {
  var factory = {};
  var socket = undefined;

  factory.getSocket = function() {
    return socket;
  };

  factory.connect = function(onopenCallback, onmessageCallback, connecturl) {
    connecturl = "ws://127.0.0.1:8000/web" || connecturl;
    socket = new WebSocket(connecturl);
    socket.onopen = onopenCallback;
    socket.onmessage = function (data) {
      onmessageCallback(JSON.parse(data.data));
    };
  };

  factory.isConnected = function() {
    return socket !== undefined;
  };

  factory.close = function() {
    socket.close();
    socket = undefined;
  };

  factory.send = function(data) {
    socket.send(JSON.stringify(data));
  };

  return factory;
});
