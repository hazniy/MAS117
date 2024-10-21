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
