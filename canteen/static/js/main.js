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

               if (document.cookie && document.cookie !=='') {

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

         $(document).ready(function() {

               var subBtn = $('#ship'),
                   success = $('#ship-form .js-msg'),
                   radioContainer = $('#ship-form .js-container');

               $('#ship').bind('click', function () {

                  var val = $('#ship-form').find('input[name="order_type"]:checked').val(),
                  data = {order_type: val},
                  msg;

                  $.post("/order/add/",data,function(data) {

                     //radioContainer.hide();

                     if (data.success === 'True') {
                        //success.html('已经订餐. =)');
                        //subBtn.addClass("disabled");
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
