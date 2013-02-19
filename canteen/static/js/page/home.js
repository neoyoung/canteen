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
requirejs(['jquery', 'jqueryReveal', 'bootstrap','../util/base','../user/User'],
      function ($,jqueryReveal,bootstrap,base,User) {

         $(function() {

               var subBtn = $('#ship'),
                   success = $('#ship-form .js-msg'),
                   radioContainer = $('#ship-form .js-container'),
                   user = new User();


               $('#ship').bind('click', function () {

                  var val = $('#ship-form').find('input[name="order_type"]:checked').val(),
                  data = {order_type: val},
                  msg;

                  if ( !user.isLogin() ) {
                     //redirect to the login page
                     window.location = '/accounts/login';
                     return false;
                  }

                  $.post("/order/add/",data,function(data) {

                     if (data.success === 'True') {
                        
                        msg = "<h4>订餐成功啦~</h4><p>去围观下今天谁拿第一哇.=)</p><a class='close-reveal-modal'>&#215;</a>";

                     } else {

                        msg = "<h4>貌似出问题了，上水群找下管理猿吧=(</h4><a class='close-reveal-modal'>&#215;</a>";
                     }

                     $('#success-confirm').empty().html(msg)
                                        .reveal({animation: 'fadeAndPop',
                                                 animationspeed: 300,
                                                 closeonbackgroundclick: false,
                                                 dismissmodalclass: 'close-reveal-modal'
                                               });
                     });

                  $(this).attr('disabled', 'disabled');

                  return false;

                  });

               //TODO support the cancel action
               //$('#cancel').bind('click', function () {
                     //$.post("/order/delete/",{},function(data) {
                        //if (data.success === 'True') {
                        //console.log("delete success");
                        //} else {
                        //console.log("not work");
                        //}
                        //});
                     //});
         });
      });
