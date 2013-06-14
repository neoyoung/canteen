// Require.js allows us to configure shortcut alias
require.config({
	// The shim config allows us to configure dependencies for
	// scripts that do not call define() to register a module
	shim: {

        "bootstrap":{
           deps:['jquery'],
           exports: "$.fn.popover"
         },

   },
	paths: {
		jquery: '../lib/jquery/jquery',
        bootstrap:'../lib/bootstrap/bootstrap.min'
	}
});

// Start the main app logic.
requirejs(['jquery', 'bootstrap','../util/base','../user/User'],
      function ($,bootstrap,base,User) {
         $(function() {});
});
