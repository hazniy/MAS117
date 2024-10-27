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
j = 2  
multiple = 0
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
