from apps import *
from views.index import *
from views.master_user import *
from views.master_barang import *
from views.master_mitra import *
from views.master_stock import *
from views.lov import *
# penambahan middle session untuk logout ketika tidak ada activitas user =====
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)


''' must be have this !!!! '''
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = ENV['SECRET_KEY']


''' must be have this !!!! '''
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run('localhost',port=8080,debug=True)