adminApp.controller('adminViewItemCtrl',function($scope,NgTableParams){
	$scope.viewitemInit = function(){

		var data = [{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'},{name: "Moroni", age: 50,sex:'Male'}, /*,*/];
		$scope.tableParams = new NgTableParams({}, { dataset: data});
	}
	
})