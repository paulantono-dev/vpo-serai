import time
from common.logger import Logger
from common.connectios import Connection

class BaseResponse():
    def __init__(self):
        self.__code = {
            '00':{'status':True,'msg':'Berhasil mendapatkan data'},
            '01':{'status':False,'msg':'Terdapat kesalahan pada transaksi data'},
            '02':{'status':False,'msg':'Terdapat kesalahan pada model data'},
            '03':{'status':False,'msg':'Terdapat kesalahan pada view data'}
        }
    def get_response(self,code,data=[]):
        result = self.__code.get(code)
        result['data']=data
        return self.__code.get(code)
        
class BaseModel():
    def __init__(self):
        self._conn = None
        self._success_status = {}
        self._success_status_execute = {}
        self._failed_status = {}
        self._failed_status_execute = {}
        self._status = {}
        self._logger = Logger()
        # self._logger.createLogger()
        self.__declare_conn()
    
    def __declare_conn(self):
        self._conn = Connection('SERAI')
        # self.__set_lc()
        self._success_status = {'status':True,'msg':'Berhasil mendapatkan data','data':[]}
        self._success_status_execute = {'status':True,'msg':'Berhasil eksekusi data','data':[]}
        self._failed_status = {'status':False,'msg':'Gagal mendapatkan data','data':[]}
        self._failed_status_execute = {'status':False,'msg':'Gagal eksekusi data','data':[]}
        self._status = {}
    def __set_lc(self):
        self._status = self._failed_status
        try:
            vSql = """

                set lc_time = 'id_ID';

            """
            status,data = self._conn.selectDataDict(vSql,{})
            if not status:
                return self._failed_status
            self._status = self._success_status
            self._status['data']=data[0]
        except Exception as e:
            print(e)
        return self._status
    def conn_commit(self):
        self._conn.forCommit()
        self._conn.delete()
    def conn_open(self):
        self._conn.delete()
        del self._conn
        self.__declare_conn()
    def conn_close(self):
        self._conn.delete()
    def select_data_pagination(self,prmSql,page=1,prmBinding={},fetch='all',prmLimit=10):
        rs = self._failed_status
        try:
            status,result = self._conn.selectPaginationDict(page,prmSql,prmBinding,prmLimit)
            self._logger.info(application='',prm_query=prmBinding,prm_sql=prmSql,result_status=status)
            if not status:
                return rs
            if fetch=='one':
                if len(result)<1:
                    result={}
                else:
                    result=result[0]
            rs = self._success_status
            rs['status']=True
            rs['msg']='Berhasil mendapatkan data'
            rs['data']=result
        except Exception as e:
            print(e)
            rs['msg']=e
        self._conn.delete()
        return rs
    def select_data_limit_offset(self,prmSql,prmBinding={},fetch='all',limit=10,offset=0):
        rs = self._failed_status
        try:
            vSqlTemp = """SELECT count(aaa.*) from ("""+prmSql+""") aaa """
            vResult = self._conn.selectData(vSqlTemp, prmBinding, 'one')
            prmSql +="limit %(limit)s offset %(start)s"
            status,result = self._conn.selectDataDict(prmSql,prmBinding)
            self._logger.info(application='',prm_query=prmBinding,prm_sql=prmSql,result_status=status)
            if not status:
                return rs
            if fetch=='one':
                if len(result)<1:
                    result={}
                else:
                    result=result[0]
            rs = self._success_status
            rs['status']=True
            rs['msg']='Berhasil mendapatkan data'
            rs['data']=result
            rs['total']=int(vResult[1][0])
        except Exception as e:
            print(e)
            rs['msg']=e
        self._conn.delete()
        return rs
    def select_data(self,prmSql,prmBinding={},fetch='all'):
        rs = self._failed_status
        try:
            status,result = self._conn.selectDataDict(prmSql,prmBinding)
            self._logger.info(application='',prm_query=prmBinding,prm_sql=prmSql,result_status=status)
            if not status:
                return rs
            if fetch=='one':
                if len(result)<1:
                    result={}
                else:
                    result=result[0]
            rs = self._success_status
            rs['status']=True
            rs['msg']='Berhasil mendapatkan data'
            rs['data']=result
            
        except Exception as e:
            print(e)
            rs['msg']=e
        self._conn.delete()
        return rs
    
    def execute_data(self,prmSql,prmBinding={}):
        rs = self._failed_status_execute
        try:
            status,result = self._conn.executeDataNoCommit(prmSql,prmBinding)
            self._logger.info(application='',prm_query=prmBinding,prm_sql=prmSql,result_status=status,result_data=f"{result}")
            if not status:
                self.conn_close()
                return rs
            self.conn_commit()
            rs = self._success_status_execute
            rs['data']=result       
        except Exception as e:
            print(e)
        return rs
    def execute_data_same_session(self,conn,prmSql,prmBinding={}):
        self.conn_close()
        rs = self._failed_status_execute
        try:
            status,result = conn.executeDataNoCommit(prmSql,prmBinding)
            self._logger.info(application='',prm_query=prmBinding,prm_sql=prmSql,result_status=status,result_data=f"{result}")
            if not status:
                return rs
            rs = self._success_status_execute
            rs['data']=result       
        except Exception as e:
            print(e)
        return rs