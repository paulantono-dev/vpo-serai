from apps import *
from controllers.master_mitra import CMasterMitra


@app.route('/page/master_mitra/<page>',methods=['GET'])
def page_msm(page):
    if page == 'display':
        getData = CMasterMitra().get_data_display_page(request.args)
        return render_template('master_mitra/display.html',activeMenu='master_mitra',result=getData)
    elif page == 'insert':
        return render_template('master_mitra/insert.html',activeMenu='master_mitra')
    elif page == 'update':
        getData = CMasterMitra().get_data_display_page(request.args)
        return render_template('master_mitra/edit.html',activeMenu='master_mitra',result=getData)
    else:
        return abort(404)

@app.route('/api/master_mitra/<type_request>',methods=['POST'])
def api_msm(type_request):
    prmData = request.form
    rs = {'status':False,'msg':'Invalid request !','data':{}}
    if type_request=='insert':
        rs = CMasterMitra().insert_data(prmData)
    elif type_request=='update':
        rs = CMasterMitra().update_data(prmData)
    return jsonify(rs)
