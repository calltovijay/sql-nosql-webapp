import pymysql
import pandas as pd
import base64


class DBConnection:
    def __init__(self):
        #local MySQL config
        # host = "127.0.0.1"
        # user = "root"
        # password = b'Z2F5YXRocmk0'

        # AWS RDS MySQL config
        host = "mysqldb-spring-2020.cojfgxld8ebp.us-east-1.rds.amazonaws.com"
        user = "admin"
        password = b'bXlzcWwyMDIw'

        db = "nps"
        self.con = pymysql.connect(host=host, user=user, password=base64.b64decode(password.decode()), db=db,
                                   cursorclass=pymysql.cursors.
                                   DictCursor)

    def get_query_results(self, sql):
        status_message = "Success"
        df = None
        try:
            df = pd.read_sql_query(sql, self.con)
        except:
            status_message ="Error: Invalid SQL Query. Please validate"
        return df, status_message
