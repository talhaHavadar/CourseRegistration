/**
 * Created by gulgu on 28.04.2016.
 */
app.controller("MainController", ["$scope",'CourseService','StudentService', function ($scope,CourseService, StudentService) {
    $scope.currentPage = 0;
    $scope.setPage = function (index) {
        $scope.currentPage = index;
    };

    $scope.isOnPage = function(index){
        return $scope.currentPage == index;
    };
    //StudentService.me();
   	CourseService.filterCourse();

}]);
