from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    ReferenceField,
    ListField,
)


class Authors(Document):
    fullname = StringField(required=True)
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    quote = StringField(required=True)
    author = ReferenceField(Authors)
    tags = ListField(StringField())
