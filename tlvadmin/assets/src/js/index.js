$(document).ready(function () {

    // Get Counter Users
    $.ajax({
        url: 'http://localhost:8000/api/rest/users/',
        type: 'get',
        success: function (result) {
            $("#user-overlay").hide();
            $('#user-registered').html(result.count);
        }
    })

    // User Module Table
    var table = $('#users-dash').DataTable({
        responsive: true,
        autoWidth: false,
        lengthChange: false,
        info: false,
        serverside: true,
        searching: false,
        pageLength: 10,
        scrollY: 200,
        ajax: {
            url: 'http://localhost:8000/api/rest/users/?format=datatables',
        },
        columns: [
            { data: "username" },
            { data: "first_name" },
            { data: "last_name" },
            {
                data: "date_modified",
                render: function (data, type, row) {
                    return moment(data).format("DD MMMM YYYY HH:mm A");
                }
            },
        ],
        order: ['3', 'desc']
    });




});