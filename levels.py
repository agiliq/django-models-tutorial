#!/usr/bin/env python
import os
import sys
import readline

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")

from authors.models import Book, Author, Publisher


def level1(inp):
    return inp == Book or inp == Author or inp == Publisher 

def level2(inp):
    return list(inp) == list(Author.objects.all())

def level3(inp):
    return list(inp) == list(Author.objects.filter(first_name = "Stephen"))

def level4(inp):
    return list(inp) == list(Book.objects.exclude(title = "The Merchant of Venice"))

def level5(inp):
    if inp == Author.objects.get(first_name="Neal", last_name="Stephenson"):
        Author.objects.get(first_name='Neal', last_name='Stephenson').delete()
        return True
    else:
        return False

def level6(inp):
    return inp == Author.objects.count()

def level7(inp):
    return list(inp) == list(Book.objects.order_by("title"))

def level8(inp):
    return list(inp) == list(Author.objects.filter(first_name="Stephen").exclude(last_name='Hawkings'))

def level9(inp):
    return inp == Book.objects.all()[0].publisher

def setup_level_9():
    book = Book.objects.all()[0]
    return {"book": book}

def level10(inp):
    return list(inp) == list(Publisher.objects.all()[0].book_set.all())

def setup_level_10():
    publisher = Publisher.objects.all()[0]
    return {"publisher": publisher}


levels = [
    {}, # To start from level1
    {
    
        'test': level1,
        'greet': """
    Welcome to the Queryget tutorial.
    The interactive queryset tutorial.
    INFO: Available models are Author, Book and Publisher
    INFO: Exit the prompt by typing "q"
    We assume some familiarity with Python and Django.
    The models present for this tutorial are
    Book, Author and Publisher
    """,
        'question': """
    Enter the name of any model.
    """,
        'goodbye': "Thats right. Remember each model in models.py maps to one table.",
    },
    {
    
        'test': level2,
        'greet': """
    The first method you should know about is .all.
    It will give you all the entries for a particular model.
    Eg to get all the Books, the command is
    Book.objects.all()
    """,
        'question': """
        How can you get all the Authors?
        """,
        'goodbye': """Thats right. Author.objects.all() will give you all the Authors. Publisher.objects.all() will give you all the publishers.
         """,
    },
    {
        'test': level3,
        'greet': """
    The second method is .filter.
    .filter filters out the queryset, based on the specific 
    field restrictions you set for the query.
    For example, to get the publishers with country as USA, you can use
    Publisher.objects.filter(country='USA')
    """,
        'question': """
    How can you get all the Authors with first_name Stephen?
    """,
        'goodbye': "Correct. Author.objects.filter(first_name='Stephen') will get you that.",
    },
    {
        'test': level4,
        'greet': """
    This level we'll learn about .exclude.
    .exlude like .filter, filters out the queryset, based on the specific 
    field restrictions you set for the query. But it excludes the ones
    matching the arguments. You can think of it as oposite of .filter.
    For example, to get the publishers with country other than USA, you can use
    Publisher.objects.exclude(country='USA')
    """,
        'question': """
    How can you get all the Books other than the one with The Merchant of Venice
    as title?
    """,
        'goodbye': "Good work",
    },
    {
        'test': level5,
        'greet': """
    This level we'll learn about .create.
    .create is to create new objects for a model. This creates new rows in database
    tables, and takes model fields as arguments
    For example, to create a new Author named John Grisham, you can use

    Author.objects.create(first_name='John', last_name='Grisham')
    """,
        'question': """
    Now, can you create a new author with name Neal Stephenson?
    """,
        'goodbye': "Cool, now we know about Neal Stephenson",
    },
    {
        'test': level6,
        'greet': """
    What about learning some counting?
    You can get the count of the number of objects we have in a table using
    .count 
    
    For example, to get the number of Authors in the database, you can use

    Author.objects.count()
    """,
        'question': """
    Now, can you check the number of Books in the Book model?
    """,
        'goodbye': "Thats right. We have %s books."%Book.objects.count(),
    },
    {
        'test': level7,
        'greet': """
    Now, let's do some ordering?
    We can order querysets by using order_by.
    
   For example, to get the 
authors sorted by first_name you can use
    Author.objects.all().order_by("first_name")
    """,
        'question': """
    Now, can you get all the Books sorted by title? 
    """,
        'goodbye': "Good work",
    },
    {
        'test': level8,
        'greet': """
    Now, We'll try multiple methods on same queryset.
    We can chain method queryset like .filter, .exclude. 
    
    For example, we can get all the publishers with country as USA,
    but, not Delacorte Press as name
    Publisher.objects.filter(country='USA').exlude(name='Delacorte Press')
    """,
        'question': """
    Now, can you get all authors with first_name Stephen, other than Stephen Hawkings? 
    """,
        'goodbye': "Good work",
    },
    {
    "setup": setup_level_9,
        'test': level9,
        'greet': """
    A queryset contains model instances. A model instance can be used to get access to other models it is related to
    via ForeignKey
    """,
        'question': """
    We have a book in the book variable. How can you get its publisher (see the models file to see the ForeignKeys).
    """,
        'goodbye': "Good work",
    },
    {
    "setup": setup_level_10,
        'test': level10,
        'greet': """
    Models create the functions to get the related objects in opposite direction as well. Since Book has a ForeignKey to Publisher,
    Publisher instances get a book_set method which can be used to get all the related books.
    """,
        'question': """
    We have a publisher in the publisher variable. How can you get all its related books (see the models file to see the ForeignKeys).
    """,
        'goodbye': "Good work",
    },
]
