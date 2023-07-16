from common.models_base import BaseModel
class MMasterStock:
    def __init__(self):
        pass

    def get_data_master_stock(self,prmBinding):
        fetch = 'all'
        vWhere = ""
        if prmBinding.get('kode_stock','')!='':
            fetch='one'
            vWhere = " and mss_code = %(kode_stock)s"
        vSql = f"""
            SELECT
                mss_msm_code,
                MSM_NAMA_MITRA, 
                mss_msb_code, 
                MSB_DESC,
                mss_harga_beli, 
                mss_harga_jual, 
                mss_stock, 
                mss_start_date, 
                mss_end_date, 
                mss_status_aktif
            FROM 
                SERAI.MS_STOCK,
                SERAI.MS_BARANG,
                SERAI.MS_MITRA
            WHERE
                MSS_MSM_CODE = MSM_CODE AND
                MSS_MSB_CODE = MSB_CODE
                {vWhere}
        """
        return BaseModel().select_data(vSql,prmBinding,fetch=fetch)

    def insert_data_master_stock(self,prmBinding):
        vSql = """
            INSERT INTO serai.ms_stock
                (
                    mss_msm_code, 
                    mss_msb_code, 
                    mss_harga_beli, 
                    mss_harga_jual, 
                    mss_stock, 
                    mss_start_date, 
                    mss_end_date, 
                    mss_status_aktif, 
                    mss_create_user, 
                    mss_create_date, 
                    mss_update_user, 
                    mss_update_date
                )
            VALUES(
                %(kode_mitra)s, 
                %(kode_barang)s, 
                %(harga_beli)s, 
                %(harga_jual)s, 
                %(stock)s, 
                to_date(%(start_date)s,'DD-MM-YYYY'), 
                to_date(%(end_date)s,'DD-MM-YYYY'), 
                %(status_aktif)s, 
                %(creator)s, 
                now(), 
                %(creator)s, 
                now()
            );
        """
        return BaseModel().execute_data(vSql,prmBinding)
    
    def update_data_master_stock(self,prmBinding):
        vSql = """
            UPDATE SERAI.MS_STOCK
                mss_harga_beli = %(harga_beli)s, 
                mss_harga_jual = %(harga_jual)s, 
                mss_stock = %(stock)s, 
                mss_start_date = to_date(%(start_date)s,'DD-MM-YYYY'), 
                mss_end_date = to_date(%(end_date)s,'DD-MM-YYYY'), 
                mss_status_aktif = %(status_aktif)s, 
                mss_update_user = %(creator)s, 
                mss_update_date = now()
            where
                mss_code = %(kode_stock)s
        """
        return BaseModel().execute_data(vSql,prmBinding)
        
