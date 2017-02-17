adminApp.controller('adminAddSubcategoryCtrl',function($scope,$http,urls,toaster){

	$scope.init_subcategory = function(){
		$http({
		url:urls.BASE_API+"/api/get-category",
		method:'get',
		headers:{
			"Content-Type": 'application/x-www-form-urlencoded'
		}
			
		}).then(function successCallback(response){
			$scope.category = response.data.category_list
			
		},function errorCallback(response){

		});
	}

	$scope.add_subcategory = function(subcategory_form){

		if(subcategory_form.$valid){
			var post_data = {
				'category_id':subcategory_form.category.$viewValue.id,
				'sub_category_name':subcategory_form.subcategory_name.$viewValue
			}

			$http({
				url:urls.BASE_API+"/api/add-sub-category/",
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

})