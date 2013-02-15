// Require.js allows us to configure shortcut alias
require.config({
	// The shim config allows us to configure dependencies for
	// scripts that do not call define() to register a module
	shim: {
		//underscore: {
			//exports: '_'
		//},
		//backbone: {
			//deps: [
				//'underscore',
				//'jquery'
			//],
			//exports: 'Backbone'
		//},
		//backboneLocalstorage: {
			//deps: ['backbone'],
			//exports: 'Store'
		//},
        "bootstrap":{
           deps:['jquery'],
           exports: "$.fn.popover"
         },

         "jqueryReveal":{
            deps:['jquery'],
            exports: "$.fn.reveal"
         }
   },
	paths: {
		jquery: 'lib/jquery/jquery',
        jqueryReveal:'lib/jquery/jquery.reveal',
        bootstrap:'lib/bootstrap/bootstrap.min'
	}
});

// Start the main app logic.
requirejs(['jquery', 'jqueryReveal', 'bootstrap'],
      function ($) {

      //solve the csrf validate
         $('html').ajaxSend(function(event, xhr, settings) {

            function getCookie(name) {

               var cookieValue = null;

               if (document.cookie && document.cookie !='') {

                  var cookies = document.cookie.split(';');

                  for (var i = 0; i < cookies.length; i++) {

                     var cookie = $.trim(cookies[i]);

                     // Does this cookie string begin with the name we want?

                     if (cookie.substring(0, name.length + 1) == (name + '=')) {

                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));

                        break;

                     }

                  }

               }

               return cookieValue;

            }

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {

               // Only send the token to relative URLs i.e. locally.

               xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));

            }

         });

         //TODO order CRUD
         $(document).ready(function() {

            $('body').bind('click', function () {
               $.get("/order/",function(data) {
                  if (data.success === 'True') {
                     console.log("show the data");
                  } else {
                     console.log("hide the data");
                  }
               });
            });

            $('#lunch').bind('click', function () {
               $.post("/order/add/",{order_type:1},function(data) {
                  console.log(data);
                  if (data.success === 'True') {
                     console.log("add success");
                  } else {
                     console.log("not work");
                  }
               });
            });

            $('#cancel').bind('click', function () {
               $.post("/order/delete/",{},function(data) {
                  if (data.success === 'True') {
                     console.log("delete success");
                  } else {
                     console.log("not work");
                  }
               });
            });

         });
      });
