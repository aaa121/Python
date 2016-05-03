# Letter/ Character Counter Program
def letter_counter(s1,s2,ch):
    ''' str,str,str --> int

    :param s1: String of the first statement
    :param s2: String of the second statement
    :param word: String of word to search
    :return: Returns the number of occurrence of the searched word

    Example:
    >>> letter_counter('Have you seen the file?', 'Yeah!, Have seen the mail','e')
    10
    '''
    L_1=len(s1)
    L_2=len(s2)
    count_1=0
    count_2=0
    for i in range(0,L_1,1):
        if ch == s1[i]:
            count_1 +=1
    count_1
    for h in range(0,L_2,1):
        if ch == s2[h]:
            count_2 +=1
    count_2
    return (count_1 + count_2)
'''
-----------------------------
Prep of import of the function:
------------------------------
import Letter_Counter_Program as lc
print(lc.letter_counter('Have you seen it?', 'Hope you are good?', 'y'))
'''

'''
--------------------
Alternative for Loop:
--------------------
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count
'''
