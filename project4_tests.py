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
        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/docs", stop_table)

    def test_parse_words(self):
        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)

        # get list of important words
        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/docs", stop_table)


    def test_count_words(self):
        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)

        # get list of important words
        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/docs", stop_table)

    def test_index_files(self):
        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)

        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/docs", stop_table)
        # print(test_searchengine.doc_length)
        # print(test_searchengine.term_freqs)

    def test_get_scores(self):
        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)
        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/docs", stop_table)
        test_results = test_searchengine.get_scores(["computer", "science"])
        # print(test_results)
        self.assertAlmostEqual(test_results[1][1], 1)
        # print(test_results)

    def test_rank(self):
        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)
        # creates test searchengine object
        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/docs", stop_table)
        test_scores = (("file1.txt", 1), ("file2.txt", 2), ("file3.txt", 3))
        test_result = test_searchengine.rank(test_scores)
        desired_result = [("file3.txt", 3), ("file2.txt", 2), ("file1.txt", 1)]
        self.assertEqual(test_result, desired_result)

    def test_search(self):
        # creates stop_word hash table
        stop_table = HashTable()
        stop_table = import_stopwords("stop_words.txt", stop_table)
        # creates test searchengine object
        test_searchengine = SearchEngine("/mnt/c/College/cpe202/project4/document-search-engine/docs", stop_table)

        test_searchengine.search("Computer Science")


def test_main():
    unittest.main()


if __name__ == "__main__":
    test_main()
