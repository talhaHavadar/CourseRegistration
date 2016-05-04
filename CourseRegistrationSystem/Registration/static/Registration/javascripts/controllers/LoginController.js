/**
 * Created by gulgu on 28.04.2016.
 */
app.controller("LoginController", ["$scope","StudentService","$window", function ($scope, StudentService, $window) {

    $scope.login = function($event) {
      $event.preventDefault();
      var sNo = $scope.username !== undefined ? $scope.username.trim() : null;
      var password = $scope.password !== undefined ? $scope.password.trim() : null;

      if (sNo !== null && password !== null) {
        StudentService.login(sNo, password).then(function(data) {
          $window.location = "/index";
        }, function(data) {
          showAlert(data.message)
        });
      } else {
        showAlert("Please enter Student No and password")
      }
    };
    var showAlert = function(message) {
      $("#alert-container").empty();
      $("#alert-container").append('<div id="alert" class="alert alert-warning alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Warning!</strong> '+ message +'</div>');
    };
}]);
