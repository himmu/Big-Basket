adminApp.controller('adminAddCategoryCtrl',function($scope,$http,urls,toaster){
	
	$scope.add_category = function(category_form){
		
		if(category_form.$valid){
			
			var post_data={
				"category_name":category_form.category_name.$viewValue
			}
			$http({
				url:urls.BASE_API+"/api/add-category/",
				method:'post',
				headers:{
					"Content-Type": 'application/x-www-form-urlencoded'
				},
				data:$.param(post_data)
			}).then(function successCallback(response){
				toaster.pop('info', "Success", response.data.message);
				
			},function errorCallback(response){

			});
		}else{
			
		}

	}

}) ;