import pymongo

myclient = pymongo.MongoClient("mongodb://iflushot:qwe123@ds054999.mlab.com:54999/iflushot")

mydb = myclient["iflushot"]

print(mydb.list_collection_names())

