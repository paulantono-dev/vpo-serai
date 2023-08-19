from apps import *
from controllers.lov import CLov

@app.route('/api/lov/<type_request>',methods=['POST'])
def api_lov(type_request):
    prmData = request.form
    rs = {'status':False,'msg':'Invalid request !','data':{}}
    if type_request=='mitra':
        rs = CLov().get_ms_mitra(prmData)
    return jsonify(rs)