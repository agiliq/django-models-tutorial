#!/usr/bin/env python
import os
import sys
import readline

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")

from authors.models import Book, Author, Publisher


def level1(inp):
    return True
    
def level2(inp):
    return list(inp) == list(Author.objects.all())

def level3(inp):
    return list(inp) == list(Author.objects.filter(first_name = "Stephen"))
    

levels = [
    {}, # To start from level1
    {
        'test': level1,
        'greet': """
    Welcome to the Queryget tutorial.
    The interactive queryset tutorial.
    exit the prompt by typing "q"
    """,
        'question': """
    What is your name?
    """,
        'goodbye': "",
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
        'goodbye': "",
    },
    {
        'test': level3,
        'greet': """
    The first article you should know about is .all.
    It will give you all the entries for a particular model.
    Eg to get all the Books, the command is
    Book.objects.all()
    """,
        'question': """
    How can you get all the Authors?
    """,
        'goodbye': "",
    }
    
]
