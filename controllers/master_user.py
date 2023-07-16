from models.master_user import MMasteUser
from models.views import MViews
from common.validator import ValidatorInput
from common import utils
class CMasterUser:
    def __init__(self):
        self.validator = ValidatorInput()

    def get_data_display_insert_page(self):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            getRoleMasterUser = MViews().get_ms_role()
            if not getRoleMasterUser['status']:
                rs['msg']='Gagal mendapatkan data master role user'
                return rs
            rs['data']={
                'data_ms_role':getRoleMasterUser['data']
            }
            rs['status']=True
            rs['msg']='Berhasil mendapatkan data'
        except Exception as e:
            print(e)
        return rs


    def get_data_display_page(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            username_id = prmData.get('id','')
            prmBinding = {'username_id':username_id}
            getData = MMasteUser().get_data_master_user(prmBinding)
            if not getData['status']:
                rs['msg']='Gagal mendapatkan data user'
                return rs
            getRoleMasterUser = MViews().get_ms_role()
            rs['msg']='Berhasil mendapatkan data master user'
            rs['status']=True
            rs['data']={
                'data_user':getData['data'],
                'data_ms_role':getRoleMasterUser['data']
            }
        except Exception as e:
            print(e)
        return rs
    def insert_data(self,prmData):
        rs = {'status':False,'msg':'Terdapat kesalahan pada saat transaksi data','data':{}}
        try:
            username = prmData.get('username')
            password = prmData.get('password')
            statusaktif = prmData.get('status_aktif','N')
            role_user = prmData.get('role_user','')

            if username=="":
                rs['msg']='Username tidak boleh kosong'
                return rs
            if password=="":
                rs['msg']='Password tidak boleh kosong'
                return rs
            if statusaktif=="":
                rs['msg']='Status Aktif tidak boleh kosong'
                return rs
            if role_user=="":
                rs['msg']='Role user tidak boleh kosong'
                return rs

            # Validasi
            validator = [
                self.validator.text_numeric(username,length=10),
                self.validator.text_numeric(password,length=20),
                self.validator.text_numeric(statusaktif,length=1),
                self.validator.text_numeric(role_user,length=10),

            ]
            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs
                
            md5password = utils.generateMd5(password)
            if not md5password['status']:
                rs['msg']='Gagal melakukan encrypt data password'
                return rs
            md5password=md5password['md5']

            usernameId = utils.generateMd5(username)
            if not usernameId['status']:
                rs['msg']='Gagal melakukan encrypt data username'
                return rs
            usernameId=usernameId['md5']
                
            
            prmBinding = {
                'username':username,
                'password':md5password,
                'status_aktif':statusaktif,
                'username_id':usernameId,
                'role_user':role_user
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
            change_password = prmData.get('change_password','N')
            old_password = prmData.get('old_password','')
            new_password = prmData.get('new_password','')
            statusaktif = prmData.get('status_aktif','N')
            role_user = prmData.get('role_user','')

            if username=="":
                rs['msg']='Username tidak boleh kosong'
                return rs
            
            if change_password=="Y":
                if old_password=="":
                    rs['msg']='Password lama tidak boleh kosong'
                    return rs
                if new_password=="":
                    rs['msg']='Password baru tidak boleh kosong'
                    return rs
            if statusaktif=="":
                rs['msg']='Status Aktif tidak boleh kosong'
                return rs
            
            if role_user=="":
                rs['msg']='Role user tidak boleh kosong'
                return rs
            # Validasi
            validator = [
                self.validator.text_numeric(username,length=10),
                self.validator.text_numeric(old_password,length=20),
                self.validator.text_numeric(new_password,length=20),
                self.validator.text_numeric(statusaktif,length=1),
                self.validator.text_numeric(role_user,length=10),
            ]
            for validStatus in validator:
                if not validStatus['status']:
                    value = validStatus['value']
                    value_not_valid = validStatus['not_valid_value']
                    rs['msg']=f'Value tidak valid <b>{value}</b> ! <br> Karakter <b>{value_not_valid}</b>'
                    return rs
            
            old_md5password = utils.generateMd5(old_password)
            new_md5password = utils.generateMd5(new_password)
            usernameId = utils.generateMd5(username)

            if not old_md5password['status']:
                rs['msg']='Gagal melakukan encrypt data password lama'
                return rs
            old_md5password=old_md5password['md5']
            if not new_md5password['status']:
                rs['msg']='Gagal melakukan encrypt data password baru'
                return rs
            new_md5password=new_md5password['md5']

            usernameId = utils.generateMd5(username)
            if not usernameId['status']:
                rs['msg']='Gagal melakukan encrypt data username'
                return rs
            usernameId=usernameId['md5']

            prmBinding = {
                'username':username,
                'new_password':new_md5password,
                'old_password':old_md5password,
                'status_aktif':statusaktif,
                'username_id':usernameId,
                'change_password':change_password,
                'role_user':role_user
            }
            # check is exist
            checkIsExist = MMasteUser().check_is_password_valid(prmBinding)
            if not checkIsExist['status']:
                rs['msg']='Gagal mendapatkan ketersediaan username'
                return rs
            if checkIsExist['data']['is_exist']=='N':
                rs['msg']='Password / Username tidak valid ! Harap periksa kembali username / password lama anda'
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
                
            usernameId = utils.generateMd5(username)
            if not usernameId['status']:
                rs['msg']='Gagal melakukan encrypt data username'
                return rs
            usernameId=usernameId['md5']


            prmBinding = {
                'username_id':usernameId,
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
    