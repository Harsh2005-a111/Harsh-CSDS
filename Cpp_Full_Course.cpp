
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
# include <iostream>

using namespace std ; 

int main() {
  myFunction();
  return 0;
}

void myFunction() {
  cout << "I just got executed!";
}

// Error. User Defined function declared  
// after that function is called in the main function .
// :::::::::::::::::::::::::::::::::::::::::::::::::::::::
*/

// To avoid above error, on can either use I or II.
// Function declaration
//  (II)
/*
# include <iostream>

using namespace std ; 

void myFunction(); //Declare a function before main() 
                   //and then characterize the function...

// The main method
int main() {
  myFunction();  // call the function
  return 0;
}

// Function definition
void myFunction() {
  cout << "I just got executed!";
}


*/
/*
// Calling a function multiple times...
# include <iostream>

using namespace std ; 

void myFunction() ;

int main() {
    myFunction() ;
    myFunction() ;
    myFunction() ;

}

void myFunction() { 
    cout << ("I just got Executed!\n") ; 
}
*/
/*
#include <iostream>

using namespace std ; 

int main() {
  cout << " Enter N for number of Student's Data to be Inserted :";
  int N ;
  cin >> N ;
  string Data[N][3] ;   // Array size is specified. No Error
  for (int I = 0 ; I < N ; I++) {
    cout << " Student's Name   "   << (I+1) << ": " ; 
    Data[I][0] ;
    cin  >> Data[I][0] ; 
    cout << " Student's Age    "   << (I+1) << ": " ; 
    Data[I][1] ;
    cin  >> Data[I][1] ;
    cout << " Student's Branch "   << (I+1) << ": " ; 
    Data[I][2] ;
    cin  >> Data[I][2] ;
    }
  cout << " Name    "   << "  Age   "    << "  Branch   " << '\n' ;
  for (int I = 0 ; I < N ; I++) { 
    cout << " " << Data[I][0] << "       " << Data[I][1] << "     " << Data[I][2] << "\n"   ; 
  }
  return 0 ;
}
*/

// Parameters and Arguments...
// I . General
/*
#include <iostream>

using namespace std ; 

void myFunct(string Name) {
    cout << "Name : " << Name << "\n" ;
}
int main() {
    myFunct("Harsh") ; 
    myFunct("Yash") ; 
    return 0 ;
}
*/

// II . Default Parameters 
/*
#include <iostream>

using namespace std ; 

void myFunct(string Name = "Jatin") {
    cout << "Name : " << Name << "\n" ;
}
int main() {
    myFunct("Harsh") ; 
    myFunct("Yash")  ; 
    myFunct()        ; 
    return 0         ;
}
// A parameter with a default value, is often known as an "optional parameter". 
// From the example above, Name is an optional parameter and "Jatin" is the default value. 
// The void keyword indicates that the function should not return a value.
// If the user wants to return a value then he must specify the data type before assigning
// the function (example : int string bool etc.)
*/
/*
// III Return Values ..
#include <iostream>
 
using namespace std ; 

int myFunct(int x , int y) {
  cout << x << " + " << y << " = " ;  
  return x + y ;   
}

int main() {
  int x ;
  int y ;
  cout << "x = " ;  
  cin >> x ; 
  cout << "y = " ; 
  cin >> y ;
  cout << myFunct(x , y) ; 
  return 0 ;
}
*/
/*
// IV Multiple Parameters..
#include <iostream>

using namespace std ; 

void myFunction(string name , int age ) {
  cout << "Name : " << name << endl << "Age  : " << age ;
}
int main(){
  myFunction("Harsh" , 19) ; 
}
*/
// Swapping two data..
/*
#include <iostream>
using namespace std ; 

void Swap(int FirstNum , int SecondNum) {
  int z = FirstNum ; 
  FirstNum = SecondNum ;
  SecondNum = z ;  
  cout << FirstNum  << "  " << SecondNum ; 
}
int main() {
  int FirstNum  ; 
  cout << "First Number : "  ; 
  cin >> FirstNum  ; 
  int SecondNum ; 
  cout << "Second Number : " ; 
  cin >> SecondNum ;
  cout << "Before Swapping >>" << FirstNum << "  " << SecondNum << "\n";
  cout << "After Swapping >>" ;
  Swap(FirstNum , SecondNum) ; 
  return 0 ;
}
*/
// Passing Arrays to a function
/*
#include <iostream>

using namespace std ; 
void myFunction(int myNum[5]) {
  for (int i = 0 ; i < 5 ; i++) {
    cout << myNum[i] << "\n"; 
  }
}
int main() {
  int myNum[5] = {10,20,30,40,50} ; 
  myFunction(myNum) ;
  return 0 ;
} 
*/
/*
// Function Overloading..
#include <iostream>

using namespace std ;

int plusFunc(int x, int y) {
  return x + y;
}

double plusFunc(double x, double y) {
  return x + y;
}

int main() {
  int myNum1 = plusFunc(8, 5);
  double myNum2 = plusFunc(4.3, 6.26);
  cout << "Int: " << myNum1 << "\n";
  cout << "Double: " << myNum2;
  return 0;
}
*/

/*
The function is assigned the same name but since the 
data type and teh numbers are assigned different therefore the
result will be displayed and this situation is called 
Function Overloading...
Instead of defining two functions that should do the same thing, 
it is better to overload one. In the example above, we overload the 
plusFunc function to work for both int and double:
*/

// Scope of a variable =>
// Local Scope... Variable can be used in the scope it is specified within only.
// Any changes in the other scope will not effect the variable specified . 
/*
void myFunction() {
  int x = 5;
  cout << x;
}

int main() {
  myFunction();
  return 0;
}
*/

// Global Scope...
// Variable (x) can be used in both the function and the main code.
/*
# include <iostream>

using namespace std ; 

int x = 5 ; 

void myFunction() {
  cout << x << "\n"; 

}

int main() {
  myFunction() ;
  cout << x ; 
  return 0 ;
}
*/
/*
# include <iostream>
using namespace std;

void pattern1(int N)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << "* ";
        }
      cout << endl;
    }
}

int main()
{   
    int N = 5;

    pattern1(N);

    return 0;
}
*/


