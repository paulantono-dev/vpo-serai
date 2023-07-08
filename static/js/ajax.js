

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