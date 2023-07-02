from common.models_base import BaseModel
class MMasteUser:
    def __init__(self):
        pass
    def insert_data_master_user(self,prmBinding):
        vSql = """
            INSERT INTO serai.ms_users(
                msu_username,
                msu_password,
                msu_status_aktif
            )
            VALUES(
                %(username)s,
                %(password)s,
                %(status_aktif)s
            )
        """
        return BaseModel().execute_data(vSql,prmBinding)
    def update_data_master_user(self,prmBinding):
        querySet = "msu_status_aktif = %(status_aktif)s "
        if prmBinding.get('new_password','')!="":
            querySet+=", msu_password = %(new_password)s"
        vSql = f"""
            UPDATE serai.ms_users 
            SET
                {querySet}
            where
                msu_username = %(username)s
        """
        return BaseModel().execute_data(vSql,prmBinding)
    def delete_data_master_user(pself,prmBinding):
        vSql = """
            DELETE FROM serai.ms_users where msu_username = %(username)s
        """
        return BaseModel().execute_data(vSql,prmBinding)
    def get_data_master_user(self,prmBinding):
        vSql = """
            SELECT 
                msu_username username,
                msu_status_aktif status_aktif 
            from serai.ms_users
        """
        return BaseModel().select_data(vSql,prmBinding)
    
    def check_is_password_valid(self,prmBinding):
        vSql = """
            select (case when count(msu_username)>0 then 'Y' else 'N' end) is_exist
            from serai.ms_users where upper(msu_username) = upper(%(username)s) and msu_password = %(old_password)s
        """
        return BaseModel().select_data(vSql,prmBinding,fetch='one')
    
    def check_is_username_exist(self,prmBinding):
        vSql = """
            select (case when count(msu_username)>0 then 'Y' else 'N' end) is_exist
            from serai.ms_users where upper(msu_username) = upper(%(username))
        """
        return BaseModel().select_data(vSql,prmBinding,fetch='one')