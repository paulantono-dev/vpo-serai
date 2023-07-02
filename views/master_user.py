from apps import *
from controllers.master_user import CMasterUser

@app.route('/master_user',methods=['GET'])
def msu():
    getData = CMasterUser().get_data()
    print(getData)
    return render_template('index/index.html',data=getData)
@app.route('/master_user/insert',methods=['POST'])
def msu_insert():
    rs = CMasterUser().insert_data(request.form)
    return jsonify(rs)
@app.route('/master_user/update',methods=['POST'])
def msu_update():
    rs = CMasterUser().insert_data(request.form)
    return jsonify(rs)
@app.route('/master_user/delete',methods=['POST'])
def msu_delete():
    rs = CMasterUser().delete_data(request.form)
    return jsonify(rs)