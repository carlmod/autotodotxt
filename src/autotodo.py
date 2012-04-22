# -*- coding: utf-8 -*-
"""
    autotodo.module
    ~~~~~~~~~~~~~~

    Automatic management of todo.txt - files

    :copyright: (c) 2012 by Carl Modén.
    :license: GPL v3 or later, see LICENSE_FILE for more details.
"""

import os


class Item(object):

    """A single todo item."""

    def __init__(self, string):
        """Create a todo item from a string. The string should be in todo.txt
        format"""
        self._itemlist = string.split(' ')

    def __str__(self):
        return(' '.join(self._itemlist))

    def __repr__(self):
        return self.__str__()

    def is_done(self):
        """Returns true if the item is done, otherwise false."""
        if self._itemlist[0] == 'x':
            return True
        else: return False


def parse(file):
    """Parse a file and return a list of Items
    
    Parameter
    ---------
    file: a file like object
        the file like to be parsed
        
    Returns
    -------
    a list of Items that the file contained
    
    """
    todolist = []
    for line in file:
        line = line.strip()
        if line:
            todolist.append(Item(line))
    return todolist

def write(file, todolist, append=True):
    """Write a todo file from a list of items.
    
    Parameter
    ---------
    file: a file like object
        The file to which the items shall be written to
    todolist: an iterable
        The items to be written to file
    append: a boolean
        If True the items will be added in the end of the file, if False the
        file content will be overwritten.

    """
    if append:
        file.seek(0, os.SEEK_END)
        last_pos = file.tell()
        last_char = file.seek(last_pos - 1)
        if not last_char == '\n':
            file.seek(last_pos)
            file.write('\n')
    else:
        file.seek(0, os.SEEK_SET)
    for item in todolist:
        file.write(str(item))
        file.write('\n')
    if not append:
        file.truncate()
