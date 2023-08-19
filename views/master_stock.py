from apps import *
from controllers.master_stock import CMasterStock


@app.route('/page/master_stock/<page>',methods=['GET'])
def page_mss(page):
    if page == 'display':
        getData = CMasterStock().get_data_display_page(request.args)
        return render_template('master_stock/display.html',activeMenu='master_stock',result=getData)
    elif page == 'insert':
        getData = CMasterStock().get_data_display_page_insert()
        return render_template('master_stock/insert.html',activeMenu='master_stock',result=getData)
    elif page == 'update':
        getData = CMasterStock().get_data_display_page(request.args)
        return render_template('master_stock/edit.html',activeMenu='master_stock',result=getData)
    else:
        return abort(404)

@app.route('/api/master_stock/<type_request>',methods=['POST'])
def api_mss(type_request):
    prmData = request.form
    rs = {'status':False,'msg':'Invalid request !','data':{}}
    if type_request=='insert':
        rs = CMasterStock().insert_data(prmData)
    elif type_request=='update':
        rs = CMasterStock().update_data(prmData)
    return jsonify(rs)
