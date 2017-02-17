userApp.controller('userLoginCtrl',function($scope,$state,$http,urls,toaster){
		$scope.login_init = function(){

		if($scope.get_payload()!=null){
			if($scope.get_payload().role=="User"){
				$state.go('base.item_list')
			}
		}else{
			$state.go('login')
		}
		
	}

	$scope.login = function(login_form){
		if(login_form.$valid){
				
				var post_data={
					"email":login_form.email.$viewValue,
					"password":login_form.password.$viewValue,
					"context":"User"
				}
				$http({
					url:urls.BASE_API+"/api/login/",
					method:'post',
					headers:{
						"Content-Type": 'application/x-www-form-urlencoded'
					},
					data:$.param(post_data)
				}).then(function successCallback(response){
					toaster.pop('info', "Success", response.data.message);
					window.localStorage.setItem('token',response.data.token)
					$state.go('base.item_list')
				},function errorCallback(response){
					toaster.pop('error', "Error", response.data.message);
				});
			}else{

			}
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
})