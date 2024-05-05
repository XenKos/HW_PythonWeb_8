import json
import mongoengine
from mongoengine import Document, StringField, ReferenceField, ListField


mongoengine.connect("mongodb+srv://XenKos:<kseni4ka78>@cluster0.02433gx.mongodb.net/XenKos?retryWrites=true&w=majority")

class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author)
    tags = ListField(StringField())

with open('authors.json', 'r', encoding='utf-8') as f:
    authors_data = json.load(f)

for author_data in authors_data:
    author = Author(**author_data)
    author.save()

with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes_data = json.load(f)

for quote_data in quotes_data:
    author_fullname = quote_data.pop('author')
    author = Author.objects.get(fullname=author_fullname)
    quote_data['author'] = author
    quote = Quote(**quote_data)
    quote.save()