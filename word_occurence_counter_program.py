# Word Occurence Counter Function
def word_counter(s1,s2,word):
    ''' str,str,str --> int

    :param s1: String of the first statement
    :param s2: String of the second statement
    :param word: String of word to search
    :return: Returns the number of occurence of the searched word

    Example:
    >>> word_counter('Have you seen the file?', 'Yeah!, Have seen the mail','seen')
    2
    '''
    word_1=s1.split().count(word)
    word_2=s2.split().count(word)
    word = word_1+ word_2
    return word

'''
Prep for the function:
----------------------
import word_occurence_counter_program as wc
print(wc.word_counter('how have you been?', '', 'you'))
'''