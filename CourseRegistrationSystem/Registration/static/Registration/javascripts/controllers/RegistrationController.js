app.controller("RegistrationController", function($scope, SocketService) {
  var onopen = function() {
    console.log("Connected to socket.");
    SocketService.send({
      "deneme": 123456
    });
  };

  SocketService.connect(onopen, function (data) {
    console.log(data);
  });

});
