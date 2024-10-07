#python variable types 
approximation = 175.38
type(approximation) #type to find out type of variable 
secret_password = "dead parrot"
type(secret_password)

#integer type 
a = 7
b = 2
print(a * b, a + b, a - b, -a, a**b)
print(max(a, b), min(a, b)) #max and min
print("7/3 is", 7 // 3, "with remainder", 7 % 3) #integer division // & remainder %

#exercise 2.1
#How many digits are there in 2^100?
formula1 = 2**100 
print ("there are", len(formula1))

#What is the remainder when 3^11 is divided by 11?
formula2 = (3**11)//11 
print(formula2) 

#floating point type 
a = 7.2
b = 2.5
print(a * b, a + b, a - b, -a, a**b)
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

#celcius to fahrenheit 
temperature_in_C = float(input("Temperature in Celsius: "))
temperature_in_F = correct_expression
print("Temperature in Fahrenheit is", temperature_in_F)
#try input 37C 

#exercise 2.3 (BMI program) 
height = input(float("enter your height in metres"))
          
               
