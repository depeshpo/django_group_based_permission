$(document).ready(function () {
    // $('#user_search_list').DataTable();

    $('#user_list_table').DataTable();

    var message = document.getElementById("msg");
    setTimeout(function () {
        message.style.display = "none";
    }, 8000);

    var reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    $('#user-creation').submit(function (event) {
        first_name = $("#first_name").val().trim()
        last_name = $("#last_name").val().trim()
        username = $("#username").val().trim()
        password = $("#password").val().trim()
        email = $("#email").val().trim()

        if (first_name.length == 0 || last_name.length == 0 || username.length == 0 || password.length == 0 || email.length == 0) {
            if (first_name.length == 0) {

                alert('first name required')
                $("#first_name").focus()
                return false
            }
            if (last_name.length == 0) {
                alert('last name required')
                $("#last_name").focus()
                return false
            }
            if (username.length == 0) {
                alert('username required')
                $("#username").focus()
                return false
            }
            if (password.length == 0) {
                alert('password required')
                $("#password").focus()
                return false
            }
            if (email.length == 0) {
                alert('email required')
                $("#email").focus()
                return false
            }
            return false
        } else if (username.length <= 5) {
            alert('Username must be greater than 5 characters.')
            $("#username").focus()
            return false
        } else if (!reg.test(String(email).toLowerCase())) {
            alert('Provide appropriate email format');
            $("#email").focus()
            return false;
        } else {
            return true;
        }
    });

    $("#first_name").on('click change focus', function () {
        if ($("#first_name").val().trim().length == 0) {
            $("#first_name").addClass('error-border')
            return false
        } else {
            $("#first_name").removeClass('error-border')
            return true
        }
    });

    $("#last_name").on('click change focus', function () {
        if ($("#last_name").val().trim().length == 0) {
            $("#last_name").addClass('error-border')
            return false
        } else {
            $("#last_name").removeClass('error-border')
            return true
        }
    });

    $("#email").on('click change focus', function () {
        if ($("#email").val().trim().length == 0) {
            $("#email").addClass('error-border')
            return false
        } else {
            $("#email").removeClass('error-border')
            return true
        }
    });

    $("#username").on('click change focus', function () {
        if ($("#username").val().trim().length == 0) {
            $("#username").addClass('error-border')
            return false
        } else if ($("#username").val().trim().length <= 5) {
            $("#username").addClass('error-border')
            return false
        } else {
            $("#username").removeClass('error-border')
            return true
        }
    });

    $("#password").on('click change focus', function () {
        if ($("#password").val().trim().length == 0) {
            $("#password").addClass('error-border')
            return false
        } else {
            $("#password").removeClass('error-border')
            return true
        }
    });
});
