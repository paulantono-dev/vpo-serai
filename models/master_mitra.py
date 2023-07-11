from common.models_base import BaseModel
class MMasterMitra:
    def __init__(self):
        pass

    def insert_data_master_mitra(self,prmBinding):
        vSql = """
            INSERT INTO 
                serai.ms_mitra(
	                msm_code, 
                    msm_nama_mitra, 
                    msm_alamat_mitra, 
                    msm_telp_mitra, 
                    msm_nama_pemilik, 
                    msm_email_mitra, 
                    msm_npwp, 
                    msm_status_aktif
                )
            VALUES(
                %(kode_mitra)s,
                %(nama_mitra)s,
                %(alamat_mitra)s,
                %(telp_mitra)s,
                %(nama_pemilik)s,
                %(email_mitra)s,
                %(npwp_mitra)s,
                %(status_aktif)s
            )
        """
        return BaseModel().execute_data(vSql,prmBinding)
    
    def update_data_master_mitra(self,prmBinding):
        vSql = """
            UPDATE 
                serai.ms_mitra
            set 
                msm_nama_mitra=%(nama_mitra)s, 
                msm_alamat_mitra=%(alamat_mitra)s, 
                msm_telp_mitra=%(telp_mitra)s, 
                msm_nama_pemilik=%(nama_pemilik)s, 
                msm_email_mitra=%(email_mitra)s, 
                msm_npwp=%(npwp_mitra)s, 
                msm_status_aktif=%(status_aktif)s
            where msm_code = %(kode_mitra)s
        """
        return BaseModel().execute_data(vSql,prmBinding)

    def get_data_master_mitra(self,prmBinding):
        vWhere=""
        fetch='all'
        if prmBinding.get('kode_mitra','')!="":
            vWhere = "where msm_code = %(kode_mitra)s"
            fetch='one'
        vSql = f"""
            SELECT 
                msm_code kode_mitra,  
                msm_nama_mitra nama_Mitra, 
                msm_alamat_mitra alamat_mitra, 
                msm_telp_mitra telp_mitra, 
                msm_nama_pemilik nama_pemilik, 
                msm_email_mitra email_mitra, 
                msm_npwp npwp_mitra, 
                msm_status_aktif status_aktif
            from serai.ms_mitra
            {vWhere}
        """
        return BaseModel().select_data(vSql,prmBinding,fetch=fetch)