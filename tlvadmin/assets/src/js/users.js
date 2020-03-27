$(document).ready(function () {

    // User Module Table
    var table = $('#users-table').DataTable({
        responsive: true,
        autoWidth: false,
        lengthChange: false,
        info: false,
        serverside: true,
        pageLength: 20,
        processing: true,
        language: {
            processing: '<i class="fas fa-spinner fa-spin fa-3x fa-fw"></i><span class="sr-only">Loading...</span> '
        },

        ajax: {
            url: 'http://localhost:8000/api/rest/users/?format=datatables',
        },
        columns: [
            { data: "username" },

            // Permission / Role
            {
                data: null,
                render: function (data, type, row) {
                    if (type == 'display') {

                        if (row.is_superuser == true) {
                            data = "<span class='badge badge-pill badge-warning'>Superuser</span>";
                        } else if (row.is_staff == true) {
                            data = "<span class='badge badge-pill badge-info'>Staff</span>";
                        } else {
                            data = "<span class='badge badge-pill badge-secondary'>Unassign</span>";
                        }

                        if (row.is_superuser == true && row.is_staff == true) {
                            data = "<span class='badge badge-pill badge-info mr-2'>Staff</span>" +
                                "<span class='badge badge-pill badge-warning'>Superuser</span>";
                        }
                    }
                    return data
                }
            },

            { data: "first_name" },
            { data: "last_name" },
            {
                data: "date_modified",
                render: function (data, type, row) {
                    return moment(data).format("DD MMMM YYYY HH:mm A");
                }
            },

            // Actions
            {
                data: "null",
                render: function (data, type, row) {
                    data = "<button class='btn btn-sm btn-secondary btn-action mr-2' data-toggle='modal' data-target='#viewModal'> View </button > " +
                        "<button class='btn btn-sm btn-danger btn-action'> Delete </button>";
                    return data
                },
            }
        ],
        order: ['4', 'desc']
    });

    // Add User
    $("#save").click(function () {
        var data = {};
        data.username = $('#username').val();
        data.password = $('#password').val();

        var success = 3;

        // Validate Username field
        if ($('#username').val() == '') {
            $('#username').addClass('form-error');
            $('#error-username').html('*This item cannot be empty <br>');
            success--;
        } else {
            $('#username').addClass('form-success');
            $('#error-username').html('');
        }

        // Validate Password field
        if ($('#password').val() == '') {
            $('#password').addClass('form-error');
            $('#error-password').html('*This item cannot be empty <br>');
            success--;
        } else {
            $('#password').addClass('form-success');
            $('#error-password').html('');
        }

        // Validate Confirm Password field
        if ($('#confirm_password').val() == '') {
            $('#confirm_password').addClass('form-error');
            $('#error-conf-password').html('*This item cannot be empty <br>');
            success--;
        } else if ($('#confirm_password').val() != $('#password').val()) {

            $('#confirm_password').removeClass('form-success');
            $('#password').removeClass('form-success');

            $('#confirm_password').addClass('form-error');
            $('#password').addClass('form-error');

            $('#confirm_password').val('');
            $('#password').val('');

            $('#error-conf-password').html('*Password mismatch <br>');
        } else {
            $('#confirm_password').addClass('form-success');
            $('#error-conf-password').html('');
        }

        if (success == 3) {
            $.ajax({
                url: 'http://localhost:8000/api/rest/users/',
                type: 'POST',

                data: data,
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
                },
                success: function (result) {
                    Swal.fire({
                        icon: 'success',
                        title: 'Saved!',
                        showConfirmButton: false,
                        timer: 1500
                    });
                    table.ajax.reload();
                },
            }).done(function () {
                $('#userModal').modal('toggle');
            })
        }
    });


    $('#users-table tbody').on('click', 'tr', function () {
        var data = table.row(this).data();
        alert('You clicked on ' + data[0] + '\'s row');
    });

});