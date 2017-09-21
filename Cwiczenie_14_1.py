# -*- coding: utf-8 -*-
"""

"""

def sed(orig_string, new_string, file_n1, file_n2):
    '''Reads the first file and writes the second file.
    If the original string is found in the first file, it is replaced by the new string.
    orig_string: string
    new_string: string
    file_n1: name of the original file
    file_n2: name of the second file
    '''
    try:
        file1 = open(file_n1) 
        new_f = open(file_n2, 'w')
    except:
        print('Error while opening a file')
        return
        
    try:    
        content1 = file1.read()
    except:
        print('Error while reading the file')
        return
        
    if orig_string in content1:
        content1 = content1.replace(orig_string, new_string)
        
    try:    
        new_f.write(str(content1))
    except:
        print('Error while writing data')
        return
     
    try:
        new_f.close()
    except:
        print('Error while closing the file')
        return
        
        
def main():
    first_s = 'Anaconda'
    second_s = 'Python'
    filename1 = path\\memo.txt'  #correct paths
    filename2 = path\\new_memo.txt' #correct paths
    sed(first_s, second_s, filename1, filename2)
       
if __name__ == '__main__':
    main()
         
    