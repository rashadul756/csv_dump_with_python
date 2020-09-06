from datetime import datetime
from datetime import timedelta
from Classes.Main import MainClass

class MembershipClass(MainClass):
    
    def __init__(self):
        pass

    def columns(self):
        return [
            'user_id',
            'membership_id',
            'md_add_products',
            'md_send_inquiries',
            'md_featured_products',
            'md_verified_member',
            'md_create_microsite',
            'md_add_products_used',
            'md_send_inquiries_used',
            'md_featured_products_used',
            'md_membership_start_date',
            'md_membership_upgrade_date',
            'md_membership_end_date'
        ]
    
    def values(self, id): 
        return (id, 1, 5, 5, 2, 0, 1, 0, 1, 0, 
            str(datetime.now()), 
            str(datetime.now()), 
            str(datetime.now() + timedelta(days=365))) 
    
    def query(self):
        return '''insert into damas_user_membership_detail (%s) VALUES (%s)
            ''' %(self.query_columns(self.columns()), self.query_placeholders(self.columns())) 
