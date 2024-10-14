"""
CP Class Assignment
"""
"""
Questions to be submitted by everyone 




Q - 7 start from notebooks..

Q - 1 Make a colums for
1)lists
2)tuples
3)strings
1.04)dictionary
Write their functions with meaning
"""

"""
# Q - 2 Make a program to find the sum of digits.

Num = int(input("Enter a number :"))
sum_of_digits = 0
while Num > 0:
    sum_of_digits += (Num % 10)
    Num = Num//10

print("Sum of Digits :" , sum_of_digits)
"""
"""
# Q - 3 Write a program to find the reverse of a number.


Num = int(input("Enter a number :"))
print(f"Reverse of {Num} is :",end = "")
while Num > 0:
    temp = Num % 10
    print(temp , end ="")
    Num = Num // 10
"""
"""
# Q - 4 Write a program to find whether a number is Armstrong or not.

def Armstrong():
    Sum = 0
    Num = int(input("Enter a number :"))
    TempNum = Num
    L = len(str(Num))
    while TempNum > 0:
        temp = TempNum % 10
        Sum += temp**L
        TempNum = TempNum // 10
    print(Num , "is an Armstrong Number .") if Sum == Num else print(Num , "is not an Armstrong Number .")

while True:
  Armstrong()
  Ask = input("Want to Check for another Number (Y/N): ")
  if Ask == "N":
    break
"""

"""
Q - 5 Write a program to find factorial of a number 
"""
"""
print("Calculating the Factorial of N   ")
Num = int(input('N = '))
c = 1
for i in range(1,Num+1):
  c = c*i 
print(Num,'! =',c)

"""

"""
Q - 6 Write a program to find the Fibonacci series
"""
"""
Num = int(input("Enter how many terms of the Fibonacci Series to be shown :"))
num1  = 0
num2  = 1
next_num = num2
print(num1)
for I in range(2 , Num + 1):
    print(next_num)
    num1 , num2 = num2 , next_num
    next_num = num1 + num2

"""

"""
def Fib(N):

    if N < 0:
        return 1

    elif N == 0:
        return 0

    elif N == 1 or N == 2:
        return 1

    else:
        a = Fib(N-1) + Fib(N-2)
        return a


N = int(input('Enter till which term to find :'))
for I in range(1 , N + 1 ):
  print(Fib(I)-Fib(I-2) , end = " ")

"""
"""
Q - 7
"""
"""
Dict = {}
for I in range(1 , 16):
    Dict[I] = I**2
print(Dict)
"""

'''
Q - 8
'''
"""
def Sum_of_Squares(Num):
  Num1 = str(Num)
  Sum = (int(Num1[0:2])**2) + (int(Num1[2:4])**2) 
  print('Sum of squares of first 2 digits and last 2 digits is',Sum)
Num = int(input('Enter a four digit number :'))
Sum_of_Squares(Num)
"""

"""
Q - 9
"""
"""
import random

states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

def quiz_user():
    correct_count = 0
    incorrect_count = 0
    states = list(states_and_capitals.keys())

    print("Welcome to the Indian States and Capitals Quiz!")
    print("Type 'exit' to end the quiz.\n")

    while True:
        state = random.choice(states)
        capital = states_and_capitals[state]
        states.remove(state)
        user_answer = input(f"What is the capital of {state} ? (or type exit if want to quit) : ")

        if user_answer.lower() == 'exit':
            break

        if (user_answer.strip()).title() == capital:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect! The correct answer is 
                  {capital}.")
            incorrect_count += 1

        print(f"Score: {correct_count} correct, {incorrect_count} incorrect\n")

    print("Quiz ended.")
    print(f"Total Questions Attempted {correct_count + incorrect_count}")
    print(f"Final data: {correct_count} correct, {incorrect_count} incorrect")
    print(f"Final data: {correct_count * 5 - incorrect_count*2} ")

print('Welcome to the Capital Quiz')
print('You will be given a state and you have to enter the capital of that state')
print('You will be given 10 questions')
print('Each correct answer will give you 5 points')
print('Each wrong answer will deduct 2 points.')
print('You can quit the quiz anytime by entering quit')
quiz_user()

"""
"""
Q - 10 
"""
"""
def Factorial(Num):
    print("Calculating the Factorial of N   ")
    c = 1
    for i in range(1,Num+1):
        c = c*i 
    print(Num,'! =',c)
    print(f'Checking if {Num} is Prime or Composite...')
    for num in range(2 , Num):
        if Num % num == 0:
            print(f"{Num} is a Composite Number .")
            break
        else:
            print(f"{Num} is a Prime Number .")
            break

Num = int(input('Enter N to calculate :'))
Factorial(Num)
"""

"""
Q - 11
"""
"""
def Sum_Avg(n):
  Sum = 0
  for i in range(n):
    Num = int(input('Enter a number :'))
    Sum = Sum + Num
  print('Sum :',Sum)
  print('Average :',Sum/n)
n = int(input('Enter how many numbers to be entered :'))
Sum_Avg(n)
"""
"""
Q - 12
"""
"""
def Change_Case(String):
  String = String.swapcase()
  print("The string after changing case is :")
  print(String)
String = input('Enter a string :')
Change_Case(String)
"""

"""
Q - 13
"""
"""
def Reverse(Num):
    while Num > 0:
        Digit = Num % 10
        print(Digit , end = "")
        Num //= 10
Num = int(input('Enter a number :'))
Reverse(Num)
"""

"""
Q - 14
"""
"""
def Count_Chars(String):
  Characters = 0
  Alphabets = 0
  Digits = 0
  Spaces = 0
  for i in String:
    if i.isalpha():
      Alphabets = Alphabets + 1
    elif i.isdigit():
      Digits = Digits + 1
    elif i.isspace():
      Spaces = Spaces + 1
    else:
      Characters = Characters + 1
  print(f"Characters : {Characters}")
  print(f"Alphabets  : {Alphabets}")
  print(f"Digits : {Digits}")
  print(f"Spaces : {Spaces}")
String = str(input("Enter a String of words :"))
Count_Chars(String)
"""

"""
Q - 15
"""
"""
from math import pi

def Cube(Side):
  print(f"TSA of cube    :{6*(Side**2)}") 
  print(f"Volume of cube :{Side**3}")

def Cuboid(L,B,H):
  print(f"TSA of cuboid   : {2*(L*B+B*H+H*L)}")
  print(f"Volume of cuboid: {L*B*H}")
def Sphere(Radius):
  print(f"TSA of sphere: {4*pi*Radius**2}")
  print(f"Volume of sphere : {(4*pi*Radius**3)/(3)}")
print('Enter 1 for Cube\nEnter 2 for Cuboid')
print('Enter 3 for Sphere')

while True:
  Choice = int(input('Enter your choice :'))
  if Choice == 1:
    Side = int(input('Enter the side of the cube :'))
    Cube(Side)
  elif Choice == 2:
    L = int(input('Enter the length of the cuboid :'))
    B = int(input('Enter the breadth of the cuboid :'))
    H = int(input('Enter the height of the cuboid :'))
    Cuboid(L,B,H)
  else:
    Radius = int(input('Enter the radius of the sphere :'))
    Sphere(Radius)
  Ask = input('Want to continue (Yes/No) :')
  if Ask.capitalize() == 'No':
    break
"""
