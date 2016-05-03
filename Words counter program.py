# Words Counter Program
# It counts the number of words in a particular statement.
docfile=input("Paste the statement here:")
words=str.split(docfile)
words_count=len(words)
print(words_count)
print(words)
#count the frequency of occurence for a particluar word say: "the"
word_search=input("Input the word to search its frequency here (Note: Do not use quote): ")
word_frequency=str.count(docfile,word_search)
print(word_frequency)

'''
The aim of this paper is to examine the difference between environmentally labelled and non-environmentally labelled products available on the New Zealand building market. It seeks to enhance an understanding of product values realized through an adoption of voluntary eco-labelling schemes amongst paints, carpets and building insulation. This study delivers comparative analysis of key product attributes identified as performance, retail price, and environmental attributes comprising of volatile organic compounds (VOC) emissions, recycled content, hazardous substances, waste and energy management. Results suggest that the selected eco-labelled products are competitive with their non-labelled counterparts in terms of performance and retail value. This is particularly true for carpets and building insulation. Non-eco-labelled paints are, however, offered at lower prices despite comparable performance to eco-labelled paints. In addition, this study identifies that the eco-labelled products provide more coherent, comprehensive and accessible information to retail customers than non-eco-labelled products.

'''
docfile=input("Paste the statement here:")
words=docfile.split()
words_count=len(words)
print(words_count)
print(words)
#count the frequency of occurence for a particluar word say: "the"
word_search=input("Input the word to search its frequency here (Note: Do not use quote): ")
word_frequency=str.count(docfile,word_search)
print(word_frequency)