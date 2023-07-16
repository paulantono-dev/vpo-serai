from models.master_mitra import MMasterMitra
from models.views import MViews
from common.validator import ValidatorInput

class CMasterMitra:
    def __init__(self):
        self.validator = ValidatorInput()

    def get_data_display_insert_page(self):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            getRoleMasterMitra = MViews().get_ms_role_mitra()
            if not getRoleMasterMitra['status']:
                rs['msg']='Gagal mendapatkan data master role mitra'
                return rs
            rs['data']={
                'data_role_mitra':getRoleMasterMitra['data']
            }
            rs['status']=True
            rs['msg']='Berhasil mendapatkan data'
        except Exception as e:
            print(e)
        return rs

    def get_data_display_page(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            kode_mitra = prmData.get('id','')
            prmBinding = {'kode_mitra':kode_mitra}
            getData = MMasterMitra().get_data_master_mitra(prmBinding)
            getMsRoleMitra = MViews().get_ms_role_mitra()
            print(getMsRoleMitra)
            if not getData['status']:
                rs['msg']='Gagal mendapatkan data mitra'
                return rs
            rs['msg']='Berhasil mendapatkan data master mitra'
            rs['status']=True
            rs['data']={
                'data_mitra':getData['data'],
                'data_role_mitra':getMsRoleMitra['data']
            }
        except Exception as e:
            print(e)
        return rs
    def insert_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            kode_mitra = prmData.get('kode_mitra','')
            nama_mitra = prmData.get('nama_mitra','')
            telp_mitra = prmData.get('telp','')
            npwp_mitra = prmData.get('npwp','')
            status_aktif = prmData.get('status_aktif','N')
            alamat_mitra = prmData.get('alamat','')
            email_mitra = prmData.get('email','')
            nama_pemilik = prmData.get('nama_pemilik','')
            role_mitra = prmData.get('role_mitra','')


            if kode_mitra=="":
                rs['msg']='Kode Mitra tidak boleh kosong'
                return rs
            if nama_mitra=="":
                rs['msg']="Nama Mitra tidak boleh kosong"
                return rs
            if telp_mitra=="":
                rs['msg']="Telp Mitra tidak boleh kosong"
                return rs
            if alamat_mitra=="":
                rs['msg']="Alamat Mitra tidak boleh kosong"
                return rs
            if nama_pemilik=="":
                rs['msg']="Nama Pemilik tidak boleh kosong"
                return rs
            if status_aktif=="" or status_aktif not in ('Y','N'):
                rs['msg']="Status Aktif tidak boleh kosong"
                return rs
            if role_mitra=="":
                rs['msg']='Role mitra tidak boleh kosong'
                return rs

            

            # Validasi
            validator = [
                self.validator.text_numeric(kode_mitra,length=10),
                self.validator.text_numeric(nama_mitra,length=100),
                self.validator.text_numeric(alamat_mitra,allowed_character=['-','/'],length=500),
                self.validator.numeric(telp_mitra,length=20),
                self.validator.text_numeric(npwp_mitra,allowed_character=['.','-'],length=30),
                self.validator.text_numeric(nama_pemilik,allowed_character=["'"],length=100),
                self.validator.text_numeric(status_aktif,length=1),
                self.validator.email(email_mitra,length=200),
                self.validator.text_numeric(role_mitra,length=10),
            ]


            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs
            
            prmBinding = {
                'kode_mitra':kode_mitra,
                'nama_mitra':nama_mitra,
                'alamat_mitra':alamat_mitra,
                'telp_mitra':telp_mitra,
                'npwp_mitra':npwp_mitra,
                'nama_pemilik':nama_pemilik,
                'status_aktif':status_aktif,
                'email_mitra':email_mitra,
                'role_mitra':role_mitra
            }

            # insert data
            insertData = MMasterMitra().insert_data_master_mitra(prmBinding)
            if not insertData['status']:
                rs['msg']='Gagal melakukan transaksi insert data master mitra'
                return rs
            rs['msg']='Berhasil melakukan insert data'
            rs['status']=True
        except Exception as e:
            print(e)
        return rs
    def update_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            kode_mitra = prmData.get('kode_mitra','')
            nama_mitra = prmData.get('nama_mitra','')
            telp_mitra = prmData.get('telp','')
            npwp_mitra = prmData.get('npwp','')
            status_aktif = prmData.get('status_aktif','N')
            alamat_mitra = prmData.get('alamat','')
            email_mitra = prmData.get('email','')
            nama_pemilik = prmData.get('nama_pemilik','')
            role_mitra = prmData.get('role_mitra','')
            


            if kode_mitra=="":
                rs['msg']='Kode Mitra tidak boleh kosong'
                return rs
            if nama_mitra=="":
                rs['msg']="Nama Mitra tidak boleh kosong"
                return rs
            if telp_mitra=="":
                rs['msg']="Telp Mitra tidak boleh kosong"
                return rs
            if alamat_mitra=="":
                rs['msg']="Alamat Mitra tidak boleh kosong"
                return rs
            if nama_pemilik=="":
                rs['msg']="Nama Pemilik tidak boleh kosong"
                return rs
            if status_aktif=="" or status_aktif not in ('Y','N'):
                rs['msg']="Status Aktif tidak boleh kosong"
                return rs
            if role_mitra=="":
                rs['msg']='Role mitra tidak boleh kosong'
                return rs

            

            # Validasi
            validator = [
                self.validator.text_numeric(kode_mitra,length=10),
                self.validator.text_numeric(nama_mitra,length=100),
                self.validator.text_numeric(alamat_mitra,allowed_character=['-','/'],length=500),
                self.validator.numeric(telp_mitra,length=20),
                self.validator.text_numeric(npwp_mitra,allowed_character=['.','-'],length=30),
                self.validator.text_numeric(nama_pemilik,allowed_character=["'"],length=100),
                self.validator.text_numeric(status_aktif,length=1),
                self.validator.text_numeric(role_mitra,length=10),
                self.validator.email(email_mitra,length=200),
            ]


            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs
            
            prmBinding = {
                'kode_mitra':kode_mitra,
                'nama_mitra':nama_mitra,
                'alamat_mitra':alamat_mitra,
                'telp_mitra':telp_mitra,
                'npwp_mitra':npwp_mitra,
                'nama_pemilik':nama_pemilik,
                'status_aktif':status_aktif,
                'email_mitra':email_mitra,
                'role_mitra':role_mitra
            }

            # update data
            updateData = MMasterMitra().update_data_master_mitra(prmBinding)
            if not updateData['status']:
                rs['msg']='Gagal melakukan transaksi update data master mitra'
                return rs
            rs['msg']='Berhasil melakukan update data'
            rs['status']=True
        except Exception as e:
            print(e)
        return rs