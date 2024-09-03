from pymongo import MongoClient
connection_string= "mongodb+srv://ankitk2002121:PEpfghfsCbMYgqYQ@farmerproject.1ytnv.mongodb.net/?retryWrites=true&w=majority&appName=farmerproject"
client = MongoClient(connection_string) #client == conn
database = client['Farmer']
collection = database['FarmerDetail']

documents = collection.find()  # select * from table;
for document in documents: 
    print(document) 
print("thank you!")
