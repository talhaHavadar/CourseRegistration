app.factory("CourseService",function($http, $q){
	var factory = {};



	factory.getCourse = function(){
		var deferred = $q.defer();
		$http.post("/courseregistration", {
			"method": "courses" 
		}).then(function (data) {
			console.log("data",data);
		}, function (data) {
			console.log("data",data);
		});
	};

	factory.filterCourse = function(cumulative){

	};

	factory.grouppingCourse = function(classID){

	};

	return factory;
});
