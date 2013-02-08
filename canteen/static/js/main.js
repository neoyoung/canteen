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
    //jQuery, canvas and the app/sub module are all
    //loaded and can be used here now.
    //console.log('hello world!');
   $(document).ready(function() {
      $('body').bind('click', function () {
         $.get("/order/get_order", function(data) {
            if (data.status) {
               console.log("show the data");
            } else {
               console.log("hide the data");
            }
            //$('body')[0].innerHTML=guess_result;
            });
         });
      });
});
