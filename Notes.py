'''
    Lesson: Variables and Data Types
    Author: Mr. Kalisz
    Date Created: Sept 16, 2024
    Date Last Modified: Spet 16, 2024
'''

#Assignment statment
#Assigning the value on the right to the value on the left

#Integers

num = 90

#Float - decimal fractions

fracNum = 1.5

#String

word = "Hello there"

#Boolean

tOrF = True


#Variable Call
#Replace the variable with the value it current has stored
#applies any time the variable is NOT on the left of an assignment symbol

print(num)
#print(90)

print(num + 5)

#Operations

#Addition (+)

#Overwrite num
num = 5 + 7
print(num) #Uses the most recent value of num

#Right side ALWAYS comes first
num = num + 3

print(num + 3.0)

#Subtraction (-)

num = num - 2
print(num)

#Multiplication (*)

print(num * 3) #13*3
print(num * 10) #13*10

#For addition, multiplication and subtraction when a float is used, the result is a float
#When two integers are used, the result is an integer

#Division (/)

#The result is always a float

num = 36
print(num / 3) #12.0

#Integer Division or Floor Division (//)

#Rounds down the result to the nearest whole number
#You always get an integer
#Converts the float result to an integer by removing the decimal point and everything after it

print(num // 10) #3

#Mod (%) - Gives the remainder to a divisoin question where it treads the % as a /

print(num % 10) #6

print(num % 5) #1