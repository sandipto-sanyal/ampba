# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""
import string
import re
class FileCleaner:
    """This class will perform the following:
        1. breaks each line into words 
        2. strips whitespace and punctuation from the words
        3. and converts them to uppercase  
    """
    def __init__(self, path):
        """Reads the file passed through path and 
        creates a string of the contents of the file
        Parameters:
            path: string
            Path to the .txt file
        Returns:
            FileCleaner class object
        """
        with open(path, 'r') as file:
            self.file_content = file.read()
    
    def clean_text(self, string_of_char):
        """Reads a string of characters and break each line 
        Parameters:
            string_of_char: string
            String of characters to break each line by '.'
        Returns:
            List of sentences
        """
        list_of_sentences = string_of_char.split('.')[:-1]
        # break each line into words
        list_of_words = []
        for sentences in list_of_sentences:
            # remove punctuations
            sentences = sentences.translate(str.maketrans('', '', string.punctuation))
            # remove line feed characters
            sentences = re.sub('\n+', ' ', sentences)
            # strip white spaces from first to last
            sentences = sentences.strip() 
            # remove extra spaces within each word from the sentences
            sentences = re.sub(' +', ' ', sentences)
            # convert to upper case
            sentences = sentences.upper()
            # break the sentences into list of words
            list_of_words.append(sentences.split(' '))
        return list_of_words
    
if __name__=='__main__':
    path = r'datasets/Q8.txt'
    from Question_8 import FileCleaner
    fc = FileCleaner(path=path)
    string_of_char = fc.file_content
    list_of_words = fc.clean_text(string_of_char)
    print('List of words\n{}'.format(list_of_words))