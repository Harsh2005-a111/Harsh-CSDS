

# Name = input('Enter your name    :')
# Age =  int(input('Enter your age :'))
# print(Name,'is',Age,'years old .')

"""
import calendar

year  = int(input("Enter the Year         :"))
month = int(input("Enter the Month number (Between 1 and 12) :"))
Calendar = calendar.month(year , month) # prints the month of the year as displayed by user..
print(Calendar)
# print(calendar.calendar(year))
while True:
    Ask = input('Next/Previous/Exit(N/P/E) :')
    if Ask.capitalize() == 'N':
        month = (month+1)
        if month > 12:
            Calendar = calendar.month(year+1 , (month - 12))
            print(Calendar)
        else:
            Calendar = calendar.month(year , month) # prints the next month of the year as displayed by user..
            print(Calendar)
    elif Ask.capitalize() == 'P':
        month = (month-1)
        if month < 1 :
            Calendar = calendar.month(year-1 , (12 - month))
            print(Calendar)
        else: 
            Calendar = calendar.month(year , month) # prints the next month of the year as displayed by user..
            print(Calendar)
    else:
        print('Exiting...')
        break
"""
"""
import calendar
import datetime
year = datetime.datetime.now().year    # prints the current year 
month = datetime.datetime.now().month  # prints the current month 
print(calendar.month(year,month))
print(calendar.calendar(year))         # prints the current year calender
"""
"""
Write a program to read n number from user and find sum of its odd and even digits..
"""
"""

n = "x   "
Y = int(input('How many max stars do you want :'))
for I in range(Y):
    print(" "*((2*(Y-I))+1),n*(I+1))
for J in range(Y,0,-1):
    print(" "*((2*(Y-J))+5),n*(J-1))

print("")
"""

'''


Question 1
Write a program to calculate the area of circle given the radius

Question 2 
Perform basic arithmentic operations on two numbers

Question 3
Write a program to input three numbers and swap them

Question 4
Write a program to check the grades of a student as follows
90 - 100 = O
80 - 90 = A
70 - 80 = B
60 - 70 = C

'''
"""
# Question 2
print('Question 2')
Num1 = int(input('Enter Num1 :'))
Num2 = int(input('Enter Num2 :'))
Sum = Num1 + Num2
print("Sum :" , Sum)
Difference = Num1 - Num2
if Difference >= 0:
  print("Difference ",Difference)
else:
  print("Difference ",-Difference)
Product = Num1 * Num2
print("Product ",Product)
Division = Num1/Num2
print("Division (Num1/Num2):",Division)
print('')
# Question 3
print('Question 3')
Num1 = int(input('Enter Num1 :'))
Num2 = int(input('Enter Num2 :'))
Num3 = int(input('Enter Num3 :'))
temp = Num1
Num1 = Num2
Num2 = Num3
Num3 = temp
print('Num1 =',Num1)
print('Num2 =',Num2)
print('Num3 =',Num3)
print('')

# Question 4
print('Question 4')
Name = input('Enter your Name :')
print('')
Sub = ['English','Maths','Physics','Chemistry','Computer Science']
print("The Grade Table is as follows...\n")
print('90 - 100 = O\n')
print('80 - 90 = A\n')
print('70 - 80 = B\n')
print('60 - 70 = C\n')
Marks = {}
Grades = {}
for i in range(len(Sub)):
  print('Enter your marks in',Sub[i] )
  M = int(input(''))
  Marks[Sub[i]] = M
print("Student's Marks",Marks)
print('Grades')
for j in range(len(Sub)):
  if Marks[Sub[j]] >=90:
    Grades[Sub[j]] = 'O'
  elif Marks[Sub[j]] >=80 and Marks[Sub[j]] < 90:
    Grades[Sub[j]] = 'A'
  elif Marks[Sub[j]] >=70 and Marks[Sub[j]] < 80:
    Grades[Sub[j]] = 'B'
  else:
    Grades[Sub[j]] = 'C'
print(Grades)
print("Code execution run successfully")
"""
'''
num = int(input('Enter whose factorial to find :'))
c = 1
for i in range(1,num+1):
  c = c*i 
print(num,'! =',c)
'''
'''
p = int(input('Enter how many terms to print :'))
c1 , c2 = 0,1
print(c1)
for i in range(p):
  c1 , c2 = c2 , c1 + c2
  print(c2)
'''
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
'''
n = int(input('Enter how many rows to print :'))
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end = ' ')
  print()
'''

'''
print(sum(map(int, input().split())))
'''

'l = list(map(int,input().split()))'

'''
L1 = [1,2,3,4,5,6]
L2 = [6,7,8,9,10]
L3 = []
if len(L2)>=len(L1):
  for i in range(len(L1)):
    L3.append(L1[i]+L2[i])
  for j in range(len(L1),len(L2)):
    L3.append(L2[j])
else:
  for i in range(len(L2)):
    L3.append(L1[i]+L2[i])
  for j in range(len(L2),len(L1)):
    L3.append(L1[j])

print(L3)
'''
'''
L1 = list(map(int, input().split()))
sum = L1[0]
max = L1[0]
min = L1[0]
for i in L1[1:]:
  if i > max:
    max = i 
  if i < min:
    min = i
  sum = sum + i
print('Sum :',sum)
print('Max :',max)
print('Min :',min)
'''
'''
Questions to be submitted by everyone 
Q Write the difference between list , tuple , dictionary , strings  
Q-1 Write a program to find the sum of digits.
Q-2 Write a program to find the reverse of a number.
Q-3 Write a program to find whether a number is Armstrong or not.
Q-4 Write a program to find factorial of a number 
Q-5 Write a program to find the Fibonacci series
Q-6 Write a program to find an element in a list(Linear Search))
Q-7 Write a program to create a dictionary where values are the square of keys(taken in integer)
Q-8 
'''
'''
#Question 1
Int1 = int(input('Enter a number :'))
Sum = 0
for i in str(Int1):
  Sum = Sum + int(i)
print('Sum of digits of',Int1,':',Sum)

#Question 2
Int1 = int(input('Enter a number :'))
Int2 = Int1
Rev = 0
while Int2 > 0:
  Rem = Int2 % 10
  Rev = Rev * 10 + Rem
  Int2 = Int2 // 10
print('The number before reversed is :',Int1)
print('The number after reversed is :',Rev)
'''
'''
Q - Capital Quiz) Write a program that creates a dictionary containing the India states as keys
and their capitals as values. The program should then randomly quiz the user by displaying the name
of a state and asking the user to enter that state’s capital. The program should keep a count of the
number of correct and incorrect responses. using random function.
'''
"""



'''
In NoteBook (Handwritten)
Write a function to know if the given string is palindrome or not.(on paper)
'''

def Palindrome(String):
  if String == String[::-1]:
    print('The given string is a palindrome')
  else:
    print('The given string is not a palindrome')

String = str(input('Enter a string :'))
Palindrome(String)
print('******************************************************************')
'''
Write a function to find the factorial of a number
'''
Num = int(input('Enter a number :'))
c = 1
for i in range(1,Num+1):
  c = c*i
print('The Factorial of ',Num,'is',c)
print('******************************************************************')
'''

print('******************************************************************')


"""
'''
class Room:
  Length = 0
  Breadth = 0
  def calculate_area(self):
    print('Area :',self.Length*self.Breadth)
Room1 = Room()
'''
'''
Q - Write a program to create a class called Student with the following attributes:
1) Name
2) Roll No
3) Subject of Maths, Physics, Chemistry
'''
'''
class Student:
  L = []
  def __init__(self,Name,Roll_No,Maths,Physics,Chemistry):
    self.Name = Name
    self.Roll_No = Roll_No
    self.Maths = Maths
    self.Physics = Physics
    self.Chemistry = Chemistry
    L.append(self)
while True:
  N = input('Enter the name of Student :')
  R = int(input('Enter the roll number of Student :'))
  M = int(input('Enter the marks in Maths :'))
  P = int(input('Enter the marks in Physics :'))
  C = int(input('Enter the marks in Chemistry :'))
  S = Student(N,R,M,P,C)
  Ask = input('Want to enter more students :(Yes/No) :')
  if Ask.capitalize() == 'No':
    break

print(L)
'''

'''
from prettytable import PrettyTable 

class Student:
  def __init__(self,Name,Roll_No,Maths,Physics,Chemistry):
    self.Name = Name
    self.Roll_No = Roll_No
    self.Maths = Maths
    self.Physics = Physics
    self.Chemistry = Chemistry
    myTable.add_row([Name, Roll_No, Maths, Physics, Chemistry])

myTable = PrettyTable(["Student Name", "Roll No", "Marks in Maths", "Marks in Physics", 
                       "Marks in Chemistry"])
while True:
  N = input('Enter the name of Student :')
  R = str(input('Enter the roll number of Student :'))
  M = str(input('Enter the marks in Maths :'))
  P = str(input('Enter the marks in Physics :'))
  C = str(input('Enter the marks in Chemistry :'))
  S = Student(N,R,M,P,C)
  Ask = input('Want to enter more students :(Yes/No) :')
  if Ask.capitalize() == 'No':
    break
print(myTable)
'''
'''
class Area:
  def __init__(self,l,b):
    self.l = l
    self.b = b
  def display(self):
    print("The length is", self.l)
    print("The breadth is",self.b)
class Rectangle(Area):
  def ar(self):
    Rarea = self.l*self.b
    print("The area of a rectangle is",Rarea)

class Triangle(Area):
  def arr(self):
    Tarea = 0.5*self.l*self.b
    print("The area of triangle is",Tarea)
l = int(input('Enter length  :'))
b = int(input('Enter breadth :'))
obj = Area(l,b)
obj.display()
obj1 = Rectangle(l,b)
obj1.ar()
obj2 = Triangle(l,b)
obj2.arr()
'''
'''
Lamda Functions 
'''
#Syntax :
'''
lambda arguments : expression

def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

#convert the map into a list, for readability:
print(sum(x))
'''
'''
def myfunct(n):
  return n*n
x = map(myfunct, (1,2,3,4,5,6,7,8,9,10))
print(list(x))
'''
'''
#  Doubt

def fil(a):
  if a>5:
    return a
x = filter(fil,[1,2,3,4,5,6,7,8,9,10])
print(list(x))

def fill(a):
  if a>5:
    print(a)
x = filter(fill,[1,2,3,4,5,6,7,8,9,10])
print(list(x))
'''
'''
def is_possible(target):
  n = len(target)

  # Count the number of `1`s
  count_of_ones = target.count('1')

  # If the count of `1`s is odd, return "No"
  if count_of_ones % 2 != 0:
      return "No"

  # Find positions of `1`s
  ones_positions = [i for i, char in enumerate(target) if char == '1']

  # Try to pair `1`s
  painted = [False] * n
  pairs = 0

  for i in range(len(ones_positions)):
      if painted[ones_positions[i]]:
          continue
      found_pair = False
      for j in range(i + 1, len(ones_positions)):
          if not painted[ones_positions[j]] and abs(ones_positions[i] - ones_positions[j]) > 1 :
              painted[ones_positions[i]] = True
              painted[ones_positions[j]] = True
              pairs += 1
              found_pair = True
              break
      if not found_pair:
          return "No"

  return "Yes" if pairs * 2 == count_of_ones else "No"

# Example usage
print(is_possible("1001001"))  
print(is_possible("1100110"))  
'''
'''
# define a class
class Bike:
    name = ""
    gear = 0

# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")
'''
'''
class Student:

  Name = ""
  Grade = ""

S1 = Student()
S1.Name = "Harsh"
S1.Grade = "A"
S2 = Student()
S2.Name = "Saumya"
S2.Grade = "A+"
print(f"{S1.Name}  , Grade : {S1.Grade} ")
print(f"{S2.Name} , Grade : {S2.Grade}  ")
'''
'''
# Inheritance
# base class
class Animal:

    def eat(self):
        print( "I can eat!")

    def sleep(self):
        print("I can sleep!")

# derived class
class Dog(Animal):

    def bark(self):
        print("I can bark! Woof woof!!")

# Create object of the Dog class
dog1 = Dog()

# Calling members of the base class
dog1.eat()
dog1.sleep()

# Calling member of the derived class
dog1.bark()
'''


'''
# Encapsulation
class Computer:

    def __init__(self):
      self.__maxprice = 900

    def sell(self):
      print(f"Selling Price: {self.__maxprice}")

class Canva(Computer):
  def oprice(self, price):
    self.__maxprice = price
    print(f"Selling Price: {self.__maxprice}")

Caus = Canva()
Caus.sell()
Caus.oprice(11000)
'''
'''
# Encapsulation
class Computer:

    def __init__(self):
      self.__maxprice = 900

    def sell(self):
      print(f"Selling Price: {self.__maxprice}")

Caus =  Computer()
print(Caus._Computer__maxprice)
'''


'''

# Polymorphism
class Polygon:
  # method to render a shape
  def render(self):
      print("Rendering Polygon...")

class Square(Polygon):
  # renders Square
  def render(self):
      print("Rendering Square...")

class Circle(Polygon):
  # renders circle
  def render(self):
      print("Rendering Circle...")

# create an object of Square
s1 = Square()
s1.render()
# create an object of Circle
c1 = Circle()
c1.render()

'''
'''
# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print(f"Area of Room = { self.length * self.breadth }")

# create object of Room class
study_room = Room()

# assign values to all the properties 
study_room.length = 40
study_room.breadth = 30

# access method inside class
study_room.calculate_area()
'''
'''
# The normal way of using class and function
class Identity:
  def id(self, name = ""):
    self.name = name
    print(self.name)

bike1 = Identity()
bike1.id('Harsh')
'''
'''
# Using the __init__() function
class Identity:
  def __init__(self , name = ""):
    self.name = name
    print(self.name)

bike1 = Identity('Harsh')
bike2 = Identity('Saumya')

'''
'''
from abc import ABC, abstractmethod

class Animal(ABC):
  def sound(self):
    return 'HI'

class Dog(Animal):
  def sound(self):
    return 'Bark'
class Cat(Animal):
  def sound(self):
    return 'Meow'

animals = [Dog(),Cat()]
for animal in animals:
  print(animal.sound())
'''
'''
class Animal(object):
  def __init__(self, animal_type ):
    print('Animal Type:', animal_type)

class Mammal(Animal):
  def __init__(self):

    # call superclass
    super().__init__('Mammal')
    print('Mammals give birth directly')

dog = Mammal()

# Output: Animal Type: Mammal
#         Mammals give birth directly
'''
'''
add = lambda a,b : (a+b)
print(add(7,5))
'''
'''
def funct(a):
  return len(a)
L = list(map(funct, ('apple', 'banana', 'cherry')))
print(L)

def function(a):
  return len(a)
x = map(function, ('apple', 'banana', 'cherry'))
a = iter(x)
print(next(a))
print(next(a))
print(next(a))
'''
'''
L1 = list(map(int, input().split()))
'''
'''
fobj = filter(lambda x: 'r' in x , ['pears','guava', 'rotten tomato'])
for i in fobj:
  print(i)
'''
'''
from functools import reduce
L1 = list(map(int, input().split()))
print(reduce(lambda x,y : x+y, L1))
'''
'''
Method 1'''
'''
import functools
import operator
# initializing list
lis = [6, 3, 5, 2, 1]

# using reduce to compute maximum element from list
print("The sum of elements of list is : ", end="")
print(functools.reduce(operator.add, (lis)))

'''

'''
Method 2
'''
'''
import functools
import operator
# initializing list
lis = [6, 3, 5, 2, 1]

# using reduce to compute maximum element from list
print("The sum of elements of list is : ", end="")
print(functools.reduce(lambda a,b : a+b , lis))
'''
'''
string = 'abcdefg hijklmnop'
temp = string
for i in string.lower():
  if i in ['a','e','i','o','u']:
    string2 = temp.replace(i,'')
    temp = string2
print(temp)
print(string)

'''
"""
import numpy as np

print(np.__version__)

# Creating Arrays
# 1 D Array
arr = np.array([1,2,3,4,5])
print(arr)

print("********************************")

# 2 D Array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print("********************************")

 3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.



arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr3)

print("********************************")

print(arr.ndim , 'D')
print(arr2.ndim, 'D')
print(arr3.ndim, 'D')
# Accessing Arrays.. 

twodarr = np.array([[5,7,8],[9,10,45]])
print(twodarr)
print(twodarr.shape) # Two rows with 3 elements each... => Output (2,3)

"""
"""
import numpy as np

# print(np.__version__)

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr3)
print(arr3[0,1,2])

# Slicing
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr3)


# Adding to elements

import numpy as np

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr3)
print(arr3+5)

# To be Continued..
"""
"""

# Matplotlib

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0 , 5 , 6 ,  7])
ypoints = np.array([10, 5 , 8 , 14])

plt.plot(xpoints , ypoints)
plt.show()

xpoints = np.array([180,90,270]) 
Sum = 540
180/540  = 0.33
90/540 = 0.16
270/540 = 0.5

plt.pie(xpoints)
plt.show()

"""
# Pandas 
"""
import pandas as pd
a = [1 , 7 , 2]
myvar = pd.Series(a)
print(myvar)
"""

"""

import pandas as pd

data = {
  "calories":[430 , 380 , 390],
  "duration":[500 , 40 ,45]
}
myvar = pd.DataFrame(data)
print(myvar)

"""
"""
# To specify Index


import pandas as pd

data = {
  "calories":[430 , 380 , 390],
  "duration":[500 , 40 ,45]
}

myvar = pd.DataFrame(data)
# print(myvar)
# print(myvar[["calories"]])
# print(myvar.iloc[1])
print(myvar.iloc[ 0:3 , 0:1 ]) # Reading three row and one column.
"""
"""
import pandas as pd
index_labels = ["A" , "B" ]
indexclabel = ["Calo" , "Halo" , "Balo"]
myvar = pd.DataFrame ([
                     [430 , 380 , 390],
                     [500 , 40 ,45]]   ,
                     index  = index_labels , 
                     columns = indexclabel
                     )
print(myvar.info())
<<<<<<< HEAD
# Congratulations ! You have completed 1st Semester.
"""
"""

class ZeroBalanceError(Exception):
    pass

limit = 0

try:
    balance = int(input("Enter balance "))
    if balance < limit:
        raise ZeroBalanceError
    else:
        print("Balance is not zero.")
        
except ZeroBalanceError:
    print("Exception occurred: Balance less than or equal to zero.")
"""
'''
myfamily = {
  " Name1 " : {"First Name : "  : "Harsh",
               "Middle Name: " : "Raj"  ,
               "Last Name  : "   : "Srivastava"
             } ,
  " Name2 " : {"First Name : "  : "Saumya",
               "Last Name  : "   : "Srivastava"
              } ,
}
'''
'''
for I,J in myfamily.items():
  print(I)
  for K in J:
    print(K , J[K]) 
    
'''
'''
In the bustling city of Numerville, a young mathematician named Priya has always been fascinated by the world of numbers. One day, her mentor, Professor Rao, presented her with an intriguing challenge. The task was to find the smallest positive integer N such that the factorial of N (denoted as N!) is perfectly divisible by a given number K (where K≥2).

Professor Rao assured Priya that there was always a solution within the given constraints.

Input Format

The input is given from Standard Input in the following format:

K

Constraints

2≤K≤1012

K is an integer.

Output Format

Print the minimum positive integer N such that N! is a multiple of K.

Sample Input 0

30
Sample Output 0

5
Explanation 0

1!=1 2!=2×1=2 3!=3×2×1=6 4!=4×3×2×1=24 5!=5×4×3×2×1=120 Therefore, 5 is the minimum positive integer N such that N! is a multiple of 30. Thus, 5 should be printed.

Sample Input 1

123456789011
Sample Output 1

123456789011
Sample Input 2

280
Sample Output 2
'''
'''
class Student:
  def __init__(self , name , marks ):
    self.name  = name
    self.marks = marks
    
  def get_average(self):
    Sum = sum(self.marks)
    Num = len(self.marks)
    return f"The Average Marks scored by {self.name} is {Sum/Num} . "  

s1 = Student("Harsh" , [ 99 , 98 , 97 ])
print(s1.get_average())
s1.name = "Saumya" # Changing the name going inside the class.
print(s1.get_average())
'''

"""
Create Account Class with 2 attributes - balance and account no.
Create methods for debit credit and printing the balance...
"""
# class Account:
#   def __init__(self , balance , account_no ):
#     self.balance    = balance
#     self.account_no = account_no
  
#   def debit(self , debitamt):
#     self.balance -= debitamt
#     print(f"Rs.{debitamt} was  debited...")
  
#   def credit(self , creditamt):
#     self.balance += creditamt
#     print(f"Rs.{creditamt} was credited...")
    
#   def show(self):
#     return self.balance

# init_amt = int(input("Enter your initial amt in bank account :"))
# Acc = Account( init_amt , "H12401414")
# print(Acc.account_no)
# debitamt = int(input("Enter amt. to be debited (in Rupees) :"))
# Acc.debit(debitamt)
# print(f"Balance is now Rs.{Acc.show()}")
# creditamt = int(input("Enter amt. to be credited (in Rupees) :")) 
# Acc.credit(creditamt)
# print(f"Balance is now Rs.{Acc.show()}")

# class Person:
#   __name = "Anonymous"
  
#   def __hello(self):
#     print("Hello Person!")
  
#   def welcome(self):
#     self.__hello()

# p1 = Person()

# p1.welcome() 
"""
class Car :
  
  def __init__(self , type):
    self.type = type
    
  @staticmethod
  def start():
    return "car started..."
  
  @staticmethod 
  def stop():
    return "car stopped..."
    
class Lamborghini(Car):

  def __init__(self , name , type):
    self.name = name
    self.type = type # This implies that the type attribute changes inside
                     # the Lamborghini class and not the Car Class...

car1 = Lamborghini("Urus" , "xc1") 

print(car1.name , car1.type)
"""

"""
class Car :
  
  def __init__(self , type):
    self.type = type
    
  @staticmethod
  def start():
    return "car started..."
  
  @staticmethod 
  def stop():
    return "car stopped..."
    
class Lamborghini(Car):

  def __init__(self , name , type):
    self.name = name
    super().__init__(type)

car1 = Lamborghini("Urus" , "xc1") 

print(car1.name , car1.type)
"""
"""
class Person:
  name = "anonymous"
  
  def change(self , name):
    self.name = name # This name is not same as class 'name'.
                     # We cannot change this 'name' using object 'name'.
                     # The object 'name' is created independently.
                     
p1 = Person()
print(p1.name)

p2 = Person()
p2.change("Harsh")
print(p2.name) 

p1 = Person()
print(p1.name) # No change observed...

"""
"""
# Changing the class attribute 'name'.

class Person:
  name = "anonymous"
  
  def change(self , name):  # Method 1 
    self.__class__.name = name
  
  @classmethod
  def change(cls , name):    # Method 2
    cls.name = name
    print("Hi")

p1 = Person()
p1.change("Harsh") # Output : Hi
print(p1.name)     # Output : Harsh
"""

# Changing the percentage when changing the marks...
# Method 1 ==>

"""
class Student:
    def __init__(self , phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math

    
    def calc(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3)

stud1 = Student(98 , 97 , 99)

stud1.calc()

stud1.phy = 89
stud1.calc()
print(stud1.percentage)
"""

# Method 2 ==>
"""
class Student:
  def __init__(self , phy , chem , math):
    self.phy = phy
    self.chem = chem
    self.math = math

  @property  
  def calc(self):
    print(str((self.phy + self.chem + self.math) / 3))

stud1 = Student(98 , 97 , 99)
(stud1.calc)
stud1.phy = 89
(stud1.calc)
"""

"""
class Complex:
    def __init__(self , real , img):
        self.real = real
        self.img = img
        
    def show(self):
        print(f"{self.real} + {self.img} j")
    
    def __add__(self , num2):
        NewReal = self.real + num2.real
        NewImg  = self.img + num2.img
        return Complex(NewReal , NewImg)
    
    def __sub__(self , num2):
        NewReal = self.real - num2.real
        NewImg  = self.img - num2.img
        return Complex(NewReal , NewImg)

num1 = Complex(1 , 3)
num1.show()

num2 = Complex(5 , 4)
num2.show()

num3 = num1 + num2
num3.show()

num4 = num2 - num1
num4.show()
"""

# class Circle:
  
#   def __init__(self , radius):
#     self.r = radius
    
#   def Area(self):
#     return f"Area of Circle is {(22/7)*self.r**2} ."
    
#   def Perimeter(self):
#     return f"Perimeter of Circle is {2*(22/7)*self.r} ."
    
# C = Circle(7)
# print("Radius : " , C.r)
# print(f"{C.Area()}\n{C.Perimeter()}")

"""
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role   : ", self.role)
        print("Dept   : ", self.dept)
        print("Salary : ", self.salary)
  

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,00,000")
    
    def show(self):
        print("Name   : ", self.name)
        print("Age    : ", self.age)
        super().showDetails()
        
E = Engineer("Harsh", 19)

E.show()
"""
"""
import getpass
 
p = getpass.getpass(prompt='Your favorite flower? ')
 
if p.lower() == 'rose':
    print('Welcome..!!!')
else:
    print('The answer entered by you is incorrect..!!!')
"""
"""
x = 1

if type(x) == int:
  raise TypeError("Only integers are allowed")
print(x)
"""
"""
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy","H"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, 
# a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(" ; ", " = ")))
"""
"""
import re

#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search("S", txt)
print(x.group())
"""
"""
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in input_string if char not in vowels)
    return result

# Example usage
text = "Hello, how are you?"
print(remove_vowels(text))  # Output: "Hll, hw r y?"
"""
# def myfunct(*kids):

#   print(f"The Youngest Kid is {kids[2]}")

# myfunct("Emil","Harsh","Zoya")
# # Order Matters....

# def myfunct(**kid):

#   print("The Eldest Child is " + kid["child1"] )

# myfunct(child = "Harsh" , child1 = "Saumya")

# class Student :
  
#   def college(self):

#     print('A college')

# s1 = Student()
# s1.college()


# class Base:

#     def __init__(self, name, roll, role):

#         self.name = name
#         self.roll = roll
#         self.role = role

# class Intermediate(Base):

#     def __init__(self, age, name, roll, role):

#         super().__init__(name, roll, role)
#         self.age = age

# class Derived(Intermediate):

#     def __init__(self, age, name, roll, role):

#         super().__init__(age, name, roll, role)

#     def Print_Data(self):

#         print(f"The Name is : {self.name}")
#         print(f"The Age is : {self.age}")
#         print(f"The role is : {self.role}")
#         print(f"The Roll is : {self.roll}")

# # Creating Object of Base Class
# obj = Derived(21, "Lokesh Singh", 25, "Software Trainer")
# # Printing the data with the help of derived class
# obj.Print_Data()

"""
# Using Lambda Map Filter combined in the code...

numbers = [1, 2, 3, 4, 5, 6]

square = lambda x: x ** 2

squared_numbers = (map(square, numbers))

even_squared = filter(lambda x: x % 2 == 0, squared_numbers)

print(list(even_squared))
"""
# # Program to count the number of 1s in the binary representation of a number
# try:
#     # Get input from the user
#     num = int(input("Enter an integer: "))
    
#     # Convert the number to binary and count the '1's
#     binary_representation = bin(num)  # Get the binary representation (e.g., '0b101')
#     count_of_ones = binary_representation.count('1')
    
#     # Display results
#     print(f"The binary representation of {num} is {binary_representation[2:]}.")
#     print(f"The number of 1s in the binary representation is {count_of_ones}.")
# except ValueError:
#     print("Please enter a valid integer.")
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print("Mean:", np.mean(arr))
# print("Standard Deviation:", np.std(arr))
# print("Sine values:", np.sin(arr))
"""
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 15 , side = "right")

print(x)
"""
