# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""
import string
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
    
    def break_each_line(self, string_of_char):
        """Reads a string of characters and break each line
        Parameters:
            string_of_char: string
            String of characters to break each line by '.'
        Returns:
            List of sentences
        """
        list_of_sentences = string_of_char.split('.')
        return list_of_sentences
    
    def convert_sentences(self, list_of_sentences):
        """Convert the sentences as below:
            1. strips whitespace and punctuation from the words
            2. converts them to uppercase
        Parameters:
            list_of_sentences: list
            List of sentences separated by new line from our file
        Returns:
            List of sentences with extra white spaces stripped
        """
        for i, sentences in enumerate(list_of_sentences):
            sentences = sentences.strip() # strip white spaces
            sentences = sentences.translate(str.maketrans('', '', string.punctuation)) # remove punctuations
            sentences = sentences.upper() # convert to upper case
            list_of_sentences[i] = sentences
        return list_of_sentences

if __name__=='__main__':
    path = r'datasets/Q8.txt'
    from Question_8 import FileCleaner
    fc = FileCleaner(path=path)
    string_of_char = fc.file_content
    list_of_sentences = fc.break_each_line(string_of_char)
    list_of_sentences = fc.convert_sentences(list_of_sentences)
    print("The cleaned text::::")
    print(' '.join(list_of_sentences))