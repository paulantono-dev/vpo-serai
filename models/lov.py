from common.models_base import BaseModel
class MLov:
    def __init__(self):
        pass
    def lov_get_ms_mitra(self,prmBinding={}):
        vSql = """
            SELECT 
                msm_code kode_mitra,  
                msm_nama_mitra nama_mitra
            from serai.ms_mitra
            where msm_status_aktif = 'Y'
        """
        return BaseModel().select_data(vSql,prmBinding,fetch='all')