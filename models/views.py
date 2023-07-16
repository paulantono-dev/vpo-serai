from common.models_base import BaseModel

class MViews:
    def get_ms_role(self):
        vSql="""
            SELECT 
                msru_code as id, 
                msru_desc as value
            FROM serai.ms_role_user
            where msru_status_aktif = 'Y'
        """
        return BaseModel().select_data(vSql,{})

    def get_ms_role_mitra(self):
        vSql = """
            SELECT 
                mtm_code as id, 
                mtm_desc as value
            FROM 
                serai.ms_tipe_mitra
            where 
                mtm_status_aktif = 'Y'
        """
        return BaseModel().select_data(vSql,{})