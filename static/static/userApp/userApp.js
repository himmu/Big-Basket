var userApp = angular.module('user_app',['ui.router','ngMessages','ngTable','toaster','ngAnimate',])


.constant('urls',{
    BASE_API:"http://localhost:8002"
})

.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
})


.config(function($stateProvider,$locationProvider,$urlRouterProvider,$httpProvider) {

        $httpProvider.interceptors.push(['$q', '$location', function ($q, $location) {
            return {
                'request': function (config) {
                    config.headers = config.headers || {};
                    if (window.localStorage['token']) {
                        config.headers.Authorization = window.localStorage['token'];
                    }else{
                        config.headers.Authorization = "avishek"
                    }

                    return config;
                },
                'responseError': function (response) {
                    // debugger;
                    if (response.status === 401) {
                        // $location.path('/unauthorized');
                    }else if(response.status === 403){
                        $location.path('/forbidden');
                    }/*else if(response.data == null && response.statusText === ""){
                     globalService.toast("negative", "Unable to contact the backend");
                     }*/
                    return $q.reject(response);
                }
            };
        }]);
 
        $stateProvider

        	.state('base',{
        		templateUrl:'/static/userApp/partials/userBase.html',
        		Abstract:true,
                controller:"headerCtrl"
        	})
            .state('login', {
                url: '/login',
                templateUrl: '/static/userApp/partials/userLogin.html',
                controller: 'userLoginCtrl',
            })

            .state('base.item_list', {
                url: '/products',
                templateUrl: '/static/userApp/partials/userItemList.html',
                controller: 'userItemCtrl',
            })

             .state('item_detail', {
                url: '/products-detail/{item_id}',
                templateUrl: '/static/userApp/partials/userItemdetail.html',
                controller: 'userItemdetailCtrl',
                params:{
                    'item_id':null
                }
            })


            $urlRouterProvider.otherwise('login')



    });

userApp.run(function($rootScope){
    $rootScope.media_url = "http://localhost:8002/media/"
})