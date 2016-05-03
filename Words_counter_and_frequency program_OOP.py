# Object Oriented Program
# Word(s) Counter and Frequency Program

docfile=input("Enter the statements or group of words here:")
words=docfile.split()
words_counter=len(words)
print(words_counter)
word_search=input("Enter the word to search and count its frequency here:")
word_frequency=docfile.count(word_search)
print(word_frequency)
