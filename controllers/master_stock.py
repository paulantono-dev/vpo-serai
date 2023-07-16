from models.master_stock import MMasterStock
from models.views import MViews
from common.validator import ValidatorInput
from libs import *

class CMasterStock:
    def __init__(self):
        self.__validator = ValidatorInput()
    
    def get_data_display_page(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            kode_stock = prmData.get('id','')
            prmBinding = {'kode_stock':kode_stock}
            getData = MMasterStock().get_data_master_stock(prmBinding)
            if not getData['status']:
                rs['msg']='Gagal mendapatkan data stock'
                return rs
            rs['msg']='Berhasil mendapatkan data master stock'
            rs['status']=True
            rs['data']={
                'data_mitra':getData['data']
            }
        except Exception as e:
            print(e)
        return rs
    def get_data_display_page_insert(self):
        return
    def insert_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            kode_mitra = prmData.get('kode_mitra','')
            kode_barang = prmData.get('kode_barang','')
            harga_beli = prmData.get('harga_beli','')
            harga_jual = prmData.get('harga_jual','')
            stock = prmData.get('stock','')
            start_date = prmData.get('start_date','')
            end_date = prmData.get('end_date','')
            creator = session.get('user_login','')

            for value in (kode_mitra,kode_barang,harga_beli,harga_jual,stock,start_date,end_date):
                if value=="":
                    rs['msg']='Harap mengisi value dengan lengkap'
                    return rs
            
            # Validasi
            validator = [
                self.validator.text_numeric(kode_mitra,length=10),
                self.validator.text_numeric(kode_barang,length=10),
                self.validator.numeric(harga_beli),
                self.validator.numeric(harga_jual),
                self.validator.numeric(stock),
                self.validator.datetime(start_date),
                self.validator.datetime(end_date)
            ]

            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs

            prmBinding = {
                'kode_mitra':kode_mitra,
                'kode_barang':kode_barang,
                'harga_beli':harga_beli,
                'harga_jual':harga_jual,
                'stock':stock,
                'start_date':start_date,
                'end_date':end_date,
                'creator':creator
            }

            insertData = MMasterStock().insert_data_master_stock(prmBinding)
            if not insertData['status']:
                rs['msg']='Gagal melakukan insert data master stock'
                return rs
            rs['msg']='Berhasil melakukan insert data master stock'
            rs['status']=True
        except Exception as e:
            print(e)
        return rs
    def update_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            kode_stock = prmData.get('kode_stock','')
            kode_mitra = prmData.get('kode_mitra','')
            kode_barang = prmData.get('kode_barang','')
            harga_beli = prmData.get('harga_beli','')
            harga_jual = prmData.get('harga_jual','')
            stock = prmData.get('stock','')
            start_date = prmData.get('start_date','')
            end_date = prmData.get('end_date','')
            creator = session.get('user_login','')

            for value in (kode_mitra,kode_barang,harga_beli,harga_jual,stock,start_date,end_date):
                if value=="":
                    rs['msg']='Harap mengisi value dengan lengkap'
                    return rs
            
            # Validasi
            validator = [
                self.validator.numeric(kode_stock),
                self.validator.text_numeric(kode_mitra,length=10),
                self.validator.text_numeric(kode_barang,length=10),
                self.validator.numeric(harga_beli),
                self.validator.numeric(harga_jual),
                self.validator.numeric(stock),
                self.validator.datetime(start_date),
                self.validator.datetime(end_date)
            ]

            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs

            prmBinding = {
                'kode_stock':kode_stock,
                'kode_mitra':kode_mitra,
                'kode_barang':kode_barang,
                'harga_beli':harga_beli,
                'harga_jual':harga_jual,
                'stock':stock,
                'start_date':start_date,
                'end_date':end_date,
                'creator':creator
            }

            updateData = MMasterStock().update_data_master_stock(prmBinding)
            if not updateData['status']:
                rs['msg']='Gagal melakukan update data master stock'
                return rs
            rs['msg']='Berhasil melakukan update data master stock'
            rs['status']=True
        except Exception as e:
            print(e)
        return rs 