from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        "mongodb+srv://zhowtenkooleksiy:OdqjdrrgrJDD64qf@db-hw2-08.u8lqztr.mongodb.net/?retryWrites=true&w=majority"
    )

    db = client.hw2_09db
    return db
