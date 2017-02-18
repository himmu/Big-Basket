var adminApp = angular.module('admin_app',['ui.router','ngMessages','ngTable','toaster','ngAnimate',])

.constant('urls',{
    BASE_API:"https://bigbasket-demo.herokuapp.com"
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
        		templateUrl:'/static/adminApp/partials/adminBase.html',
        		Abstract:true,
                controller:'headerCtrl'
        	})
            .state('login', {
                url: '/login',
                templateUrl: '/static/adminApp/partials/adminLogin.html',
                controller: 'adminLoginCtrl',
            })



            .state('base.dashboard', {
                url: '/dashboard',
                templateUrl: '/static/adminApp/partials/adminViewItem.html',
                controller: 'adminViewItemCtrl',
            })

            .state('base.addcategory', {
                url: '/add-category',
                templateUrl: '/static/adminApp/partials/adminAddCategory.html',
                controller: 'adminAddCategoryCtrl',
            })

            .state('base.addsubcategory', {
                url: '/add-subcategory',
                templateUrl: '/static/adminApp/partials/adminAddSubcategory.html',
                controller: 'adminAddSubcategoryCtrl',
            })

            .state('base.additems', {
                url: '/add-items',
                templateUrl: '/static/adminApp/partials/adminAddItem.html',
                controller: 'adminAddItemCtrl',
            })

            .state('base.viewitems', {
                url: '/view-items',
                templateUrl: '/static/adminApp/partials/adminViewItem.html',
                controller: 'adminViewItemCtrl',
            })

            .state('base.edititems', {
                url: '/edit-items/{item_id}',
                templateUrl: '/static/adminApp/partials/adminEditItem.html',
                controller: 'adminEditItemCtrl',
                params:{
                    'item_id':null
                }
            })


            $urlRouterProvider.otherwise('login')



    });

adminApp.run(function($rootScope){
    $rootScope.media_url = "https://bigbasket-demo.herokuapp.com/media/"
})

