#exercise 1.4 triangular program 
n = int(input("Enter the number you want "
"to calculate the triangular of: "))
i = 1
while i <= n:
    triangular = i*(i+1)/2
    i = i + 1
print(triangular)

#simpler way 
n = int(input("Enter the number you want "
"to calculate the triangular of: "))

triangular = n*(n+1)/2
print(triangular)

#first homework MAS 117
#3
x = 13
y = 21
x = y + 10
y = x + 10 
print("x = ", x, "and y = ", y)

x = 13 
y = 21
x, y = y +10, x+10 
print("x = ", x, "and y = ", y)

#4 triangular number program (recursion)
n = int(input("enter a number: "))
reciprocal = 0
i = 1

if n == 0: 
    print("maths error bruh")
else: 
    while i <= n: 
        formula = 1/(i**2)
        reciprocal = reciprocal + formula
        i = i + 1
    print(reciprocal) 
