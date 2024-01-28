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
    def lov_get_ms_barang(self,prmBinding={}):
        vSql = """
            SELECT 
                msb_code kode_barang,
                msb_desc nama_barang
            FROM serai.ms_barang
            WHERE msb_status_aktif = 'Y'
        """
        return BaseModel().select_data(vSql,prmBinding,fetch='all')