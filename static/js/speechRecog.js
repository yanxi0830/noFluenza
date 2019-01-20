const app = angular.module('webApp', []);

app.controller('iFlushotController', function($scope, $http) {
    
    // get all reasons
	$scope.getAllReasons = function() {
		$http.get('/reasons').then((response) => {
			$scope.allReasons = response.data;
		});
    }
    
    // delete a Reason
    $scope.removeReason = function(reasonID) {
        const route = `/delete/${reasonID}`

        $http.delete(route).then((response) => {
            for(let i = 0; i < $scope.allReasons.length; i++) { // updates webApp without needing to refresh
                if(reasonID === $scope.allReasons[i]._id) {
                    $scope.allReasons.splice(i,1)
                }
            }
        })
    }
    
    // post a Reason
    $scope.addReason = function(reasonID) {

        const reason = {
            'comment': $scope.reasonComment,
            'date': new Date()
        };
        $scope.reasonComment = '';
        const route = `/add`;
        $http.post(route, reason).then((response) => {
            $scope.allReasons.push(response.data);
        });
    }

    $scope.convertDate = function(date) {
        date = new Date(date);
        const months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        return `${months[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}`;
    }

    $scope.getAllReasons();
});