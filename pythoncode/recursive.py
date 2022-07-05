
  #  """This is a recursive function
 #to find the factorial of an integer"""
 
#def factorial(x):
 # if x == 1:
#    return 1
 # else:
 #     return(x* factorial(x-1))
#num = 3
#print("the factorialof",num,"is", factorial(num))

#factorial(3) # 1st call with 3
#3 * factorial(2) # 2nd call with 2
#3 * 2 * factorial(1) # 3rd call with 1
#3 * 2 * 1 # return from 3rd call as number=1
#3 * 2 # return from 2nd call
#6 # return from 1st call

# print sum of all elements useing recursive
#def arraysum(A, n):
 #   if n == 1:
 #       return  A[n-1]
 #   return arraysum(A,n-1)+A[n-1]
#A = list(int,(input().split()))
#print(arraysum(A,len(A)))


#Write a method that reverse a string recursively.
#def reverse(string):
 #  if len(string) == 0:
  #  return string
  # else:
   # return reverse(string[1:]) + string[0]
#a = str(input("Enter the string to be reversed: "))
#print(reverse(a))


#Febonacci series problem using recursion:
#def fibonacci(n):
  #if n==1:
   #return 0
  #if n==2:
#return 1
#fibx = fibonacci(n-1)
  #fiby = fibonacci(n-2)
  #return fibx + fiby
#n = int(input(" 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,"))
#print(fibonacci(n))  

#stair case problem using recursive:
#def Nthstair(curr,n):
  # if curr==n:
  #  return 1
  # if curr>n:
#return 0
 #  numofways1 = Nthstair(curr+1, n)
 #  numofways2 = Nthstair(curr+2, n)
 #  numofways3 = Nthstair(curr+3, n)
 #  return numofways1+numofways2+numofways3
#n = int(input())
#print(Nthstair(0,n))


# python 3 program for the above approach
#
# Function to find the minimum number
# of flips to make all three pairs of
# consecutive characters different






                
                  
