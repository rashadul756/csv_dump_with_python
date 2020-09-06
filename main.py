from tqdm.auto import tqdm
from Classes.Input import input
from Classes.Database import db
from Classes.User import UserClass
from Classes.UserDetail import UserDetailClass
from Classes.Membership import MembershipClass
from Classes.Microsite import MicrositeClass
from Classes.ProductService import ProductServiceClass
from Classes.MicrositeFile import MicrositeFileClass

for i in tqdm(range(len(input.data))):
    user = UserClass(input.data.iloc[i])
    user_detail = UserDetailClass(input.data.iloc[i])
    membership = MembershipClass()
    microsite = MicrositeClass(input.data.iloc[i])
    product_service = ProductServiceClass(input.data.iloc[i])
    microsite_file = MicrositeFileClass(input.data.iloc[i])
    
    inserted_ids = db.execute_transaction(user, membership, user_detail, microsite, index = i, data = input.data.iloc[[i]])
    
    if inserted_ids is not False:
        db.execute_multi(model = product_service, index = i, id = inserted_ids['UserClass'])
        db.execute_multi(model = microsite_file, index = i, id = inserted_ids['MicrositeClass'])


db.close

print('Total Success: {}'.format(db.total_success))
print('Total Fail: {}'.format(db.total_fail))
print('Total Duplicate: {}'.format(db.total_duplicate))   

'''
try: 
    user = UserClass(input.data.iloc[i])

    cursor = db.conn.cursor()
    user.insert(cursor)
    db.conn.commit()
    total_success = (total_success + 1)
except mysql.connector.Error as error :
    #data.iloc[[i]].to_csv('fail.csv', mode='a', header=False)
    db.conn.rollback()
    total_fail = (total_fail + 1)
    logging.error(' # id: {} # {}'.format(i, error))
finally:
    if(db.conn.is_connected()):
        cursor.close()

db.conn.close()        

print('Total Success: {}'.format(total_success))
print('Total Fail: {}'.format(total_fail))
print('Total Duplicate: {}'.format(total_duplicate))    
'''

'''
df = pd.read_csv("Input/emails.csv")
data = df.replace(np.nan, '', regex=True)

user = UserClass(data)
db = DatabaseClass()

col = user.query()

cursor = db.conn.cursor()

print(db.conn)
'''