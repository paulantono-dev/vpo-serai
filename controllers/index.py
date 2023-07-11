from libs import *
from models.index import ModelIndex as m_index
class CIndex:
    def getData():
        session['list_menu']=[
            {'id':'dashboard','value':'Dashboard','href':'/','icons':'ni ni-tv-2 text-primary'},
            {'id':'-','value':'Master Pages'},
            {'id':'master_user','value':'Master User','href':'/page/master_user/display','icons':'ni ni-single-02 text-danger'},
            {'id':'master_barang','value':'Master Barang','href':'/page/master_barang/display','icons':'ni ni-app text-success'},
            {'id':'master_mitra','value':'Master Mitra','href':'/page/master_mitra/display','icons':'ni ni-badge text-info'},
            # {'id':'master_logistik','value':'Master Logistik','href':'/master_logistik'},
            # {'id':'master_stock','value':'Master Stock','href':'/master_stock'},
        ]
        getData = m_index.test()
        return getData
