adminApp.controller('adminAddItemCtrl',function($scope,urls,$http,toaster){
	
	$scope.init_add_item = function(){
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

	$scope.get_subcategories = function(subcategory_form){
		var post_data = {
				'category_id':subcategory_form.category.$viewValue.id,
			}

		$http({
			url:urls.BASE_API+"/api/get-sub-category-by-id/",
			method:'post',
			headers:{
				"Content-Type": 'application/x-www-form-urlencoded'
			},
			data:$.param(post_data)
		}).then(function successCallback(response){
			$scope.subcategories = response.data.subcategory_list
			
		},function errorCallback(response){

		});
	}

	$scope.add_item = function(subcategory_form){
		if(subcategory_form.$valid){

			var formData = new FormData()
			formData.append('sub_category_id',subcategory_form.subcategory.$viewValue.id)
			formData.append('item_name',subcategory_form.item_name.$viewValue)
			formData.append('description',subcategory_form.description.$viewValue)
			formData.append('price',Number(subcategory_form.price.$viewValue))
			formData.append('feature_image',$('#featureimage')[0].files[0])
			
			
			$http({
				url:urls.BASE_API+"/api/add-item/",
				method:'post',
				headers:{
					"Content-Type": undefined
				},
				data:formData
			}).then(function successCallback(response){
				toaster.pop('info', "Success", response.data.message);
				
			},function errorCallback(response){

			});
		}else{

		}
	}
})