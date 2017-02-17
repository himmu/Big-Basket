adminApp.controller('adminViewItemCtrl',function($scope,NgTableParams,$http,urls,toaster,$state){
	$scope.viewitemInit = function(){
		$scope.getItems()
		
	}


	$scope.delete_item = function(item_id){
		
		$http({
			url:urls.BASE_API+"/api/delete-item/",
			method:'delete',
			headers:{
				"Content-Type": 'application/x-www-form-urlencoded'
			},
			data:JSON.stringify(item_id)
			}).then(function successCallback(response){
				toaster.pop('info', "Success", response.data.message);
				$scope.getItems()
			
				
			},function errorCallback(response){

		});		
	}
	

	$scope.getItems = function(){
		$http({
			url:urls.BASE_API+"/api/get-item/",
			method:'get',
			headers:{
				"Content-Type": 'application/x-www-form-urlencoded'
			}
				
			}).then(function successCallback(response){
				$scope.item_list = response.data.item_list
			
				$scope.tableParams = new NgTableParams({}, { dataset: $scope.item_list});
			},function errorCallback(response){

		});		
	}

	$scope.edit_item = function(item){
		$state.go('base.edititems',{'item_id':item.id})
	}

	
}) 