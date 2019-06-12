""" Project 4: Document Search Engine
Chris Specht
CPE 202-09
Spring 2019
"""


from hashtables import import_stopwords
from hashtables import HashTableLinear as HashTable


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

            # if word is already in term_freqs, skip it since it has already been processed
            if self.term_freqs.contains(word):
                continue # this should be the right command, it continues with next iteration of the loop

            # calculate frequency of this word in this document
            word_frequency = words.count(word) # returns number of occurences of this word in words

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
        pass

    # SEARCHING ====================================================================================


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