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
        print("---------------------")
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectiolnFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("------------------")
    print("1. Add a record")
    print("2. Find a record by Name")
    print("3. Edit a record")
    print("4. Delet a record")
    print("5. Exit")
    option = input("Enter option: ")
    return option


def add_record():
    print("-------------------")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dob = input("Enter Date of Berth: ")
    gender = input("Enter gender: ")
    hair_color = input("Enter hair_color: ")
    new_doc = {"first": first.lower(), "last": last.lower(), "dob": dob, "gender": gender, "hair_color": hair_color}
    try:
        coll.insert(new_doc)
        print("-------------------------------")
        print("Document inserted into database")
    except:
        print("Error accessing databases")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
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


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]
main_loop()
