#!/usr/bin/env python
import os
import sys
import readline
import json

from levels import levels

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")


def dump_gameinfo(level=1, **kwargs):
    gameinfo = kwargs
    gameinfo['current_level'] = level
    with open('.gameinfo.json', 'w') as f:
        f.write(json.dumps(gameinfo))

def game_play():
    from django.db.models.query import QuerySet
    from authors.models import Book, Author, Publisher
    print "Type 'q' and press RETURN to quit"

    try:
        with open('.gameinfo.json', 'r') as f:
            level = json.loads(f.read())['current_level']
    except IOError:
        level = 1
        dump_gameinfo()

    level_changed = True
    while True:
        try:
            level_dict = levels[level]
        except IndexError:
            print "Great! You are a queryset Champion!"
            break
        if level_changed:
            print level_dict.get('greet')
        print level_dict.get('question')
        inp = raw_input(">>> ")
        if inp == 'q':
            break
        try:
            qs = eval(inp)
        except Exception, e:
            print e
        else:
            passed = level_dict['test'](qs)
            if passed:
                level_changed = True
                print level_dict['goodbye']
                level += 1
                dump_gameinfo(level=level)
            else:
                level_changed = False
                print 'Try again'


if __name__ == "__main__":
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode emacs')
    game_play()

