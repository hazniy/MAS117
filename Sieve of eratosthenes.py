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
    
#sieve of eratosthenes : list all prime numbers 
prime = []
i = 2
n = int(input("enter a positive integer: ")) #25
while n < 0 : 
    n = int(input("enter a positive integer once again: "))
if n == 0 : 
    print("theres no prime number for", n)
else:
    numbers = list(range(2, n+1)) #[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    #if (2,n) itll be until 24 only!
    while i != n:
        num = numbers[i]
        newlist = list(range(i, i+2)) #how do i list all the multiple of 2
print(numbers)
print("\n There are", len(numbers), "prime numbers up to", n)




































n = int(input("Enter a positive integer: "))

# Step 1: Create a list of all numbers from 2 to n
numbers = list(range(2, n+1))

# Step 2: Implement the sieve algorithm
for i in range(2, int(n**0.5) + 1):
    if i in numbers:  # If i is still in the list, it is a prime
        # Remove multiples of i from the list (but not i itself)
        for multiple in range(i*2, n+1, i):
            if multiple in numbers:
                numbers.remove(multiple)

# Step 3: Print the remaining numbers (which are primes)
print("\nPrime numbers up to", n, "are:", numbers)
print("There are", len(numbers), "prime numbers up to", n)

# Define a function to check if a number is equal to the sum of the cubes of its digits
def is_sum_of_cubes(number):
    # Convert the number to a string to get each digit
    digits = [int(digit) for digit in str(number)]
    # Calculate the sum of the cubes of the digits
    sum_of_cubes = sum(digit ** 3 for digit in digits)
    return sum_of_cubes == number

# Find all numbers greater than 1 up to a reasonable limit
limit = 1000  # You can increase this limit if needed
results = []

for number in range(2, limit):
    if is_sum_of_cubes(number):
        results.append(number)

# Print the results
print("Numbers equal to the sum of the cubes of their digits:", results)


# Define a function to check if a number is equal to the sum of the cubes of its digits
def is_sum_of_cubes(number):
    # Convert the number to a string to get each digit
    digits = [int(digit) for digit in str(number)]
    # Calculate the sum of the cubes of the digits
    sum_of_cubes = sum(digit ** 3 for digit in digits)
    return sum_of_cubes == number

# Set a higher limit to find the numbers
limit = 10000  # Increased limit

# Find all numbers greater than 1 up to the limit
results = []

for number in range(2, limit):
    if
