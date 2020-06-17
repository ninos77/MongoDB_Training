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
        return conn
    except pymongo.errors.ConnectiolnFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by Name")
    print("3. Edit a record")
    print("4. Delet a record")
    print("5. Exit")
    option = input("Enter option: ")
    return option


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


show_menu()
main_loop()
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()
