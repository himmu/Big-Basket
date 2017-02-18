userApp.controller('headerCtrl',function($scope,$rootScope,$state){
	
	$rootScope.logout = function(){
		window.localStorage.removeItem('token')
		$state.go("login")
	}

	$scope.get_payload = function(){
		if(window.localStorage.getItem('token')!=undefined || window.localStorage.getItem('token')!=null){
			var encoded = window.localStorage.getItem('token').split('.')
			var user_detail = window.atob(encoded[1])
			user_detail = JSON.parse(user_detail)
			return user_detail
		}else{
			return null
		}
	}
	
	
	if($scope.get_payload()!=null){
		$rootScope.username=$scope.get_payload().email
	}
})