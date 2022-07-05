# print("hello world")

# a = (4)
# b = (5)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)

#print('"hello"world')
#print("hello")
#print("world")

#define the values of different datatypes and checking its type.
#a=10
#b="Hi Python"
# c = 10.5
# print(type(a))
# print(type(b))
# print(type(c))

#example for, input from a consoler
#a= input()
#print(type(a))

#A program that takes a floating-point number as input and prints its integer part give input from console 
#a=float(input("A number is"))
#print(int(a))

#program that takes a integer as input and prints its floating-point number
#a = int(input("A number is"))
#print(float(a))

# program to check numbers are equal are not 
#a = int(input())
#b = int(input())
#print(a==b)

# program to check  a> b a greater then b 
#a = int(input())
#b = int(input())
#print(a>b)

# program to chgeck a lessthen b 
#a = int(input())
#b = int(input())
#print(a<b)

# program to a lessthe then are equal b
#a = int(input())
#b = int(input())
#print(a<=b)

 # program to check a greatthen b are  a equal b 
#a = int(input())
#b = int(input())
#print(a>=b)
 
 #program logical and operator
#a = 10
#b = 10
#c = 20
#if a > 0 and b > 0:
# print("true")
#if a > 0 and b > 0 and c < 0:
 #print("false")
#else:
 #print("true")
 
 #program to check AND operation try with diffrent examples
#a = 10
#b = 10
#c = 10
#if a and b and c:
 #print("All the numbers have boolean value as True")
#else:
 #print("Atleast one number has boolean value as False")
 
 
 #program to check OR operation try with different examples
#a = 10
#b = -10
#c = 0
#if a > 0 or b > 0:
# print("true")
#else:
 #print("false")
#if b > 0 or c > 0:
 #print("true")
#else:
 #print("false")
 
 # program to check not operator
#a = 10
#if not a:
 #print("Boolean value of a is True")
#3if not (a%3 == 0 or a%5 == 0):
 #print("true")
#else:
 #print("false")
 
 # IF STATEMENT AND LOOPS EXAMPLSE
#a = 33
#b = 200
#if b > a:
 #print("true")# (Indentation )wanted give sapce if not u  will get error
#else:
 #   print("false")
 
 # elif statement value of conditon is not true elif say try condition 
#a = 33
#b = 33
#if b > a:
 #print("true")
#elif a == b:
 #print("false")
 
#else statements example 
#a = 200
#b = 33
##if b > a:
# print("true")
#elif a == b:
 #print("true")
#else:
 #print("false")
 
 #Example of if...elif...else try more like 0,4.5,33 etc
#num = -4.5
#if num > 0:
 #    print("Positive number")
#elif num == 0:
 #print("Zero")
#else:
# print("Negative number")

#Python Nested if Example
#In this program, we input a numbercheck if the number is positive ornegative or zero and display
#num = float(input("Enter a number: "))
#if num >= 0:
# if num == 0:
#  print("Zero")
# else:
 # print("Positive number")
#else:
# print("Negative number")  

#Fizz-Buzz Program in Python
#a = int(input())

#if a%2 == 0 and a%5 == 0:
 #    print("fizzbuzz")   
#elif a%2 == 0:
 #    print("fizz")
#elif a%5 == 0:
 #    print("buzz")
#else:
 #    print(a)

# print hello  for n number times by giving input in console 
#n =int(input())
#for i in range(0,n,1):
#    print("hello")

# printing num from o to 5
#for i in range(6):
 #   print(i)

# first natural numbers
#for i in range(1,25,1):
 # print(i)
 
 #printing odd and even 
#for i in range(1,26,1):
 #   if i%2 ==0:
 #       print(i, "even")
#    else:
 #       print(i, "odd")
 
 # printimg * in colums number of rows
#rows = int(input("Enter the rows:"))
#for i in range(0,rows+1):
 #   for j in range(i):
 #    print("*",end = '')
#print()

#print natural numbers 
#number = int(input("Please Enter any Number: "))

#print("The List of Natural Numbers from 1 to {0} are".format(number)) 

#for i in range(1, number + 1):
 #   print (i, end = '  ')

 # sum n natural number 
#n = int(input("Please Enter any Number: "))
#total = 0

#for value in range(1, n + 1):
#    total = total + value

#print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(n, total))

 # printing sum of n natural numbers 
#n = int(input("please enter any number: "))
#sum = 0
#for i in range(1,n+1,1):
 #   sum = sum + i
 #   print(sum)
 
 # print cude and squre of numbers 
#n =int(input("please enter amy number: "))
#for i in range(0,n+1,1):
 #   print(" the number is ",i)
 #   print("square of the number is",i*i)
 #   print("qube of the number is",i*i*i)

# print total number of string letter in example
#n ="mariyamennen"
#count = 0
#for char in n:
 #   if char != "y":
 #       continue
 #   else:
 #       count = count + 1
 #       print("total numbert of y is:", count)
 
 # break loop exampole how to break loop fore given number is 15 
#n =[1,4,5,6,9,14,15,35,56,89]
#for i in n:
 #   if i>15:
 #       break
 #   else:
 #       print(i)
 # print product of first n natural nubers for given example

#n = int(input("please enter any number:"))
#product = 1
#for i in range(1,n+1,1):
 #   product = product*i;
 #   print(product)
 
 # print the first n natural numbers in reverse order 
#n =int(input("please enter any number:"))
#for i in range(n,0,-1):
 #   print(i)
 
 #printing the (enter 2 even numbers) odd number  in reverse order
#n =int(input("please enter any number:"))
#for i in range(16,0,-1):
 #   if i%3 ==0:
 #       print(i)
 
# print i as long as i is less than 6:
#i = -1
#while i < 6:
 #print(i)
 #i += 1
 
 # print the first n natural numbers useing while loop
#n =int(input("please enter any number:"))
#i = n
#while i > 1:
 #   i = i+1
#print(i)
# Program to illustrate
# the use of user-defined functions
##=def add_numbers(x,y):
 #sum = x + y
 #return sum
#num1 = 5
#num2 = 6
#print("The sum is", add_numbers(num1, num2))

#  add, sub, mult, divi useing methods  
#def addnumbers(a,b):
 #   print(a+b)
#addnumbers(1,2)

#useing methods

#def addnumbers(a,b,c):
#print(a,b,c)
#    print(a*b*c)  
#addnumbers(1,2,3)

#def add(x,y):
 #   return x + y
#def subtract(x, y):
 # return x - y
#def multiply(x, y):
 #  return x * y
#def divide(x, y):
 # return x / y
#print("Select operation.")
#print("1.Add")
#print("2.Subtract")
#print("3.Multiply")
#print("4.Divide")

# printing hello world multiple times
#n=int(input())
# for i in range(n):
# print('hello world')
#print('hello world\n'*n)


#Q3. Write a function which will take a str as input and will return a string where vowels are removed
# inputStr = ABCDEFG
# output Result = BCDFG
#string = "ABCDEFG"
#vowels = "AEIOU"
#result=" "
#for i in string:
 #if i in vowels:
 # continue
 #else:
 # result=result+i
#print(result, end =" ")


# 