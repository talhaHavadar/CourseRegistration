app.factory("CourseService",function($http, $q){ 
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
	};
	

	factory.filterCourse = function(cumulative){

	};

	factory.grouppingCourse = function(classID){

	};

	return factory;
});
