#Algorithm for Reading and Writing a File
def read_write_file(filename,add):
    ''' file, string --> string

    :param filename:Name of file to be created or add to with its extension e.g. filename.txt
    :param add: The string to be added to the file. \n can be used as suffix to create new line
    :return: Returns the created file or read the modified file
    Format:
    import read_write_file_algorithm as rd
    rd.read_write_file('Yes.txt','Do you love me?')

    Example:
    >>> read_write_file('Yes.txt','Do you love me?')
    Do you love me?

    '''
    with open(filename,'a') as file:
        file.write(add)
    with open(filename,'r') as file:
        read=file.read()
    return read
