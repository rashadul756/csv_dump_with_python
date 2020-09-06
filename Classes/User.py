from Classes.Main import MainClass

class UserClass(MainClass):
    
    def __init__(self, data):
        self.data = data

    def columns(self):
        return ['user_email','user_password','login_count']
    
    def values(self, id): 
        return (self.data['Email'],'20eabe5d64b0e216796e834f52d61fd0b70332fc',1)
    
    def query(self):
        return '''insert into damas_user (%s) VALUES (%s)
            ''' %(self.query_columns(self.columns()), self.query_placeholders(self.columns())) 
