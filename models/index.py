from libs import Connection
class ModelIndex:
    def test():
        conn = Connection('SERAI')
        return conn.selectData('select current_date',{})
