#!/usr/bin/env python3
# Author ID: kang-kang

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    file_list = f.read()
    f.close()
    return file_list

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    file_list = list(f)
    f.close()
    new_list = []
    for x in file_list:
        new_list.append(x.strip())
    return new_list


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))