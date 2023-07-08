from common.models_base import BaseModel
class MMasteUser:
    def __init__(self):
        pass
    def insert_data_master_user(self,prmBinding):
        vSql = """
            INSERT INTO serai.ms_users(
                msu_username,
                msu_password,
                msu_status_aktif,
                msu_id
            )
            VALUES(
                %(username)s,
                %(password)s,
                %(status_aktif)s,
                %(username_id)s
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
                msu_id = %(username_id)s
        """
        return BaseModel().execute_data(vSql,prmBinding)
    def delete_data_master_user(pself,prmBinding):
        vSql = """
            DELETE FROM serai.ms_users where msu_id = %(username_id)s
        """
        return BaseModel().execute_data(vSql,prmBinding)
    def get_data_master_user(self,prmBinding):
        vWhere=""
        fetch='all'
        if prmBinding.get('username_id','')!="":
            vWhere = "where msu_id = %(username_id)s"
            fetch='one'
        vSql = f"""
            SELECT 
                msu_username username,
                msu_status_aktif status_aktif,
                msu_id user_id
            from serai.ms_users
            {vWhere}
        """
        return BaseModel().select_data(vSql,prmBinding,fetch=fetch)
    
    def check_is_password_valid(self,prmBinding):
        vWhere = ""
        if prmBinding.get('change_password','')=='Y':
            vWhere="and msu_password = %(old_password)s"
        vSql = f"""
            select (case when count(msu_id)>0 then 'Y' else 'N' end) is_exist
            from serai.ms_users where upper(msu_id) = upper(%(username_id)s)
            {vWhere}
        """
        return BaseModel().select_data(vSql,prmBinding,fetch='one')
    
    def check_is_username_exist(self,prmBinding):
        vSql = """
            select (case when count(msu_id)>0 then 'Y' else 'N' end) is_exist
            from serai.ms_users where upper(msu_id) = upper(%(username_id)s)
        """
        return BaseModel().select_data(vSql,prmBinding,fetch='one')