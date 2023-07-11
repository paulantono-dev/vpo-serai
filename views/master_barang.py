from apps import *
from controllers.master_barang import CMasterBarang


@app.route('/page/master_barang/<page>',methods=['GET'])
def page_msb(page):
    if page == 'display':
        getData = CMasterBarang().get_data_display_page(request.args)
        return render_template('master_barang/display.html',activeMenu='master_barang',result=getData)
    elif page == 'insert':
        return render_template('master_barang/insert.html',activeMenu='master_barang')
    elif page == 'update':
        getData = CMasterBarang().get_data_display_page(request.args)
        return render_template('master_barang/edit.html',activeMenu='master_barang',result=getData)
    else:
        return abort(404)

@app.route('/api/master_barang/<type_request>',methods=['POST'])
def api_msb(type_request):
    prmData = request.form
    rs = {'status':False,'msg':'Invalid request !','data':{}}
    if type_request=='insert':
        rs = CMasterBarang().insert_data(prmData)
    elif type_request=='update':
        rs = CMasterBarang().update_data(prmData)
    return jsonify(rs)
