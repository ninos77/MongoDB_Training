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


def get_record():
    print("")
    print("--- Get Record By First Name")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing databases")

    if not doc:
        print("")
        print("****No Record Find it****")
    return doc


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


def find_record():
    print("")
    doc = get_record()
    print("")
    if doc:
        print("------------------")
        for k, v in doc.items():
            if k != "_id":
                print(k+": "+v.capitalize())
        print("------------------")


def edit_record():
    doc = get_record()
    if doc:
        uppdate_doc = {}
        for k, v in doc.items():
            if k != "_id":
                uppdate_doc[k] = input(k.capitalize() + "[" + v + "]: ").lower()
                if uppdate_doc[k] == "":
                    uppdate_doc[k] = v
        try:
            coll.update_one(doc, {"$set": uppdate_doc})
            print("")
            print("document update it......")
        except:
            print("Error accessing databases")


def delet_record():
    doc = get_record()
    if doc:
        for k, v in doc.items():
            if k != "_id":
                print(k+": "+v.capitalize())
        confirmation = input("Did you want to delet this record (Y/N): ")
        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("Document has been removed")
            except:
                print("Error accessing databases")
        else:
            print("Document Not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delet_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]
main_loop()
