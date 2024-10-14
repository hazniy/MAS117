#python variable types 
approximation = 175.38
print(type(approximation)) #type to find out type of variable 
secret_password = "dead parrot"
print(type(secret_password))

#integer type 
a = 7
b = 2
print('product', a * b, 'sum', a + b, 'subtract', a - b, 'negative', -a, 'power of', a**b)
print(max(a, b), min(a, b)) #max and min
print("7/3 is", 7 // 3, "with remainder", 7 % 3) #integer division // & remainder %

#exercise 2.1
#How many digits are there in 2^100?
formula1 = 2**100 
print ("there are", len(str(formula1)))

#What is the remainder when 3^11 is divided by 11?
formula2 = (3**11)//11 
print(formula2) 

#floating point type 
a = 7.2
b = 2.5
print('product', a * b, 'sum', a + b,'subtract', a - b, 'negative', -a, 'power of' ,a**b)
print(max(a, b), min(a,b))

#turn float into integer
a = 3
b = float(a)
c = int(b)
print(a, b, c)
print(int(5.2), int(5.99))

#exercise 2.2 
#How can you tell from the output that b is a float and not an integer? theres a point
#How does int() round a number? Does it round down? Round up? round down 
a = -7.8 
b = int(a) 
print(b)

#exercise 2.3 (BMI program) 
height = float(input("enter your height in metres "))
weight = float(input("enter your weight in kilogram "))
BMI = weight/height**2
print("%.1f"% BMI) #round of to 1 place 

#exercise 2.4 Write a short program that inputs an integer and prints either “It is True that your number is non-zero” or “It is False that your number is non-zero”, whichever is correct.
number = int(input("enter a number: "))
if number == 0 :
    print("it is False that your number is non-zero")
else:
    print("it is True that your number is non-zero")
    
#exercise 2.5
while 1 > 2:
    print("Spam")
    print("Spam and eggs")
print("Lobster thermidor")
#1 < 2 : itll produce infinite loop which itll keepp looping since 1 is less than 2
#1 > 2 : itll output lobster thermidor since 1 is not more than 2, so itll execute the loop

#homework
#(i) 
print(type(3.1415))
#(ii) x > = y
#(iii) 
print((3 < 2) or (10 == 5)) #false
#(iv)
total = 0
i = 10
while i > 5:
    total = total + i**2
    print(i, total)
    i = i - 2
print("We finished with i =", i)

#3 GCD
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
while num1 != num2:
    if num1 > num2:
        num1 = num1 - num2

    else:
        num2 = num2 - num1
print("the greatest common divisor for these 2 numbers is", num1)

#by hand: can use LCM method
#9 and 12 output 3
#17 and 17 output 17
#21 and 22 output 1
#221 and 289 output 17

#alternative : (it says that we need to replace the num1 and num2 with min val and absolute) 
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
while num1 != num2:
    num1, num2 = min(num1,num2), abs(num2-num1)
print("the greatest common divisor for these 2 numbers is", num1)

#4 how to find a pi using 10 iterations 
import math


def gauss_legendre_pi(precision=10):
    # Step 1: Initialize variables
    a_n = 1.0
    b_n = 1.0 / math.sqrt(2)
    t_n = 1.0 / 4.0
    p_n = 1.0

    for _ in range(precision):
        # Step 2: Update variables
        a_next = (a_n + b_n) / 2.0
        b_next = math.sqrt(a_n * b_n)
        t_next = t_n - p_n * (a_n - a_next) ** 2
        p_next = 2 * p_n

        # Move to the next iteration
        a_n = a_next
        b_n = b_next
        t_n = t_next
        p_n = p_next

    # Step 3: Calculate pi approximation
    pi_approx = (a_n + b_n) ** 2 / (4 * t_n)

    return pi_approx


# Testing the function with a precision of 10 iterations
pi_approximation = gauss_legendre_pi(10)
print(f"Approximation of π after 10 iterations: {pi_approximation}")
