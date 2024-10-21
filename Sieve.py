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
