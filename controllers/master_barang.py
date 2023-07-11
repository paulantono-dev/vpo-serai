from models.master_barang import MMasteBarang
from common.validator import ValidatorInput

class CMasterBarang:
    def __init__(self):
        self.validator = ValidatorInput()
    def get_data_display_page(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            kode_barang = prmData.get('id','')
            prmBinding = {'kode_barang':kode_barang}
            getData = MMasteBarang().get_data_master_barang(prmBinding)
            if not getData['status']:
                rs['msg']='Gagal mendapatkan data barang'
                return rs
            rs['msg']='Berhasil mendapatkan data master barang'
            rs['status']=True
            rs['data']={
                'data_barang':getData['data']
            }
        except Exception as e:
            print(e)
        return rs
    def insert_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            kode_barang = prmData.get('kode_barang','')
            deskripsi_barang = prmData.get('deskripsi_barang','')
            status_aktif = prmData.get('status_aktif','N')

            if kode_barang=="":
                rs['msg']='Kode Barang tidak boleh kosong'
                return rs
            if deskripsi_barang=="":
                rs['msg']="Deskripsi Barang tidak boleh kosong"
                return rs
            if status_aktif=="" or status_aktif not in ('Y','N'):
                rs['msg']="Status Aktif tidak boleh kosong"
                return rs

            

            # Validasi
            validator = [
                self.validator.text_numeric(kode_barang,length=10),
                self.validator.text_numeric(deskripsi_barang,length=100),
                self.validator.text_numeric(status_aktif,length=1),
            ]
            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs
            
            prmBinding = {
                'kode_barang':kode_barang,
                'deskripsi_barang':deskripsi_barang,
                'status_aktif':status_aktif
            }

            # insert data
            insertData = MMasteBarang().insert_data_master_barang(prmBinding)
            if not insertData['status']:
                rs['msg']='Gagal melakukan transaksi insert data master barang'
                return rs
            rs['msg']='Berhasil melakukan insert data'
            rs['status']=True
        except Exception as e:
            print(e)
        return rs
    def update_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            kode_barang = prmData.get('kode_barang','')
            deskripsi_barang = prmData.get('deskripsi_barang','')
            status_aktif = prmData.get('status_aktif','N')

            if kode_barang=="":
                rs['msg']='Kode Barang tidak boleh kosong'
                return rs
            if deskripsi_barang=="":
                rs['msg']="Deskripsi Barang tidak boleh kosong"
                return rs
            if status_aktif=="" or status_aktif not in ('Y','N'):
                rs['msg']="Status Aktif tidak boleh kosong"
                return rs

            

            # Validasi
            validator = [
                self.validator.text_numeric(kode_barang,length=10),
                self.validator.text_numeric(deskripsi_barang,length=100),
                self.validator.text_numeric(status_aktif,length=1),
            ]
            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs
            
            prmBinding = {
                'kode_barang':kode_barang,
                'deskripsi_barang':deskripsi_barang,
                'status_aktif':status_aktif
            }

            # update data
            updateData = MMasteBarang().update_data_master_barang(prmBinding)
            if not updateData['status']:
                rs['msg']='Gagal melakukan transaksi update data master barang'
                return rs
            rs['msg']='Berhasil melakukan update data'
            rs['status']=True
        except Exception as e:
            print(e)
        return rs
    def delete_data(self):
        pass