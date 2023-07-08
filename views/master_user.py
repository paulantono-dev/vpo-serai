from apps import *
from controllers.master_user import CMasterUser


@app.route('/page/master_user/<page>',methods=['GET'])
def page_msu(page):
    if page == 'display':
        getData = CMasterUser().get_data_display_page(request.args)
        return render_template('master_user/display.html',activeMenu='master_user',result=getData)
    elif page == 'insert':
        return render_template('master_user/insert.html',activeMenu='master_user')
    elif page == 'update':
        getData = CMasterUser().get_data_display_page(request.args)
        return render_template('master_user/edit.html',activeMenu='master_user',result=getData)
    else:
        return abort(404)

@app.route('/api/master_user/<type_request>',methods=['POST'])
def api_msu(type_request):
    prmData = request.form
    rs = {'status':False,'msg':'Invalid request !','data':{}}
    if type_request=='insert':
        rs = CMasterUser().insert_data(prmData)
    elif type_request=='delete':
        rs = CMasterUser().delete_data(prmData)
    elif type_request=='update':
        rs = CMasterUser().update_data(prmData)
    return jsonify(rs)
