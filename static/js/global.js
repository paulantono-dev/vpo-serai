
function loadingBarStart(){
    $('.preloader').css({ 'display':'' });
}
function loadingBarStop(){
    $('.preloader').css({ 'display':'none' });
}
function defaultDatatable(prmId){
    $(`#${prmId}`).DataTable({
        bPaginate: false,
        bInfo: false,
        scrollY: "300px",
        searching:false,
        scrollX:true,
        scrollCollapse:true,
        paging:false,
        autoWidth : true,
        fnInitComplete: function(oSettings) {
            $( window ).resize();
        },
        fnDrawCallback: function(oSettings) {
            $( window ).trigger('resize');
        },
    })
}
function get_value_form_obj(obj,key){
    let value = ''
    if(obj[key]){
        value = obj[key]
    }
    return value
}

function getValuesFormData(id){
    let arrayData = $(`#${id}`).serializeArray()
    let objData = {}
    arrayData.forEach(element => {
        objData[element['name']]=element['value']
    });
    return objData
}
function is_numeric(code){
    listKey = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '-', 'Backspace', 'Tab']
    if (listKey.includes(code.key)) {
        return code.key
    }
    else {
        code.preventDefault()
        // webix.html.stopEvent(code);
    }
    if (code.charCode == '16') {
        code.preventDefault()
        // webix.html.stopEvent(code);
    } else {
        code.preventDefault()
    }

}
function alertConfirmation(prmMessage,prmFunctionSuccess,prmTitle){
    const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
        confirmButton: "btn btn-success",
        cancelButton: "btn btn-danger me-2",
        }
    })
    swalWithBootstrapButtons.fire({
            title: prmMessage,
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Ya, Simpan",
            cancelButtonText: "Tidak",
            reverseButtons: true,
        })
    .then((result) => {
        if (result.isConfirmed) {
            prmFunctionSuccess()
        }
    });
}
function alertReloadCallbackFunction(prmMessage,prmFunction,prmTitle='Success'){
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: "btn btn-success",
            cancelButton: "btn btn-danger me-2",
        },
        buttonsStyling: false,
        });
        swalWithBootstrapButtons.fire(
            prmTitle,
            prmMessage,
            "success"
        ).then(()=>{
            prmFunction()
        })
}

function alertError(prmMessage,prmUrl='/'){
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: "btn btn-success",
            cancelButton: "btn btn-danger me-2",
        },
        buttonsStyling: false,
    });
    swalWithBootstrapButtons.fire(
        "Error !",
        prmMessage,
        "error"
    );
}