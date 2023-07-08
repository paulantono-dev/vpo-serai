from libs import *
from models.index import ModelIndex as m_index
class CIndex:
    def getData():
        session['list_menu']=[
            {'id':'dashboard','value':'Dashboard','href':'/'},
            {'id':'master_user','value':'Master User','href':'/page/master_user/display'},
            {'id':'master_barang','value':'Master Barang','href':'/master_barang'},
            {'id':'master_logistik','value':'Master Logistik','href':'/master_logistik'},
            {'id':'master_stock','value':'Master Stock','href':'/master_stock'},
        ]
        getData = m_index.test()
        print(getData)
        return getData
