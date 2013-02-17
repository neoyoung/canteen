define(['jquery','../lib/oop/Class'],function ($,Class) {
   
   var User = Class.extend({
      init: function (data, config) {
         //do something here
      },
      
      //juge whether user has login
      isLogin:function () {
         return ($('#username').size() > 0);
      }

   });

   return User;

});
