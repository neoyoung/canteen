// Require.js allows us to configure shortcut alias
require.config({
	// The shim config allows us to configure dependencies for
	// scripts that do not call define() to register a module
	shim: {

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
		jquery: '../lib/jquery/jquery',
        jqueryReveal:'../lib/jquery/jquery.reveal',
        bootstrap:'../lib/bootstrap/bootstrap.min'
	}
});

// Start the main app logic.
requirejs(['jquery', 'jqueryReveal', 'bootstrap'],
      function ($,jqueryReveal,bootstrap,base,User) {
      $('#myTab a').click(function (e) {
         e.preventDefault();
         $(this).tab('show');
         });
      });
