import pymysql
import pandas as pd
import base64


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = b'Z2F5YXRocmk0'
        db = "nps"
        self.con = pymysql.connect(host=host, user=user, password=base64.b64decode(password.decode()), db=db,
                                   cursorclass=pymysql.cursors.
                                   DictCursor)

    def get_query_results(self, sql):
        df = pd.read_sql_query(sql, self.con)
        return df
