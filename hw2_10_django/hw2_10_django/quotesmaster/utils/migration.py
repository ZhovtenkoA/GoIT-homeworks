
import os
import django

from pymongo import MongoClient
from quotes.models import Quote, Tag, Author
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotesmaster.settings')
django.setup()


client = MongoClient(
    "mongodb+srv://zhowtenkooleksiy:OdqjdrrgrJDD64qf@db-hw2-08.u8lqztr.mongodb.net/?retryWrites=true&w=majority"
)

db = client.hw2_09db

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname = author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description'],
    )
