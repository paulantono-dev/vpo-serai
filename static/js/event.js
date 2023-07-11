$(document).ready(function(){
    $('#formInsertMasterUser')
        .on('click','button[name="simpan_data"]',function(){
            let formData = getValuesFormData('formInsertMasterUser')
            save_data_master_user(formData)
        })

    $('#formUpdateMasterUser')
        .on('click','input[name="change_password"]',function(){
            let value = $(this).is(':checked');
            $('input[name="old_password"]').val('')
            $('input[name="new_password"]').val('')
            if(value){
                $('#containerPassword').show()
            }
            else{
                $('#containerPassword').hide()
            }
        })
        .on('click','button[name="simpan_data"]',function(){
            let formData = getValuesFormData('formUpdateMasterUser')
            update_data_master_user(formData)
        })

    $('#formInsertMasterBarang')
        .on('click','button[name="simpan_data"]',function(){
            let formData = getValuesFormData('formInsertMasterBarang')
            save_data_master_barang(formData)
        })
    $('#formUpdateMasterBarang')
        .on('click','button[name="simpan_data"]',function(){
            let formData = getValuesFormData('formUpdateMasterBarang')
            update_data_master_barang(formData)
        })
    $('#formInsertMasterMitra')
        .on('click','button[name="simpan_data"]',function(){
            let formData = getValuesFormData('formInsertMasterMitra')
            save_data_master_mitra(formData)
        })
    $('#formUpdateMasterMitra')
        .on('click','button[name="simpan_data"]',function(){
            let formData = getValuesFormData('formUpdateMasterMitra')
            update_data_master_mitra(formData)
        })
})