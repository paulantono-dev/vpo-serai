

function save_data_master_user(prmData){
    const url = "/api/master_user/insert"
    loadingBarStart()
    let sendRequest = $.ajax({
        method: "POST",
        url: url,
        data: prmData,
        success:function(response,status){
            if(!response.status){
                alertError(response.msg)
                return false
            }
            alertReloadCallbackFunction(response.msg,function(){
                window.location.href='/page/master_user/display'
            })
        },
    })
    sendRequest.done(function(data){
        console.log('Done Request...')
        loadingBarStop()
    })
}
function update_data_master_user(prmData){
    const url = "/api/master_user/update"
    loadingBarStart()
    let sendRequest = $.ajax({
        method: "POST",
        url: url,
        data: prmData,
        success:function(response,status){
            if(!response.status){
                alertError(response.msg)
                return false
            }
            alertReloadCallbackFunction(response.msg,function(){
                window.location.href='/page/master_user/display'
            })
        },
    })
    sendRequest.done(function(data){
        console.log('Done Request...')
        loadingBarStop()
    })
}

function save_data_master_barang(prmData){
    const url = "/api/master_barang/insert"
    loadingBarStart()
    let sendRequest = $.ajax({
        method: "POST",
        url: url,
        data: prmData,
        success:function(response,status){
            if(!response.status){
                alertError(response.msg)
                return false
            }
            alertReloadCallbackFunction(response.msg,function(){
                window.location.href='/page/master_barang/display'
            })
        },
    })
    sendRequest.done(function(data){
        console.log('Done Request...')
        loadingBarStop()
    })
}
function update_data_master_barang(prmData){
    const url = "/api/master_barang/update"
    loadingBarStart()
    let sendRequest = $.ajax({
        method: "POST",
        url: url,
        data: prmData,
        success:function(response,status){
            if(!response.status){
                alertError(response.msg)
                return false
            }
            alertReloadCallbackFunction(response.msg,function(){
                window.location.href='/page/master_barang/display'
            })
        },
    })
    sendRequest.done(function(data){
        console.log('Done Request...')
        loadingBarStop()
    })
}
function save_data_master_mitra(prmData){
    const url = "/api/master_mitra/insert"
    loadingBarStart()
    let sendRequest = $.ajax({
        method: "POST",
        url: url,
        data: prmData,
        success:function(response,status){
            if(!response.status){
                alertError(response.msg)
                return false
            }
            alertReloadCallbackFunction(response.msg,function(){
                window.location.href='/page/master_mitra/display'
            })
        },
    })
    sendRequest.done(function(data){
        console.log('Done Request...')
        loadingBarStop()
    })
}
function update_data_master_mitra(prmData){
    const url = "/api/master_mitra/update"
    loadingBarStart()
    let sendRequest = $.ajax({
        method: "POST",
        url: url,
        data: prmData,
        success:function(response,status){
            if(!response.status){
                alertError(response.msg)
                return false
            }
            alertReloadCallbackFunction(response.msg,function(){
                window.location.href='/page/master_mitra/display'
            })
        },
    })
    sendRequest.done(function(data){
        console.log('Done Request...')
        loadingBarStop()
    })
}
function save_data_master_stock(prmData){
    const url = "/api/master_stock/insert"
    loadingBarStart()
    let sendRequest = $.ajax({
        method: "POST",
        url: url,
        data: prmData,
        success:function(response,status){
            if(!response.status){
                alertError(response.msg)
                return false
            }
            alertReloadCallbackFunction(response.msg,function(){
                window.location.href='/page/master_stock/display'
            })
        },
    })
    sendRequest.done(function(data){
        console.log('Done Request...')
        loadingBarStop()
    })
}