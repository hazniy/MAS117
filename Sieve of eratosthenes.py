#make half triangle 
for n in range(1, 6):
    for i in range(1, n+1):
        print(i, end="")
    print()
    
#third parameter of range 
for i in range(0, 101, 10):
    print("i =", i, " and i**2 =", i**2)
#i = 0  and i**2 = 0
#i = 10  and i**2 = 100
#i = 20  and i**2 = 400
#i = 30  and i**2 = 900
#i = 40  and i**2 = 1600
#i = 50  and i**2 = 2500
#i = 60  and i**2 = 3600
#i = 70  and i**2 = 4900
#i = 80  and i**2 = 6400
#i = 90  and i**2 = 8100
#i = 100  and i**2 = 10000

#list methods
menu = ["spam", "eggs", "bacon", "veg", "bacon"]
menu.remove("spam")
print(menu) #['eggs', 'bacon', 'veg', 'bacon']
menu.append("tomato")
print(menu) #['eggs', 'bacon', 'veg', 'bacon', 'tomato']
print(menu.index("eggs")) #0
print(menu.count("bacon")) #2
menu.insert(2, "bread") 
print(menu)#['eggs', 'bacon', 'bread', 'veg', 'bacon', 'tomato']
menu.reverse()
print(menu) #['tomato', 'bacon', 'veg', 'bread', 'bacon', 'eggs']

#print first letter for each day 
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday",
"Thursday", "Friday", "Saturday",
"Sunday"]
for day in DAYS_OF_WEEK:
    print("The first letter of ", day, " is ",
            day[0], ".", sep="")

#recap uses of list 
numbers = list(range(1,2)) #itll output [1]
numbers = list(range(1,4)) #itll output [1, 2, 3]
numbers = list(range(0,2)) #itll output [0, 1]
numbers = list(range(2,4)) #itll output [2, 3]
print(numbers)
print(len(numbers)) #itll print 2 bcs in the list only have 2 items

#how to list down multiple of a given number 
number = int(input("enter a number: "))
print("the multiples are: ")
for i in range(1,11): 
    print(number*i,  end = " ")

i = 0
newlist = []
prime = []
n = int(input("enter a positive integer: ")) 

while n < 0:
    n = int(input("enter a positive integer once again: "))
if n == 0:
    print("there's no prime number for", n)
else:
    # 1. list every num until n
    numbers = list(range(2, n + 1))  # [2,3,4,...,n]

    # 2. list multiples and mark non-primes
    while i < len(numbers):
        num = numbers[i]  # get the current base prime
        prime.append(num)  # store the first num since eg 2,3 are prime nums
        j = 2  
        multiple = 0

        while multiple <= n:
            multiple = num * j
            newlist.append(multiple)
            j = j + 1  # increment multiplier

        # 3. Remove multiples from `numbers`
        for val in newlist:
            if val in numbers:
                numbers.remove(val)  # remove each multiple from the main list

        i = i + 1  # move to the next number in `numbers`

    print(numbers)
    print("\nThere are", len(numbers), "prime numbers up to", n)
