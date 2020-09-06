from sys import exit
import logging
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Classes.Output import output

class DatabaseClass():

    total_success = 0
    total_fail = 0
    total_duplicate = 0

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='baahis_app',
                passwd='baahis_app123',
                database='baahis_dump'
            )
            self.conn.autocommit = False 
            logging.basicConfig(filename='./error.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        except mysql.connector.Error as error :
            print('Database not connected.')
            exit(0)


    def execute(self):
        pass        

    def execute_transaction(self, *models, index, data):
        inserted_ids = {}
        try:
            cursor = self.conn.cursor()
            for model in models:
                if(model.__class__.__name__ == 'UserClass'):
                    user_data = model.values(None)
                    is_already_exists = self.check_email_already_exists(user_data[0])
                    if is_already_exists == True:
                        output.duplicate(data)
                        self.total_duplicate = (self.total_duplicate + 1)
                        return False
                
                if 'UserClass' in inserted_ids:
                    cursor.execute(model.query(), model.values(inserted_ids['UserClass'])) 
                else:
                    cursor.execute(model.query(), model.values(None)) 

                inserted_ids[model.__class__.__name__] = cursor.lastrowid

            self.conn.commit()
            output.success(data)
            self.total_success = (self.total_success + 1)
            return inserted_ids
        except mysql.connector.Error as error :
            output.fail(data)
            self.conn.rollback()
            logging.error(' # id: {} # {}'.format(index, error))
            self.total_fail = (self.total_fail + 1)
        finally:
            if(self.conn.is_connected()):
                cursor.close()    

        return False        

    def execute_multi(self, model, index, **data):
        try:
            cursor = self.conn.cursor()
            cursor.executemany(model.query(), model.values(data['id']))
        except mysql.connector.Error as error :
            logging.error(' # id: {} # {}'.format(index, error))
        finally:
            if(self.conn.is_connected()):
                cursor.close()     

    
    def check_email_already_exists(self, email):
        cursor = self.conn.cursor()
        sql = '''SELECT user_id FROM damas_user WHERE user_email = %s'''
        cursor.execute(sql, (email,))
        cursor.fetchall()
        if cursor.rowcount > 0:
            return True
        return False


    def close():
        self.conn.close()    


db = DatabaseClass()
