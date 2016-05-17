app.controller("RegistrationController", function($scope, SocketService, RegistrationService, CourseService, StudentService) {
  var onopen = function() {
    console.log("Connected to socket.");
    SocketService.send({
      "deneme": 123456
    });
  };
  $scope.courses = [];
  $scope.selected = false;
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

  function getSelectedCourses() {
    var res = [];
    for (var i = 0; i < $scope.courses.length; i++) {
      if($scope.courses[i].selected == true) {
        res.push($scope.courses[i])
      }
    }
    return res;
  }

  $scope.submitRegCourse = function() {
    console.log($scope.courses);
    var valid = true;
    for (var i = 0; i < $scope.courses.length; i++) {
      if (($scope.courses[i].selectedIns === undefined || $scope.courses[i].selectedIns == "") && $scope.courses[i].selected == true) {
        valid = false;
        break;
      }
    }

    if (valid) {
      var selecteds = getSelectedCourses();
      if(RegistrationService.checkCreditConstraint(selecteds)) {
        RegistrationService.completeRegistration(selecteds);
      } else {
        alert("Please check your courses");
      }
    } else {
      alert("Please select all courses instructor");
    }
  }


});
