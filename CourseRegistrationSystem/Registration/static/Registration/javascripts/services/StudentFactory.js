app.factory("StudentService", function($http, $q) {
  var factory = {};
  factory.login = function(studentNo, password) {
    var deferred = $q.defer();
    $http.post('/login', {
      studentNo: studentNo,
      password: password
    }).then(function(data) {
      if (data.status == 200 && data.data.success == true) {
        deferred.resolve(data.data);
      } else {
        deferred.reject({
          success: false,
          message: data.data.message
        });
      }
    }, function(data) {
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
    var deferred = $q.defer();
    $http.post("/courseregistration", {
      "method": "me"
    }).then(function (data) {
      console.log("me", data);
      if (data.data.success === true) {
        deferred.resolve(data.data);
      } else {
        deferred.reject(data.data);
      }
    }, function (data) {
      deferred.reject({ success: false, message: "Something went wrong" });
    });
    return deferred.promise;
  };

  return factory;
});
