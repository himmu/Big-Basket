adminApp.controller('adminEditItemCtrl',function($scope,$http,$state,toaster,urls,$stateParams){
	
	$scope.init_edit_item = function(){
		var post_data = {
				'item_id':$stateParams.item_id,
			}

		$http({
			url:urls.BASE_API+"/api/get-item-by-id/",
			method:'post',
			headers:{
				"Content-Type": 'application/x-www-form-urlencoded'
			},
			data:$.param(post_data)
		}).then(function successCallback(response){
			$scope.item_detail = response.data.item_detail
			$scope.category = response.data.category_list
			$scope.subcategories = response.data.subcategory_list
			
			$scope.category1 = $scope.item_detail[0].category_obj
			$scope.item_name= $scope.item_detail[0].name
			$scope.price= $scope.item_detail[0].price
			$scope.description= $scope.item_detail[0].description
			$scope.image = $scope.item_detail[0].image


		},function errorCallback(response){

		});
	}



	$scope.update_item = function(item_form){
		var formData = new FormData()
		// formData.append('category_id',item_form.category.$viewValue.id)
		// formData.append('subcategory_id',item_form.subcategory.$viewValue.id)
		formData.append('item_name',item_form.item_name.$viewValue)
		formData.append('price',item_form.price.$viewValue)
		formData.append('description',item_form.description.$viewValue)
		formData.append('item_id',$stateParams.item_id)

		try{
			formData.append('featureimage',$("#featureimage")[0].files[0])
		}catch(err){
			formData.append('featureimage',"")
		}
		


		if(item_form.$valid){
			$http({
			url:urls.BASE_API+"/api/update-item/",
			method:'post',
			headers:{
				"Content-Type": undefined
			},
			data:formData
			}).then(function successCallback(response){
				alert("Successfully updated")
				$state.reload()

			},function errorCallback(response){

			});
		}else{

		}
	}
})



