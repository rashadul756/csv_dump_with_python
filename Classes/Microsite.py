import time
from Classes.Main import MainClass

class MicrositeClass(MainClass):
    
    def __init__(self, data):
        self.data = data

    def columns(self):
        return [
            'user_id',
            'microsite_theme',
            'microsite_domain_name',
            'microsite_website',
            'microsite_keywords',
            'microsite_company_name',
            'ar_microsite_company_name',
            'microsite_company_logo',
            'microsite_ownership_type',
            'microsite_establish_year',
            'microsite_total_employe',
            'microsite_about_company',
            'ar_microsite_about_company',
            'microsite_chairman_message',
            'microsite_service_offering',
            'ar_microsite_service_offering',
            'microsite_service_looking',
            'ar_microsite_service_looking',
            'microsite_mission',
            'ar_microsite_mission',
            'microsite_vission',
            'ar_microsite_vission',
            'microsite_director_name',
            'microsite_director_message',
            'ar_microsite_director_message',
            'microsite_director_photo',
            'microsite_contact_email',
            'microsite_contact_phone',
            'microsite_contact_mobile',
            'microsite_contact_fax',
            'microsite_contact_address',
            'ar_microsite_contact_address',
            'microsite_contact_map',
            'microsite_social_facebook',
            'microsite_social_twitter',
            'microsite_social_gplus',
            'microsite_social_linkedin',
            'microsite_created_datetime',
            'microsite_modified_datetime',
            'microsite_status',
            'microsite_verified',
            'microsite_working_hours',
            'microsite_reviews'
        ]
    
    def values(self, id): 
        verified = 'false'
        if self.data['Verified']:
            verified = 'true'

        if self.data['Location']:
            location = str(self.data['Location']).replace(' ', ',')
        else:
            location = ''

        if self.data['Keywords']:
            keywords = str(self.data['Keywords']).replace(',', '::')
        else:
            keywords = ''    

        return (
            id,
            'theme1',
            '',
            self.data['Website'],
            keywords,
            self.data['Title'],
            self.data['Title'],
            self.data['Logo'],
            4,
            self.data['Establishment year'],
            self.data['Employees'],
            self.data['Description'],
            self.data['Description'],
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            self.data['Company manager'],
            '',
            '',
            '',
            self.data['Email'],
            self.data['Phone'],
            self.data['Mobile'],
            self.data['Fax'],
            self.data['Address'],
            self.data['Address'],
            location,
            '',
            '',
            '',
            '',
            time.strftime('%Y-%m-%d %H:%M:%S'),
            time.strftime('%Y-%m-%d %H:%M:%S'),
            1,
            verified,
            self.data['Working hours'],
            self.data['Reviews']
        )
    
    def query(self):
        return '''insert into damas_user_microsite (%s) VALUES (%s)
            ''' %(self.query_columns(self.columns()), self.query_placeholders(self.columns())) 
