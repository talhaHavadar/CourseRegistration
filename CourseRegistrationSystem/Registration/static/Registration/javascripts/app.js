/**
 * Created by gulgu on 28.04.2016.
 */
var app = angular.module("CourseRegistrationApp", []);
app.config(['$httpProvider', '$locationProvider', function ($httpProvider, $locationProvider) {
  $locationProvider.html5Mode(true);
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
