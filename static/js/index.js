$(function () {



    function deflaut_display(){
    let main_display = $(".main-display");
    main_display.html(`
            <div class="main-background-info">
            </div>`)
    }

    let homedisplay = $(".main-display").html()
    let btnLog = $(".btn-log");
    let mainBtnSign = $(".btn-sign");
    let mainText = $(".main-display-log");
    let loginDivForm = $(".login-div-form");
    let signUpForm = $(".signup-div-form");

       let main_display = $(".main-display");

   let homebtn = $("#home");
   homebtn.on("click", function () {
        $.ajax({
            method: "GET",
            url: "home/",
            success: main_display.html(homedisplay)
        })
        });

    let aboutUs = $("#aboutUs");
    aboutUs.on("click", function () {
        $.ajax({
            method: "GET",
            url: "about/",
            success: deflaut_display
        })
        });

    let contact = $("#contact");
    contact.on("click", function () {
        $.ajax({
            method: "GET",
            url: "contact/",
            success: deflaut_display
        })
    });

    btnLog.on("click", function () {
       loginDivForm.css("display", "block");
       mainText.css("top", "25%");
       mainText.css("transition", "1s");
       hidebtn();
   });

   mainBtnSign.on("click", function () {
      signUpForm.css("display", "block");
      mainText.css("top", "6.8%");
      mainText.css("transition", "2s");
      hidebtn();
   });

   function hidebtn() {
       btnLog.css("display", "none");
       mainBtnSign.css("display", "none");
   }

   //registration

   let choice_user = $("#choice_user");
   let choice_company = $("#choice_company");
   let signCompanyFields = $(".sign-company-fields");
   let signUserFields = $(".sign-user-fields");

   choice_user.on("click", function () {
       signUserFields.css("display", "block");
       signCompanyFields.css("display", "none");

   });

   choice_company.on("click", function () {
       signUserFields.css("display", "none");
       signCompanyFields.css("display", "block");

   });


    let btnLoginUser = $(".btn-log-conf");

    btnLoginUser.on("click", function () {
        $.ajax({
            type: 'POST',
            url: '/login/',
            data: {
                email: $("#email_idd").val(),
                password: $("#password_idd").val(),
                csrfmiddlewaretoken: $("input[name*=csrfmiddlewaretoken]").val()
            },
    }).done(function(data) {
            location.href=data["url"];
        });
    });

    let btnLogout = $("#logout");

    btnLogout.on("click", function () {
        $.ajax({
            method: "GET",
            url: "/logout/",
            success:function(response) {
           window.location.href = "http://127.0.0.1:8000";
                }
        })
        });
    let dailyTaskOpt = $(".dailyTask-options-block");
    let reclamationOpt = $(".reclamation-options-block");

    let reclamationBtn = $("#reclamation");

    reclamationBtn.on("click", function () {
        if (reclamationOpt.css("display") === 'none') {
            reclamationBtn.children().removeClass("fa fa-angle-down").addClass("fa fa-angle-right");
            dailyTaskBtn.children().removeClass("fa fa-angle-right").addClass("fa fa-angle-down");
            dailyTaskOpt.css("display", "none");
            reclamationOpt.css("display", "block");
        }else{
            reclamationBtn.children().removeClass("fa fa-angle-right").addClass("fa fa-angle-down");
            dailyTaskOpt.css("display", "none");
            reclamationOpt.css("display", "none");
            }
    });

    let dailyTaskBtn = $("#dailyTask");
    dailyTaskBtn.on("click", function () {

        if (dailyTaskOpt.css("display") == 'none') {
            dailyTaskBtn.children().removeClass("fa fa-angle-down").addClass("fa fa-angle-right");
            reclamationBtn.children().removeClass("fa fa-angle-right").addClass("fa fa-angle-down");
            reclamationOpt.css("display", "none");
            dailyTaskOpt.css("display", "block");
        }else{
            dailyTaskBtn.children().removeClass("fa fa-angle-right").addClass("fa fa-angle-down");
            reclamationOpt.css("display", "none");
            dailyTaskOpt.css("display", "none");
            }

    });

    // function changeListIcon(parent) {
    //     console.log(parent.childNodes);
    // }
    // }
    let registerBtn = $(".btn-sign-conf");

    registerBtn.on("click", function () {
        let inputs = $("#register");
        console.log($('input[name="csrfmiddlewaretoken"]').val());
        console.log(JSON.stringify(inputs.serializeArray()));
        let radio_user = $("#choice_user");

        if(radio_user.prop("checked")){
            $.ajax({url: '/register/', type: 'POST',
            data: {
                login: $("#login_user").val(),
                firstname: $("#name").val(),
                lastname: $("#surname").val(),
                email: $("#email").val(),
                password: $("#password").val(),
                csrfmiddlewaretoken: $("input[name*=csrfmiddlewaretoken]").val()
            }
        })
        }else{
            $.ajax({url: '/register/', type: 'POST',
            data: {
                company_name: $("#company_name").val(),
                company_email: $("#company_email").val(),
                company_post_code: $("#post_code").val(),
                company_city: $("#city").val(),
                company_street: $("#street").val(),
                company_house_number: $("#company_house_number").val(),
                company_number: $("#company_number").val(),
                company_password: $("#company_password").val(),
                csrfmiddlewaretoken: $("input[name*=csrfmiddlewaretoken]").val()
            }
        })
        }
    });



});