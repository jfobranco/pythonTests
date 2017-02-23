import mysql.connector

class db:
    user = 'root'
    password = 'root'
    host = 'localhost'
    database = 'exercise'
    con = None
    
    config = {
        'user': user,
        'password': password,
        'host': host,
        'database': database,
        'raise_on_warnings': True,
    }
    
    def connect(self):
        if (self.con == None):
            self.con =  mysql.connector.connect(**self.config)
        
        return self.con
    
    def close(self):
        if (self.con != None):
            self.con.close()

    
    def executeSQL(self, sql, params):
        cnx = connect()
        
        result = True
        try:
            with cnx.cursor() as cursor:
                cursor.execute(sql, params)
            cnx.commit()
        finally:
            self.close()
        
        return result
    
    def execute(self, sql):
        cnx = connect()
        
        try:
            with cnx.cursor() as cursor:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                #result = cursor.fetchone()
        finally:
            self.close()