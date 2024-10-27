i = 0
j = 2  
multiple = 0
newlist = []
prime = []
n = int(input("enter a positive integer: "))  # 25

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
        prime.append(num)  # store the first num since 2,3 are prime nums

        while multiple <= n:
            multiple = num * j
            newlist.append(multiple)
            j = j + 1  # increment multiplier

        # 3. Remove multiples from `numbers`
        for val in newlist:
            if val in numbers:
                numbers.remove(val)  # remove each multiple from the main list

        i = i + 1  # move to the next number in `numbers`

    print("Prime numbers up to", n, "are:", numbers)
