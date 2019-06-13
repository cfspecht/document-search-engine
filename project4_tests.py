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
        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/", stop_table)

        """
        test_list = test_searchengine.read_file("data_structure.txt")
        
        # print(test_list)
        """

    def test_parse_words(self):

        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)

        # get list of important words
        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/", stop_table)

        """
        test_lines = test_searchengine.read_file("data_structure.txt")

        # parse words
        test_words = test_searchengine.parse_words(test_lines)

        # print(test_words)
        """

    def test_count_words(self):

        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)

        # get list of important words
        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/", stop_table)

        """
        test_lines = test_searchengine.read_file("test.txt")

        # parse words
        test_words = test_searchengine.parse_words(test_lines)

        test_searchengine.count_words("test.txt", test_words)

        print(test_searchengine.doc_length)

        print(test_searchengine.term_freqs)
        """

    def test_index_files(self):

        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)

        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/", stop_table)
        print(test_searchengine.doc_length)
        # print(test_searchengine.term_freqs)



def test_main():
    unittest.main()


if __name__ == "__main__":
    test_main()
