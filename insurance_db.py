from pymongo import MongoClient

db_name='insurance_database'
myclient=MongoClient('mongodb://localhost:27017/')
db=myclient[db_name]
collection_user = db['user_details']
collection_prediction = db['smoker_details']

def register_user(user_data):
    user_data_dict = {}
    user_data_dict['name'] = user_data['name']
    user_data_dict['password'] = user_data['password']
    user_data_dict['age'] = user_data['age']
    user_data_dict['sex'] = user_data['sex']

    collection_user.insert_one(user_data_dict)
    return 'success'


def login_user(login_details):
    user_data_dict = {}
    user_data_dict['name'] = login_details['name']
    user_data_dict['password'] = login_details['password']
    
    response = collection_user.find_one(user_data_dict)
    if not response:
        return 'Invalid User id or Password'
    return 'Login Successfully'

def save_smoker_details(age,sex,bmi,region,smoker,prediction):

    smoker_details = {'age':age,'sex':sex,
                      'bmi':bmi,'region':region,'smoker':smoker,'prediction':prediction}
                
    collection_prediction.insert_one(smoker_details)

    return 'saved successfully'

