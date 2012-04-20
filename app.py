#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")

from authors.models import *

while True:
    inp = raw_input()
    if inp == 'q':
        break
    try:
        returned = eval(inp)
    except Exception, e:
        print e
    else:
        print 'Returned : %s' % returned
