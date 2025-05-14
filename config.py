import pymongo

class Config(object):

    # Mongodb
    MONGODB_URI = "mongodb+srv://sivaprakasamulaganathan:7yVnXJwsk8M1p1Af@cluster0.v6vqw1o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    myclient = pymongo.MongoClient(MONGODB_URI)
    mydb = myclient["mydatabase"]
    users = mydb["users"]
    sessions = mydb["sessions"]
    workdata = mydb["data"]

    # Connection
    HOST = "127.0.0.1"
    PORT = "80"
