app.factory("RegistrationService", function($http, $q, SocketService) {
  var factory = {};

  factory.checkCreditConstraint = function (selectedCourses) {
    if (SocketService.isConnected()) {
      var sum = 0;
      for (var i = 0; i < selectedCourses.length; i++) {
        sum += selectedCourses[i].credit;
      }
      if (sum <= 21 && sum > 0) {
        return true;
      } else {
        return false;
      }
    } else {
      alert("Socket connection is invalid please reload the page!");
    }
  };

  factory.completeRegistration = function(selectedCourses){
		var deferred = $q.defer();
		$http.post('/courseregistration', {
      "method": "registration",
      "courses": selectedCourses
    }).then(function(data) {
      console.log(data);
    }, function (data) {
      console.log(data);
    });
		return deferred.promise;
	};



  return factory;
});
