'''
Created on 14 apr 2012

@author: carl
'''
import unittest
from io import StringIO
import os

import autotodo


class TestItems(unittest.TestCase):

    def setUp(self):
        self.itemstring = '(A) 2012-04-15 Cut cake +birthday'
        self.item = autotodo.Item(self.itemstring)

    def tearDown(self):
        pass

    def test_initialize_and_print_item(self):
        itemstring = self.itemstring
        item = autotodo.Item(itemstring)
        self.assertEqual(itemstring, str(item))

    def test_item_is_done_nope(self):
        self.assertFalse(self.item.is_done())

    def test_item_is_done_yepp(self):
        item = autotodo.Item('x 2015-04-15 2012-04-15 Blow candles +birthday')
        self.assertTrue(item.is_done())


class TestParsing(unittest.TestCase):

    def test_parsing_and_counting(self):
        todofile = StringIO(
            'x 2012-04-15 2012-04-14 Bake cake+birthday\n2012-04-15 Light candles on cake +birthday\n')
        items = autotodo.parse(todofile)
        self.assertEqual(len(items), 2)

    def test_parsing_and_disregarding_empty_lines(self):
        todofile = StringIO(
            'x 2012-04-15 2012-04-14 Bake cake+birthday\n\n2012-04-15 Light candles on cake +birthday\n\n')
        items = autotodo.parse(todofile)
        self.assertEqual(len(items), 2)


class TestWriting(unittest.TestCase):

    def setUp(self):
        self.todoitems = [
            autotodo.Item('x 2012-04-15 2012-04-14 Bake cake+birthday'),
            autotodo.Item('2012-04-15 Light candles on cake +birthday')]
        self.todofile = StringIO(
            'x 2012-04-15 2012-04-14 Bake cake+birthday\n2012-04-15 Light candles on cake +birthday\n')

    def test_file_write_appending(self):
        """Check that something was written."""
        autotodo.write(self.todofile, self.todoitems, append=True)
        self.assertGreater(len(self.todofile.getvalue()), 100)

    def test_file_write_appending_missing_last_newline(self):
        """Check that at file not ending in a newline is properly appended
        to."""
        #Chops of last newline
        self.todofile.seek(0, os.SEEK_END)
        last_pos = self.todofile.tell()
        self.todofile.seek(last_pos - 1)
        self.todofile.truncate()
        autotodo.write(self.todofile, self.todoitems, append=True)
        self.todofile.seek(0)
        for line in self.todofile:
            self.assertLess(len(line), 80)

    def test_file_write_no_append(self):
        """Overwriting a file."""
        autotodo.write(self.todofile, self.todoitems, append=False)
        self.assertEqual(self.todofile.getvalue(),
                         '\n'.join(map(str, self.todoitems)) + '\n')

    def test_file_write_no_append_truncate(self):
        """Overwriting a file with somethin shorter."""
        autotodo.write(self.todofile, self.todoitems[0:1], append=False)
        self.assertEqual(self.todofile.getvalue(),
                    str(self.todoitems[0]) + '\n')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
