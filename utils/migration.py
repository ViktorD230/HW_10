import os
import django
from mongoengine import connect
from .models import Authors, Quotes 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()

from quoteapp.models import Author, Quote, Tag

mongo_user = "vikd_mongo"
mongodb_pass = "qwerty123456"
db_name = "book"
domain = "cluster0.ytfhotl.mongodb.net"


connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)

authors = Authors.objects()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes = Quotes.objects()

for quote in quotes:
    tags = []
    for tag in quote.tags:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    
    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))
    try:
        if not exist_quote:
            author_query = Authors.objects(id=quote.author.id)
            if author_query.first():
                author = author_query.first()
                a = Author.objects.get(fullname=author['fullname'])
                q = Quote.objects.create(quote=quote['quote'], author=a)
            
            for tag in tags:
                q.tags.add(tag)
    except AttributeError:
        continue



