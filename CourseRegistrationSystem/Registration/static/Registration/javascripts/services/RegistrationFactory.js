app.factory("RegistrationService", function($http, $q, SocketService) {
  var factory = {};

  factory.checkCreditConstraint = function (selectedCourses) {
    if (SocketService.isConnected()) {
      console.log();
    } else {
      alert("Socket connection is invalid please reload the page!");
    }
  }

  return factory;
});
