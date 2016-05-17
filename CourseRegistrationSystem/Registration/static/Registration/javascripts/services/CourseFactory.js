app.factory("CourseService",function($http, $q, StudentService){
	var factory = {};

	factory.getCourse = function(){
	var deferred = $q.defer();
		$http.post('/courseregistration',{
			"method": "courses"
			}).then(function(data){
				console.log(data);
				if(data.status == 200 && data.data.success == true){
					deferred.resolve(data.data);
				} else {
	        		deferred.reject({
	          		success: false,
	          		message: data.data.message
	        	}, function(data) {
	      			console.log(data);
	      			if(data.status == 200){
	      				deferred.reject(data.data)
	      			}else{
	      				deferred.reject({
	      					success:false,
	      					message: "Something went wrong"
	      				});
	      			}
	    		});
	      	}
		});
		return deferred.promise;
	};

	factory.getUpCourse = function(){
		var deferred = $q.defer();
		$http.post('/courseregistration',{
			"method":"courses_up"
		}).then(function(data){
			if(data.status == 200 && data.data.success == true){
				deferred.resolve(data.data);
			} else {
	        	deferred.reject({
	          	success: false,
	          	message: data.data.message
	        }, function(data) {
	      		console.log(data);
	      		if(data.status == 200){
	      			deferred.reject(data.data)
	      		}else{
	      			deferred.reject({
	      				success:false,
	      				message: "Something went wrong"
	      			});
	      		}
	    	});
	    }
	});
		return deferred.promise;
	}

	factory.filterCourse = function() {
		var deferred = $q.defer();
		StudentService.me().then(function (data) {
			var student = data.student;
			if(student.transcript.cumulative >= 2.5){
				factory.getUpCourse().then(function(data) {
					var courses = data.courses;
					console.log(courses);
					deferred.resolve({
						success: true,
						courses: courses
					});
				}, function (data) {
					deferred.reject({
						success: false,
						message: "Something went wrong"
					});
				});
			}
		}, function (data) {
			deferred.reject({
				success: false,
				message: "Something went wrong"
			})
		});
		return deferred.promise;
	};

	factory.grouppingCourse = function(classID){

	};
	return factory;
});
