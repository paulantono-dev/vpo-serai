from models.lov import MLov
from models.views import MViews
from common.validator import ValidatorInput

class CLov:
    def __init__(self):
        self.validator = ValidatorInput()
    def get_ms_mitra(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            rs = MLov().lov_get_ms_mitra({})
        except Exception as e:
            print(e)
        return rs
