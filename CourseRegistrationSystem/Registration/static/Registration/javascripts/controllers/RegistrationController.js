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
    for (var i = 0; i < data.courses.length; i++) {
      data.courses[i].selectedIns = "";
      $scope.courses.push(data.courses[i]);
    }
    console.log($scope.courses);
  }, function (data) {
    console.log("courses", data);
  });

  $scope.submitRegCourse = function() {
    console.log($scope.courses);
    var valid = true;
    for (var i = 0; i < $scope.courses.length; i++) {
      if ($scope.courses[i].selectedIns === undefined || $scope.courses[i].selectedIns == "" ) {
        valid = false;
        break;
      }
    }

    if (valid) {

    } else {
      alert("Please select all courses instructor");
    }
  }


});
