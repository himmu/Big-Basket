userApp.controller('userItemdetailCtrl',function($scope,$http,urls,$stateParams){
	$scope.item_detail_init = function(){
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
			
		},function errorCallback(response){

		});
	}
})