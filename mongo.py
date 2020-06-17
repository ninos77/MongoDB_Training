import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = "testDB"
COLLECTION_NAME = "MyfirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected !!")
        return conn
    except pymongo.errors.ConnectiolnFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)