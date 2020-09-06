import time
from Classes.Main import MainClass

class UserDetailClass(MainClass):
    
    def __init__(self, data):
        self.data = data

    def columns(self):
        return [
            'membership_id', 
            'user_id',
            'is_frequent_buyer',
            'user_lang',
            'user_fullname',
            'ar_user_fullname',
            'user_phone_no',
            'user_country',
            'user_city',
            'user_type',
            'user_status',
            'approved_by',
            'salesperson_id',
            'is_mobile_verified',
            'mobile_OTP',
            'user_last_login',
            'user_created_datetime',
            'user_modify_datetime',
            'keyword',
            'landline',
            'website',
            'ar_keyword',
            'fax'
        ]
    
    def values(self, id): 
        if self.data['Mobile']:
            mobile = self.data['Mobile']
        else:
            mobile = self.data['Phone']    

        return (
            1,
            id,
            0,
            'en',
            '',
            '',
            mobile,
            190,
            1,
            't',
            '1',
            0,
            0,
            '1',
            '123456',
            time.strftime('%Y-%m-%d %H:%M:%S'),
            time.strftime('%Y-%m-%d %H:%M:%S'),
            time.strftime('%Y-%m-%d %H:%M:%S'),
            '',
            self.data['Phone'],
            self.data['Website'],
            '',
            self.data['Fax']
        )
    
    def query(self):
        return '''insert into damas_user_detail (%s) VALUES (%s)
            ''' %(self.query_columns(self.columns()), self.query_placeholders(self.columns())) 
