from libs import *
from models.index import ModelIndex as m_index
class ControllerIndex:
    def getData():
        session['list_menu']=[
            {'id':'dashboard','value':'Dashboard','href':'/'}
        ]
        getData = m_index.test()
        return getData
