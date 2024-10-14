#recap how to print 1 letter only : 
str1 = "hazni"
print (str1[1]) #it'll print 'a'

#hamming distance : between 2 words of same size and total of diff words
str1 = str(input("enter the first string: "))
str2 = str(input("enter the second string: "))
i = 0 
hamming = 0
while len(str1) != len(str2): 
    str1 = str(input("bro please insert the first string: "))
    str2 = str(input("insert the second string SAME LENGTH with first string la bro:  "))
while i != len(str1): 
    letter1 = str1[i]
    letter2 = str2[i]
    if letter1 != letter2 : 
        hamming = hamming + 1
    i = i + 1
print (hamming)

#what if its not the same length

#what if its not the same length
str1 = str(input("enter the first string: "))
str2 = str(input("enter the second string: "))
i = 0 
hamming = 0
while len(str1) != len(str2): 
    if len(str1) > len(str2): 
        str2 = str2 + " "
    else: 
        str1 = str1 + " "
while i != len(str1) : #since str1 and str2 have the same length so it doesnt matter 
    letter1 = str1[i]
    letter2 = str2[i]
    if letter1 != letter2 : 
        hamming = hamming + 1
    i = i + 1
print (hamming)
