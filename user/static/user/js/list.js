$(function(){
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": 'id'},
            {"data": 'username'},
            {"data": 'id'},

        ],
        columnsDefs: [
            {
                targets: [-1],
                class: 'text_center',
                orderable: false,
                render: function(data, type, row){
                    var buttons = '<a href="/user/update/' + row.id + '/" class="btn btn_warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/delete/' + row.id+ '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function(settings, json){
            
        }
    });
});