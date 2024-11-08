import pymongo
from config import get_config

cfg = get_config()

def setup_client(config):
    try:
        client = pymongo.MongoClient(config['db_url'])
        print("Connection setup is successful...")
        return client
    except Exception as e:
        return print("Failed to setup the connection...")


client = setup_client(cfg)   
db = client[cfg['database']]
collection = db[cfg['collection']]
     
query = {"USN":"1AM23CI062"}     
info = collection.find(query)
for x in info:
    print(x)
    name = x['Student Name']
    print(name)