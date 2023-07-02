from models.master_user import MMasteUser
from common.validator import ValidatorInput
from common import utils
class CMasterUser:
    def __init__(self):
        self.validator = ValidatorInput()
    def get_data(self):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            getData = MMasteUser().get_data_master_user({})
            print(getData)
            if not getData['status']:
                rs['msg']='Gagal mendapatkan data user'
                return rs
            rs['msg']='Berhasil mendapatkan data master user'
            rs['status']=True
            rs['data']={
                'data_user':getData['data']
            }
        except Exception as e:
            print(e)
        return rs
    def insert_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            username = prmData.get('username')
            password = prmData.get('password')
            statusaktif = prmData.get('status_aktif')

            # Validasi
            validator = [
                self.validator.text_numeric(username,length=10),
                self.validator.text_numeric(password,length=20),
                self.validator.text_numeric(statusaktif,length=1),

            ]
            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs
                
            md5password = utils.generateMd5(password)
                
            
            prmBinding = {
                'username':username,
                'password':md5password,
                'status_aktif':statusaktif
            }

            # check is exist
            checkIsExist = MMasteUser().check_is_username_exist(prmBinding)
            if not checkIsExist['status']:
                rs['msg']='Gagal mendapatkan ketersediaan username'
                return rs
            if checkIsExist['data']['is_exist']=='Y':
                rs['msg']='Username telah digunakan, harap gunakan username lain'
                return rs
            
            insertData = MMasteUser().insert_data_master_user(prmBinding)
            if not insertData['status']:
                rs['msg']='Gagal melakukan insert data master user'
                return rs
            rs['msg']='Berhasil melakukan insert data master user'
            rs['status']=True
        except Exception as e:
            print(e)
        return rs
    def update_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            username = prmData.get('username','')
            old_password = prmData.get('old_password','')
            new_password = prmData.get('new_password','')
            statusaktif = prmData.get('status_aktif','')

            # Validasi
            validator = [
                self.validator.text_numeric(username,length=10),
                self.validator.text_numeric(old_password,length=20),
                self.validator.text_numeric(new_password,length=20),
                self.validator.text_numeric(statusaktif,length=1),
            ]
            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs
            
            old_md5password = utils.generateMd5(old_password)
            new_md5password = utils.generateMd5(new_password)

            prmBinding = {
                'username':username,
                'password':new_md5password,
                'old_password':old_md5password,
                'status_aktif':statusaktif
            }

            # check is exist
            checkIsExist = MMasteUser().check_is_password_valid(prmBinding)
            if not checkIsExist['status']:
                rs['msg']='Gagal mendapatkan ketersediaan username'
                return rs
            if checkIsExist['data']['is_exist']=='N':
                rs['msg']='Password tidak valid ! Harap periksa kembali password lama anda'
                return rs

            insertData = MMasteUser().update_data_master_user(prmBinding)
            if not insertData['status']:
                rs['msg']='Gagal melakukan update data master user'
                return rs
            rs['msg']='Berhasil melakukan update data master user'
            rs['status']=True
        except Exception as e:
            print(e)
        return rs
    def delete_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            username = prmData.get('username','')

            # Validasi
            validator = [
                self.validator.text_numeric(username,length=10),
            ]
            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs
            prmBinding = {
                'username':username,
            }
            insertData = MMasteUser().delete_data_master_user(prmBinding)
            if not insertData['status']:
                rs['msg']='Gagal melakukan delete data master user'
                return rs
            rs['msg']='Berhasil melakukan delete data master user'
            rs['status']=True
        except Exception as e:
            print(e)
        return rs