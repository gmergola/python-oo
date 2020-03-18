"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """reads a file and makes an attribute equal
    to a list of words in file
    
    >>> wf = WordFinder("/Users/gennamergola/Desktop/test.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, file_path):
        """reading file, printing out words within file"""
        self.file_str = open(file_path).read()
        self.list_words = self.make_list()
        
        print(f"{len(self.list_words)} words read")
   
    def make_list(self):
        """ making list of words read from file"""
        return self.file_str.split('\n')
    
    def random(self):
        """ prints out a random word from list_words"""

        return random.choice(self.list_words)

    class SpecialWordFinder(WordFinder):
        """ Special word finder that gets rid of blank lines and comments.

        """
        def __init__(self,file_path):
            """get parent class """
            super().__init__(file_path)

        def make_list(self):
            "creating a list of words without blank lines and #mark"
            words = super().make_list()
        return [word for word in words if not word.startswith("#") and not word == ""]
