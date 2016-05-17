app.controller("RegistrationController", function($scope, SocketService, RegistrationService, CourseService) {
  var onopen = function() {
    console.log("Connected to socket.");
    SocketService.send({
      "deneme": 123456
    });
  };
  $scope.courses = [];
  SocketService.connect(onopen, function (data) {
    console.log(data);
  });

  CourseService.getCourse().then(function (data) {
    console.log("courses", data);
    $scope.courses = data.courses;
  }, function (data) {
    console.log("courses", data);
  })

});
