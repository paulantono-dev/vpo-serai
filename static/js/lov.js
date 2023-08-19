function lov_mitra(){
    resetModal()
    let idTable = 'lov_mitra'
    const objectData = {
        id:idTable,
        columns_header:[
            {'id':'kode_mitra','header':'Kode Mitra'},
            {'id':'nama_mitra','header':'Nama Mitra'},
        ],
    }
    const stringHtml = CustomDatatable(objectData)
    $('.modal-body').html(stringHtml)
    let table = defaultDatatable(idTable,{
        columns:[
            {data:'kode_mitra'},
            {data:'nama_mitra'},
        ],
        ajax: {
            url: '/api/lov/mitra',
            type: 'POST'
        },
        select:true
        
    })
    table.on('select',function(e, dt, type, indexes){
        let rowData = table.rows(indexes).data().toArray()[0];
        $("input[name='kode_mitra']").val(rowData['kode_mitra'])
        $("input[name='nama_mitra']").val(rowData['nama_mitra'])
        $('.modal').modal("hide")
    })
    $('.modal').modal("show")
}