import pymongo

myclient = pymongo.MongoClient("mongodb://iflu:qwe123@ds030719.mlab.com:30719/iflushot")

mydb = myclient["iflushot"]

print(mydb.list_collection_names())


patient_collection = mydb.get_collection("patients")

def add_patient(req_data):
    patient_collection.insert_one(req_data)