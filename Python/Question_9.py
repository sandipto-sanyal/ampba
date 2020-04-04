# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""

import os

class DirectorySearch:
    
    def __init__(self, directory, suffix):
        self.rootdir = directory
        self.suffix = suffix
    
    def walk_directory(self):
        list_of_files_with_suffix = []
        for root, subdirs, files in os.walk(self.rootdir):
            for filename in files:
                # check whether the given suffix = the suffix in the file name
                # os.path.splitext takes care of filename where last characters
                # after '.' denotes the file extension/suffixl
                filename_without_suffix, file_extension = os.path.splitext(filename)
                if self.suffix == file_extension:
                    list_of_files_with_suffix.append(os.path.join(root,filename))
        return list_of_files_with_suffix

if __name__ == '__main__':
    print('Provide the directory name to scan: ')
    directory = input()
    print('Provide the suffix of the file names to scan: ')
    suffix = input()
    ds = DirectorySearch(directory, suffix)
    list_of_files_with_suffix = ds.walk_directory()