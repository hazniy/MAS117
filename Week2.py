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

#exercise 2.4 
number = int(input("enter a number: "))
if number == 0 :
    print("it is False that your number is non-zero")
else:
    print("it is True that your number is non-zero")
    
