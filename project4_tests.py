""" Project 4: Document Search Engine Test Suite
Chris Specht
CPE 202-09
Spring 2019
"""


import unittest
from project4 import *


class TestSearchEngine(unittest.TestCase):

    def test_read_file(self):

        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)

        # get list of important words
        test_searchengine = SearchEngine("project4", stop_table)
        test_list = test_searchengine.read_file("data_structure.txt")
        
        print(test_list)


def test_main():
    unittest.main()


if __name__ == "__main__":
    test_main()
