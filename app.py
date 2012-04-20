#!/usr/bin/env python
import os
import sys
import readline

from levels import levels

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")


def game_play():
    from django.db.models.query import QuerySet
    from authors.models import Book, Author, Publisher
    print "Type 'q' and press RETURN to quit"

    level = 1
    level_changed = True

    while True:
        level_dict = levels[level]
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
            if level_dict['test'](qs):
                level_changed = True
                print 'Good!'
                level += 1
            else:
                level_changed = False
                print 'Try again'


if __name__ == "__main__":
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode emacs')
    game_play()

