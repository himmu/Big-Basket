userApp.controller('userItemCtrl',function($scope,$http,urls,$rootScope,$state){
	$scope.itemlist_init = function(){
		$scope.getCategory()
		$scope.getItems()
	}

	$scope.getItems = function(){
		$http({
			url:urls.BASE_API+"/api/get-item/",
			method:'get',
			headers:{
				"Content-Type": 'application/x-www-form-urlencoded'
			},
			
		}).then(function successCallback(response){
			$scope.itemlist = response.data.item_list
			
		},function errorCallback(response){

		});
	}

	$scope.getCategory = function(){
		$http({
		url:urls.BASE_API+"/api/get-category",
		method:'get',
		headers:{
			"Content-Type": 'application/x-www-form-urlencoded'
		}
			
		}).then(function successCallback(response){
			$rootScope.category = response.data.category_list
			
		},function errorCallback(response){

		});
	}

	$scope.view_item = function(item){
		alert("This page will update shortly")
		/*$state.go('item_detail',{'item_id':item.id})*/
	}
})