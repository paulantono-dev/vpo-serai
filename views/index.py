from apps import *
from controllers.index import CIndex as c_index

@app.route('/',methods=['GET'])
def index():
    getData = c_index.getData()
    return render_template('index/index.html',activeMenu = 'dashboard',data=getData)