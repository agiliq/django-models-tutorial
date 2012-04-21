#!/usr/bin/env python
import os
import sys
import readline
import json

from django.utils.termcolors import colorize

from levels import levels

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")


def dump_gameinfo(**kwargs):
    """
    1. Assume that this file always exists and has valid json
    2. Update the loaded json with kwargs and rewrite the file
    """
    with open('.gameinfo.json', 'r') as f:
        game_info = json.loads(f.read())
        if 'username' not in game_info:
            game_info['username'] = raw_input("Please enter your name: ")
    with open('.gameinfo.json', 'w') as f:
        game_info.update(kwargs)
        f.write(json.dumps(game_info))


def print_models():
    print colorize("Here is the models.py.\n-----------\n", fg="green")
    print open("authors/models.py", "r").read()
    print colorize("--------\n", fg="green")

def print_help():
   print colorize("""
         q: quits the game
         h: print this help
         m: prints the models.py
       """, fg="green")

def game_play():
    "Imports all models. Runs the game"
    from authors.models import Book, Author, Publisher
    print_help()
    game_info = {}
    try:
        with open('.gameinfo.json', 'r') as f:
            game_info = json.loads(f.read())
            level = game_info['level']
            username = game_info['username']
    except IOError:
        with open('.gameinfo.json', 'w') as f:
            f.write('{}')
        level = 1
        dump_gameinfo(level=1)

    level_changed = True
    while True:
        try:
            level_dict = levels[level]
        except IndexError:
            print "Great! You are a queryset Champion!"
            if raw_input("Do you want to play again? [yn] ") == 'y':
                level = 1
                dump_gameinfo(level=1)
                continue
            else:
                break
        if level_changed:
            print colorize(level_dict.get('greet'), fg="blue")
        print colorize(level_dict.get('question'), fg="green")
        inp = raw_input(">>> ")
        if inp == 'q':
            break
        elif inp in ['h', 'help']:
            print_help()
            continue
        elif inp in ['m', 'models']:
            print_models()
            continue

        try:
            qs = eval(inp)
        except Exception, e:
            print e
        else:
            try:
                passed = level_dict['test'](qs)
            except Exception, e:
                passed = False
            if passed:
                level_changed = True
                print colorize(level_dict['goodbye'], fg="red")
                level += 1
                dump_gameinfo(level=level)
            else:
                level_changed = False
                print colorize("Try again", fg="blue")


if __name__ == "__main__":
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode emacs')
    game_play()

