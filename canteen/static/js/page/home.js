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

            //wrap one more level .
            function showReveal(options){
               var defaults = {
                  animation: 'fadeAndPop',
                  animationspeed: 300,
                  closeonbackgroundclick: false,
                  dismissmodalclass: 'close-reveal-modal'
               };

               options = $.extend({}, defaults, options);

               $(options.target).empty().html(options.msg)
                  .reveal({animation: options.animation,
                     animationspeed: options.animationspeed,
                     closeonbackgroundclick: options.closeonbackgroundclick,
                     dismissmodalclass: options.dismissmodalclass
                  });
            }

               var subBtn = $('#ship'),
                   success = $('#ship-form .js-msg'),
                   radioContainer = $('#ship-form .js-container'),
                   user = new User(),
                   defaultMessage = "<p>貌似出问题了，上水群找下管理猿吧=(</p><a class='close-reveal-modal'>&#215;</a>",
                   blankError = "<p>E...你确定你选了=.=....</p><a class='close-reveal-modal'>&#215;</a>";

               //TODO handle the return code like 403, fail gracefully
               $('#ship').bind('click', function () {

                  var selected = [],
                      msg="";



                  // if ( !user.isLogin() ) {
                  //    //redirect to the login page
                  //    window.location = '/accounts/login';
                  //    return false;
                  // }

                  $('#ship-form input:checked').each(function() {
                      selected.push($(this).val());
                  });

                  if (selected.length === 0) {
                     showReveal({target:"#success-confirm",msg:blankError});
                     return false;
                  }

                  var data = { "offertime_type":selected},
                      posting = $.post("/order/add/",data);

                  posting.done(function(data) {

                     for (var i = 0; i < data.messageArr.length; i += 1) {

                        msg += "<p>"+data.messageArr[i]+"</p><a class='close-reveal-modal'>&#215;</a>";
                     }

                     showReveal({target:"#success-confirm",msg:msg});

                  });

                  //may never fall down here =)
                  posting.fail(function(data){

                     showReveal({target:"#success-confirm",msg:defaultMessage});

                  });

                  //$(this).attr('disabled', 'disabled');

                  return false;

                  });
         });
      });
