""" Project 4: Document Search Engine
Chris Specht
CPE 202-09
Spring 2019
"""


from hashtables import import_stopwords
from hashtables import HashTableLinear as HashTable
import os, math


class SearchEngine:
    """ Builds and maintains an inverted index of documents stored in a specified directory and
    provides a functionality to search documents with query terms
    Attributes:
        directory (str): a directory name
        stopwords (HashTable): contains stopwords
        doc_length (HashTable): contains number of words in each document
        doc_freqs (HashTable): contains number of documents containing the term for each term
        term_freqs (HashTable): hash table of hash tables for each term, each hash table contains
                                the frequency of the term in documents (document names are the keys
                                and the frequencies are the values)
    """
    def __init__(self, directory, stopwords):
        self.doc_length = HashTable()
        self.doc_freqs = HashTable()  #this will not be used in this assignment
        self.term_freqs = HashTable()
        self.stopwords = stopwords
        self.index_files(directory)

    # PREPROCESSING ================================================================================

    def read_file(self, infile):
        """ A helper function to read a file
        Args:
            infile (str): the path to a file
        Returns:
            list: a list of strings read from a file
        """
        # open file
        with open(infile, "r") as f:
            lines = f.readlines() # looks like ["line 1 here", "line 2 here", "line 3 here"]
        return lines

    def parse_words(self, lines):
        """ Split strings into words, convert words to lower cases and remove newline characters,
        exclude stopwords
        Args:
            lines (list): a list of strings
        Returns:
            list: a list of words
        """
        raw_words = []
        for line in lines:
            split_line = line.split(" ") # split line looks like ["line", "1", "here"]
            raw_words.extend(split_line)
        
        # create new list with all words that aren't stop words
        # remove newline characters, convert to lowercase
        filtered_words = [word.rstrip().lower() for word in raw_words if word not in self.stopwords]

        return filtered_words

    def count_words(self, filename, words):
        """ Count words in a file and store the frequency of each word in the term_freqs hash table.
        Words should not contain stopwords. Also store the total count of words contained in the
        file in the doc_length hash table.
        Args:
            filename (str): the file name
            words (list): a list of words
        """
        # store total count of words in the doc_length hash table
        self.doc_length.put(filename, len(words))

        # iterate through each word
        for word in words:

            # calculate frequency of this word in this document
            word_frequency = words.count(word) # returns number of occurences of this word in words

            # if word is already in term_freqs
            if self.term_freqs.contains(word):
                # add new ("doc1", freq) pair to term_freqs[word] (which is the lower hashtable)
                self.term_freqs[word][1].put(filename, word_frequency)

            # if word is not already in term_freqs
            else:
                # create new frequency hashtable for each term ("doc1", frequency)
                freq_hashtable = HashTable()
                freq_hashtable.put(filename, word_frequency)
                # put this newly created hash table into term_freqs hash table ("term1", freq_hashtable)
                self.term_freqs.put(word, freq_hashtable)

    def index_files(self, directory):
        """ Index all text files in a given directory
        Args:
            directory (str) : the path of a directory
        """
        # get a list of files in the directory
        file_list = os.listdir(directory)

        # for each item in file_list, item is a filename
        for item in file_list:

            # construct full path of each file
            path = os.path.join(directory, item)

            # if item is not a file, skip it
            if not os.path.isfile(path) or item == "stop_words.txt":
                continue

            # split path into file extension and the rest
            parts = os.path.splitext(item)

            # only process text files
            if parts[1] == ".txt":

                # process it
                item_lines = self.read_file(item)
                item_words = self.parse_words(item_lines)
                self.count_words(item, item_words)

    # SEARCHING ====================================================================================

    def get_wf(self, term_frequency):
        """ Computes the weighted frequency
        Args:
            term_frequency (float): term frequency
        Returns:
            float: the weighted frequency
        """
        if term_frequency > 0:
            wf = 1 + math.log(term_frequency)
        else:
            wf = 0
        return wf

    def get_scores(self, terms):
        """ Creates list of scores for each file in corpus. 
        The score = (weighted frequency / total word count in file)
        Compute the score for each term in a query and sum all the scores.
        Args:
            terms (list): a list of strings
        Returns:
            list: a list of tuples, each containing the filename and its relevancy score
        """
        # scores = HashMap()
        # for each query term "term"
            # fetch a hash table of "term" from self.term_freqs
            # for each file in the hash table, add weighted frequency to scores[file]
        # for each file in scores, do scores[file] /= self.doc_length[file]
        # return scores, which is a list of tuples

    def rank(self, scores):
        """ Ranks files in the descending order of relevancy
        Args:
            scores (list): list of tuples of (filename, score)
        Returns:
            list: a list of filenames sorted in descending order of relevancy
        """
        pass

    def search(self, query):
        """ Search for the query terms in files
        Args:
            query (str): query input
        Returns:
            list: a list of files in descending order of relevancy
        """
        pass

def main():
    """ Entry point of the program
    """
    # takes a directory name as its command line argument
    # create an instance of SearchEngine by passing the directory name
    # enter an infinite loop
        # prompt user for input
            # if input is "q"
                # exit loop and end session
            # if input is "s:insert search query here"
                # convert search query terms to lowercase if necessary
                # search for relevant documents and print a list of file names in descending order
                # of relevancy
    pass


if __name__ == "__main__":
    main()