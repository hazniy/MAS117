#A program to see if a number is odd or even
number = int(input("enter an integer: "))
if number % 2 == 1:
    print("That is odd...")
else:
    print("thats even")
print("thank you")

#indexing 
my_name = "Hazni"
index = 0
while index < len(my_name):
    print(index, my_name[index])
    index = index + 1

#exercise 3.3
# To find the middle of a string
string = input("Enter a string: ")
if len(string) % 2 == 1:
    print("The middle of the string is ",
            string[len(string) // 2], ".", sep="")
else:
    middle = len(string) // 2
    print("The middle of the string is ",
            string[middle - 1], string[middle], ".", sep="")
#"hazni" : z
#"hazniy" : zn

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
