from pymongo import MongoClient
uri = "mongodb://root:rootpassword@mongodb_container:27017/?authSource=fastapi&authMechanism=SCRAM-SHA-1"
url="mongodb://root:rootpassword@mongodb_container:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.0"
conn = MongoClient(url)