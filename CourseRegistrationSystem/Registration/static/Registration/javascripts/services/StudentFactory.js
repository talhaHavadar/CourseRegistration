app.factory("StudentService", function($http, $q) {
  var factory = {};
  factory.login = function(studentNo, password) {
    var deferred = $q.defer();
    $http.post('/login', {
      studentNo: studentNo,
      password: password
    }).then(function(data) {
      console.log(data);
      if (data.status == 200 && data.data.success == true) {
        deferred.resolve(data.data);
      } else {
        deferred.reject({
          success: false,
          message: data.data.message
        });
      }
    }, function(data) {
      console.log(data);
      if (data.status == 200) {
        deferred.reject(data.data)
      } else {
        deferred.reject({
          success: false,
          message: "Something went wrong"
        });
      }
    });
    return deferred.promise;
  };

  factory.logout = function() {
    alert("Logout id not implemented yet!");
  };

  factory.me = function() {
    alert("Me is not implemented yet!");
  };

  return factory;
});
