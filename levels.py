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

levels = [
    {}, # To start from level1
    {
        'test': level1,
        'greet': """
    Welcome to the Queryget tutorial.
    The interactive queryset tutorial.
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
    The first article you should know about is .all.
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
    The second article is about filter.
    Filter filters out the queryset, based on the specific 
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
    This level we'll learn more about exclude.
    exlude too, like filter, filters out the queryset, based on the specific 
    field restrictions you set for the query. But, it just excludes the ones
    matching the arguments.
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
    This level we'll learn more create.
    create is to create new objects for a model. This creates new rows in database
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
    You can get the count of the number of objects we have in our database using
    count statement
    
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
    }





]
