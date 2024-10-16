"""
CP Lab Assignment
"""
"""

#1 Write a python program to copy a list

print('Answer 1')
List = []
while True:
  A = str(input("Enter a content(numbers/characters): "))
  List.append(A)
  Ask = str(input('Want to Enter more content (Yes/No) :'))
  if Ask.capitalize() == 'No':
    break
print('List ', List)

CopyList = []
for i in range(len(List)):
  CopyList.append(List[i])
print('CopyList ', CopyList)
print('')
print('*************************************************************************************')

#2 write a program that take two list and return True if they have atleast 1 common member

# 2
print('Answer 2')
List1 = []
List2 = []
while True:
  A = str(input("Enter a content(numbers/characters): "))
  List1.append(A)
  Ask = str(input('Want to Enter more content (Yes/No) :'))
  if Ask.capitalize() == 'No':
    break
print('List1 ', List1)
while True:
  A = str(input("Enter a content(numbers/characters): "))
  List2.append(A)
  Ask = str(input('Want to Enter more content (Yes/No) :'))
  if Ask.capitalize() == 'No':
    break
print('List2 ', List2)
if len(List1) >= len(List2):
  for i in range(len(List1)):
    for j in range(len(List2)):
      if List1[i] == List2[j]:
        print('True')
else:
  for i in range(len(List2)):
    for j in range(len(List1)):
      if List2[i] == List1[j]:
        print('True')
print('')
print('*************************************************************************************')
"""

"""
Q - 3
"""
"""
print('Answer 3')
dict1 = {1 : 10 , 2: 20}
dict2 = {3 : 30 , 4: 40}
dict3 = {5 : 50 , 6: 60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)
print('')
print('******************************************************************')
"""

"""
Q - 4
"""

"""
print('Answer 4')
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
sumkeys = 0
sumvalues = 0
for i in dict1.values():
    sumvalues += i 
for j in dict1.keys():
    sumkeys += j
print(sumkeys , sumvalues)
print('')
print('******************************************************************')

"""
"""
Q - 5
"""
"""
print('Answer 5')
def Palindrome(String):
  if (String).lower() == (String[::-1]).lower():
    print('The given string is a palindrome .')
  else:
    print('The given string is not a palindrome .')

String = str(input('Enter a string : '))
Palindrome(String)
print('')
print('******************************************************************')
"""

"""
Q - 6
"""
"""
print('Answer 6')
"""
"""
Q - 7
"""
"""
print('Answer 7')
def Palindrome(String):
  if (String).lower() == (String[::-1]).lower():
    print('The given string is a palindrome .')
  else:
    print('The given string is not a palindrome .')

def Length(String):
  print("Length of String :", len(String))

def Reverse(String):
  print("Reverse of ", String , "is ",String[::-1]) 


String = str(input('Enter a string : '))
while True :
  print(" Palindrome (P) "," Length (L) "," Reverse(R) " )
  Ask = input('Choose any of the above functional alphabets :')
  if Ask == " P ":
    Palindrome()
  elif Ask == " L ":
    Length()
  elif Ask == " R ":
    Reverse() 
  else:
    break
"""


"""
Q - 8
"""

"""
print('Answer 8')
Num = int(input('Enter The Number whose Table is to be shown :'))
Multiplier = int(input("Enter upto which number the table to be printed :"))
for I in range(1,Multiplier + 1):
  print(Num , "x", I , "=", Num*I)
"""

"""
Q - 9
"""
''' 
   *
  * *
* * * *
* * * *

'''
"""
print('Answer 9')
print('Pattern Character :', '*')
for i in range(4):
    if i == 2:
        print(' '*(2-i),'* '*(i+2))
    else:
        print(' '*(3-i),'* '*(i+1)) 
print('')   
print('******************************************************************')

"""
"""
Q - 10
"""
"""
import string

print('Answer 10 ')
A = str(input('Enter a string:'))
for punctuation in string.punctuation:
  A = A.replace(punctuation,'')
X = A.split()
print(X)
B = str(input('Enter a word to search:'))
for i in range(len(X)):
  if X[i] == B:
    print('Found')
    break
print('')
print('******************************************************************')

"""
"""
Q - 11
"""

''' 
*
**
***
****
*****
******
*******
'''
"""
print('Question 11')
print('Pattern Character :', '*')
A = int(input('Enter till how many lines the pattern has to run:'))
for i in range(A):
  for j in range(i + 1):
    print('*', end='')
  print('')
print('')
print('******************************************************************')
"""

"""
Q - 12
"""

''' 
1
2 2
3 3 3
4 4 4 4 
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9
'''

"""
print('Answer 12 ')
for i in range( 1 , 10 ):
  for j in range( 1 , i + 1):
    print(str(i),end = " ")
  print('')

print('')
print('******************************************************************')

"""

"""
Q - 13
"""

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 10
'''
"""
print('Answer 13 ')
for i in range( 1 , 10 ):
  for j in range( 1 , i + 1):
    print(str(j),end = " ")
  print('')

print('')
print('******************************************************************')
"""

"""
Q - 14
"""

'''
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 
4 4 4 4 4 4 4 
5 5 5 5 5 5 
6 6 6 6 6 
7 7 7 7 
8 8 8 
9 9 
10
'''
"""
print('Answer 14 ')
for i in range( 10 , 0 , -1):
  for j in range( 1 , i + 1):
    print(str(11-i),end = " ")
  print('')

print('')
print('******************************************************************')
"""

"""
Q - 15
"""

'''
EEEEE
 DDDD
  CCC
   BB 
    A
'''
"""
print('Answer 15 ')
for i in range( 69, 64 , -1):
    print(" "*(69-i) , end = '')
    for j in range( 1 , (i-63) ,  1):
        print(chr(i) , end = "")
    print('')

print('')
print('******************************************************************')

"""
"""
Q - 16 
"""
"""
print('Answer 16')
List1 = [ 91 , 54 , 24 , 56 , 45 , 36 , 23 , 98 , 65 ]
sumvalues = 0
for i in List1:
    sumvalues += i 
print("Sum of values in a List :" , sumvalues)
print('')
print('******************************************************************')
"""

"""
Q - 17 
"""
"""
print('Answer 17')
List1 = [ 91 , 54 , 24 , 56 , 45 , 36 , 23 , 98 , 65 ]
numlargest = List1[0]
for num in List1:
    if numlargest <  num :
      numlargest = num  
print("Largest number stored in a List :" , numlargest)
print('')
print('******************************************************************')
"""

"""
Q - 18 
"""
"""
print("Answer 18")
List1 = []
while True:
    str = input("Enter a string (or type 'exit' to stop): ")
    if str.lower() == 'exit':
        break
    if len(str) >= 2:
        List1.append(str)
    else:
        print('Length of string must be more than 2.')
print("\nYou entered the following strings in the List : ")
print(List1)
count = 0
for char in List1:
    if char[0:1] == char[(len(char)-1):(len(char)-2):-1]:
        count += 1
print("Result :", count)

print('')
print('******************************************************************')

"""
"""
Q - 19 
"""
"""
List1 = [ 10 , 30 , 80 , 97 , 65 , 43 , 89 , 97 , 10 , 80]
List2 = List1.copy()
temp  = List1.copy()
for I in List2:
    temp.remove(I)
    if I in temp:
        List1.remove(I)
print(List1)

print('')
print('******************************************************************')
"""

"""
Q - 20 
"""
"""
List1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
temp  = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for I in range(len(List1)):
   if str(I) in '045':
      List1.remove(temp[I])
print(List1)

"""
"""
Q - 21 
"""
"""
print('Answer 21')
dict1 = {1 : 10 , 2: 20}
dict2 = {3 : 30 , 4: 40}
dict3 = {5 : 50 , 6: 60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)
print('')
print('******************************************************************')

"""
"""
Q - 22 
"""

"""
print('Answer 22')
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
sumkeys = 0
sumvalues = 0
for i in dict1.values():
    sumvalues += i 
for j in dict1.keys():
    sumkeys += j
print(sumkeys , sumvalues)
print('')
print('******************************************************************')
"""


"""
Q - 23 
"""
"""
print('Answer 23')

dict = {6: 10, 4: 20, 8: 30, 7: 40, 1: 50, 5: 60}
K = dict.keys()
K.sort()
print(K)
dict2={}
for i in K:
    dict2[i] = dict[i]
print(dict2)
print('')
print('******************************************************************')
"""
"""
Q - 24
"""
"""
print('Answer 24')
dict = {1: 50, 4: 20, 5: 60, 6: 10, 7: 40, 8: 30}
M = max(dict.values())
m = min(dict.values())
print("Max : ", M , "Min : ", m)
print('')
print('******************************************************************')
"""
"""
Q - 25
"""
"""
print('Answer 25')
List = [(10,20,40),(40,50,60),(70,80,90)]
List2 = []
for I in List :
    J = list(I)
    J[2] = 100
    K = tuple(J)
    List2.append(K)
print(List2)
print('')
print('******************************************************************')
"""

"""
26. Write a Python function to sum all the numbers in a list. 
Sample List : [8, 2, 3, 0, 7]
Expected Output : 20
"""
"""
print('Answer 26')
List = []
Sum = 0
while True :
  Input = int(input("Enter a number : "))
  List.append(Input)
  Sum += Input
  Ask = input("Want to Enter more Data (Y/N) :")
  if Ask.upper() == "N":
    break
print(List)
print("Sum of All Numbers in List : " , Sum)
print('')
print('******************************************************************')
"""

"""
27. Write a Python program that accepts a word from the user and reverses it,     using a loop 
"""
"""
print("Answer 27")
while True :
  Str = str(input("Enter a word : "))
  for I in Str[::-1]:
    print(I,end = '')
  print("")
  Ask = input("Want to Enter another Word (Y/N): ")
  if Ask == "N":
      break
"""

"""
28. Write a Pandas program to create a dataframe from a dictionary and display
    it.
"""