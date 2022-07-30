import pymongo
client = pymongo.MongoClient("mongodb+srv://sri:devisri24.@sri.jguwuwq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)



d={
    'name':'sri',
   'email':'erg@gmail',
   'sur':'der'}
d={
    'name':'sri',
   'email':'erg@gmail',
   'sur':'der'}





db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)


