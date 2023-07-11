from common.models_base import BaseModel
class MMasteBarang:
    def __init__(self):
        pass

    def insert_data_master_barang(self,prmBinding):
        vSql = """
            INSERT INTO serai.ms_barang(
                msb_code,
                msb_desc,
                msb_status_aktif
            )
            VALUES(
                %(kode_barang)s,
                %(deskripsi_barang)s,
                %(status_aktif)s
            )
        """
        return BaseModel().execute_data(vSql,prmBinding)
    
    def update_data_master_barang(self,prmBinding):
        vSql = """
            UPDATE 
                serai.ms_barang 
            set 
                msb_desc = %(deskripsi_barang)s,
                msb_status_aktif = %(status_aktif)s
            where msb_code = %(kode_barang)s
        """
        return BaseModel().execute_data(vSql,prmBinding)

    def get_data_master_barang(self,prmBinding):
        vWhere=""
        fetch='all'
        if prmBinding.get('kode_barang','')!="":
            vWhere = "where msb_code = %(kode_barang)s"
            fetch='one'
        vSql = f"""
            SELECT 
                msb_code kode_barang,
                msb_status_aktif status_aktif,
                msb_desc deskripsi_barang
            from serai.ms_barang
            {vWhere}
        """
        return BaseModel().select_data(vSql,prmBinding,fetch=fetch)