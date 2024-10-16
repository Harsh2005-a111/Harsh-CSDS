
/*
#include <iostream>
using namespace std;

int main() {
  cout << "Swap the values of two variables" << '\n';
  int a = 1;
  int b = 2;
  int temp = a;
  a = b;
  b = temp;
  cout << a << '\n';
  cout << b;
}
*/
// *****************************************************************//
/*

#include <iostream>
using namespace std;
int main() {
  int file_size = 100;
  cout << file_size << '\n';
  int sales = 10;
  cout << sales;
  return 0;
}
*/
//*****************************************************************//

/*
#include <iostream>
int main() {
  const double pi = 3.14;
  int radius = 10;
  int area = pi*radius*radius;
  std::cout << area;
    }
*/
// *****************************************************************//
/*
int file_size; Snake case - separating multiple words with an underscore.
int FileSize; Pascal Case - without underscore and each word is capatilized.
int fileSize; Camel Case - Each word, except the first, starts with a capital letter.
int iFileSize; Hungarian Notation - first letter is lowercase and the first letter shows the data type. 
*/
// *****************************************************************//
/*
#include <iostream>

int main() {
  int x = 10;
  int y = ++x;  x is incremented to 11, then y is assigned the value of x (11)
  std::cout << x << '\n' << y;
  return 0 ; 
} 
*/

/*
#include <iostream>

int main() {
  int x = 10;
  int y = x++; y is assigned the value of x (10), then x is incremented to 11
  std::cout << x << '\n' << y;
  return 0 ; 
}
*/

/*
#include <iostream>
int main() {
  int x = 10;
  double y = 5; 
  double z = (x+10)/(3*y);
  std::cout << z;
  return 0;
}
*/
// *****************************************************************//
/* 
#include <iostream>

using namespace std;

int main() {
  int x = 10;
  int y = 20;
  cout << "x = " << x << '\n';
  cout << "y = " << y ;
  return 0;
}
*/

/* #include <iostream>

using namespace std;

int main() {
  int x = 10;
  int y = 20;
  int z = x % y;
  cout << "s = " << z;
}
*/

/*
#include <iostream>

using namespace std;

int main() {
  int x = 10;
  int y = 20;
  cout << "x = " << x << endl
       << "y = " << y;
  return 0;
}
*/
// *****************************************************************//
/*
#include <iostream>

using namespace std;

int main() {
  double sales = 95000;
  const double countytax = sales * 0.02;
  const double statetax = sales * 0.04;
  double totaltax = countytax + statetax;
  double NetIncome = sales - totaltax;
  cout << "Sales = " << sales << endl
       << "County Tax = " << countytax << endl
       << "State Tax = " << statetax << endl
       << "Net Income = " << NetIncome ;
  return 0;
}
*/
// *****************************************************************//
/* 

// >> Entering user defined values.
#include <iostream>

using namespace std;

int main (){
  cout <<"Enter values :";
  double x;
  double y;
  cin >> x;
  cin >> y;
  cout << x+y;
  return 0;
}
*/


/*
# include <iostream>
# include <cstdlib>
using namespace std;

int main() {
  int x;
  cout << "Enter a number :";
  cin >> x;
  cout << x+2;
  return 0;
}
*/
/*
#include <iostream>
#include <cmath>

using namespace std;
int main () {
  cout << "Enter Radius :" ;
  double radius;
  cin >> radius;
  const double pi = 3.14;
  double area = pi * pow(radius , 2);
  cout << area ;
  return 0;
}
*/
// *****************************************************************//

/*
# include <iostream>
# include <cstdlib>
# include <ctime>
using namespace std;

int main() {
  srand(time(0)) ;
  To Print random Numbers between a range which has a MinValue and
     MaxValue, use the following formula :
     (((MaxValue - MinValue) + 1) + MinValue)

  int NumberOne = (rand() % (6-1+1)+1) ;
  int NumberTwo = (rand() % (6-1+1)+1) ;
  cout << NumberOne << ',' << NumberTwo ;
  return 0 ;
}
*/

// *****************************************************************//

// Strings
/*
#include <string>
#include <iostream>

using namespace std;

int main () {
  string Name = "John";
  string SurName = "Doe";
  string FullName = Name + " " + SurName;
  cout << FullName ;
  return 0;
}
*/

/*
#include <string>
#include <iostream>

using namespace std;

int main () {
  string Name = "John ";
  string SurName = "Doe";
  string FullName = Name.append(SurName);
  cout << FullName ;
  return 0;
}
*/
/*
#include <string>
#include <iostream>
using namespace std;

int main() {
  string name = "QwErTy";
  cout << name.size();
  return 0;
}
*/

/*
#include <string>
#include <iostream>
using namespace std;

int main() {
  string name = "We are the \"Indians\"";
  cout << name;
  return 0;
}
*/

/*#include <string>
#include <iostream>

using namespace std;

int main() {
  string name ;
  cout << "Enter your First Name :";
  getline(cin, name);
  cout << "Your Name is :" << name;
  return 0;
}
*/
/*
#include <iostream>
using namespace std;
int main() {
  bool isCodingFun = true;
  cout << isCodingFun;
}
*/

/* 
#include <iostream>

using namespace std;

int main() {
  int x = 20;
  int y = 10;
  int z = x + y;
  if (z == 30) {
    cout << "Correct";
  }
}
*/
/* if-else statements
#include <iostream>

using namespace std;

int main() {
  int time = 20;
  if (time < 18) {
    cout << "Good day" ;
  } else if (time == 20) {
    cout << "Good evening" ;
  } else {
    cout << "Good night" ;
  }
}
*/
/*
// Short Hand if-else
#include <iostream>
#include <string>

using namespace std;

int main() {
  int time = 20;
  string result = (time<18)? "Good Day ." : "Good Evening"; //variable = (condition) ? True : False;
  cout << result;
}
*/
/*
#include <iostream>
#include <string>

using namespace std;

int main() {
  int day ;
  cout << "Enter a number (1/2/3/4/5/6/7):";
  cin >> day;
  switch (day) {
    case 1:
      cout << "Day " << day << " Monday";
      break;
    case 2:
      cout << "Day " << day << " Tuesday";
      break;
    case 3 :
      cout << "Day " << day << " Wednesday";
      break;
    case 4 :
      cout << "Day " << day << " Thursday";
      break;
    case 5 :
      cout << "Day " << day << " Friday";
      break;
    case 6 :
      cout << "Day " << day << " Weekend";
      break;
    case 7 :
      cout << "Day " << day << " Weekend";
      break;
    default :
      cout << "Invalid Input";
  }
}
*/
/*
#include <iostream>

using namespace std;

int main() {
  int i = 5;
  while (i>false) { // while i>0 or while i>=true
    cout << i << '\n';
    i--;
  }
}
*/ 
/*
#include <iostream>
using namespace std;

int main() {
  int i = 0;
  do {
    cout << i << "\n";
    i++;
  }
  while (i < 5);
  return 0;
}
*/
// Structure
/*
# include <iostream>

using namespace std;

int main(){
  struct{
  int mynum;
  string mystr;
} myStructure;    // Assigned the value of struct{} as myStructure...
myStructure.mynum =  1  ;
myStructure.mystr = "A" ;
cout << myStructure.mynum << '\n' ;
cout << myStructure.mystr << '\n' ; 
}
*/

// Creating and Accessing multiple structures...
/*
# include <iostream>

using namespace std;

int main() {
  struct car{      // Naming the structure Car and storing it in Car1 and Car2. 
    string brand ; 
    string model ;
    int year     ; 
  } myCar1 , myCar2 ;
  myCar1.brand = " BMW  " ;
  myCar1.model = "  X5  " ;
  myCar1.year  =   1999   ;
  myCar2.brand = " Audi " ;
  myCar2.model = "  Q7  " ;
  myCar2.year  =   1969   ;
  cout << " Car    " << "Brand  " << "Model " << "  Year of Manufacture "             << "\n" ;
  cout << " Car1   " << myCar1.brand << myCar1.model << "       " <<     myCar1.year  << "\n" ; 
  cout << " Car2   " << myCar2.brand << myCar2.model << "       " <<     myCar2.year  << "\n" ;
}

// Naming a structure...

# include <iostream>

using namespace std;

int main() {
  struct car{       
    string brand ; 
    string model ;
    int year     ; 
  };
  car myCar1,myCar2 ;
  myCar1.brand = " BMW  " ;
  myCar1.model = "  X5  " ;
  myCar1.year  =   1999   ;
  myCar2.brand = " Audi " ;
  myCar2.model = "  Q7  " ;
  myCar2.year  =   1969   ;
  cout << " Car    " << "Brand  " << "Model " << "  Year of Manufacture "             << "\n" ;
  cout << " Car1   " << myCar1.brand << myCar1.model << "       " <<     myCar1.year  << "\n" ; 
  cout << " Car2   " << myCar2.brand << myCar2.model << "       " <<     myCar2.year  << "\n" ;
}
*/

// Enumeration (enum)
/*
# include <iostream>

using namespace std;

enum Level {
  X = 50  ,
  Y = 100 ,
  Z = 150
};

int main() {
  enum Level myVar = Y ;
  cout << myVar ;
  return 0 ; 
}
*/

/*
# include <iostream>

using namespace std ; 

enum Level {
  X = 80 , 
  Y = 80 ,
  Z
};

int main() {
  enum Level myVar2 = Z ; 
  cout << myVar2 ; 
  return 0 ; 
}
// Output 82 .( Y = X + 1(if Y not specified ).
// Z = Y + 1 ( if Z not specified)).
*/

/*
Why And When To Use Enums?
Enums are used to give names to constants, which makes the code 
easier to read and maintain.

Use enums when you have values that you know aren't going to change, 
like month days, days, colors, deck of cards, etc.
*/

// C++ References 
/*
# include <iostream>

using namespace std ; 

int main() {
  string food = " Pizza " ;
  string meal = food ;
  cout << food << "\n" ;
  cout << meal << "\n" ; 
}

*/
// C++ Memory Address
/*
# include <iostream>

using namespace std ; 

int main() {
  string food = " Pizza " ;
  string food2 = " asf " ;
  cout << &food  ; // This prints the location or memory address of the variable.
  cout << &food2 ; // It will be stored in a location and it will not change.    
}                  // It will be different for different variables.
*/

// C++ Pointers and Deference
/*
# include <iostream>

using namespace std ; 

int main() {
  string food = "Pizza" ;
  string* ptr =   &food ;// Assigning the memory location a value ptr(pointer)
  cout << food  << "\n" ;
  cout << &food << "\n" ;
  cout << ptr   << "\n" ;// Output : Memory Address.
  cout << *ptr  << "\n" ;// Output : Returns the variable value.        
}                  
//    There are 3 ways to declare a pointer(ptr) : 
// 1. string* mystring  ; 
// 2. string *mystring  ;
// 3. string * mystring ;
*/

// FUNCTIONS and their CREATION 

// Creating a function
//  (I)
/*
# include <iostream>

using namespace std ; 

void myFunction() {
  cout << "I just got executed!";
}

int main() {
  myFunction(); // call the function
  return 0;
}
*/

/*
// :::::::::::::::::::::::: Note ::::::::::::::::::::::::

