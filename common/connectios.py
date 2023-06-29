import psycopg2
import global_variable

class Connection:
    def __init__(self,paramDatabase='',**kwargs):
        database = ''
        dictDb =global_variable.DATABASE.get(paramDatabase,{})
        db_user = dictDb.get('USER')
        db_pass = dictDb.get('PASSWORD')
        db_name = dictDb.get('DBNAME')
        db_host = dictDb.get('HOST')
        db_port = dictDb.get('PORT')
        paramDatabase = "host='"+db_host+"' dbname='"+db_name+"' user='"
        paramDatabase += db_user+"' password='"+db_pass+"' "
        paramDatabase += 'port= '+db_port
        database = paramDatabase
        self.autocommit = kwargs.get('autocommit')
        self._conn = psycopg2.connect(database)
        self._curs = self._conn.cursor()
    def selectData(self,prmSql,prmBinding):
        status = True
        
        try:
            self._curs.execute(prmSql, prmBinding)
            data = self._curs.fetchall()
        except Exception as exc :
            status = False
            data = "Error : " + str(exc)
            data2 = "SELECT STATEMENT SALAH: " + prmSql + " param" + str(prmBinding)
        result = data
        return status, result 
    def executeData(self,prmSql,prmBinding):
        status = True
        data = ""
        try:
            self._curs.execute(prmSql, prmBinding)
            if self.autocommit:
                self._conn.commit()
        except psycopg2.Error as exc:
            error = exc
            data = "Error : "+str(error)
            status = False
        result = data
        return status, result
    def forCommit(self):
        status = True
        data = ""
        try:
            self._conn.commit()
        except psycopg2.Error as exc:
            error = exc
            status = False
            data = "Error : "+str(error)

        result = data
        return status, result

    def delete(self):
        status = True
        data = ""
        try:
            self._conn.close()
        except psycopg2.Error as exc:
            status = False
            error = exc
            data = "Error : "+str(error)

        result = data
        return status, result
