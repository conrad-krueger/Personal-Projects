misc
=============================================

This folder contains miscellaneous progams that I wrote.

-------------------------------------------
bf.cpp
-------------------------------------------
Compile and Run:

g++ bf.cpp -o bf

./bf <insert .txt filename with bf syntax>

Short: A C++ program that acts as an interpreter of an esoteric programming language.

Long: An interpreter of esoteric programming language, with a not so PG-13 name, whose goal was to run on the 
smallest compiler. It only has 8 commands (< > + - [ ] , .)so it became a fun challenge to to write an 
interpreter for the language in C++. 
  
It's turing complete and is a language in which you essentially manually 
increment and decrement memory. There is a single pointer on 30000 bytes of memory which is moved left and right 
by using > and < respectively. Input and output is , and . respectively. Incrementing and decrementing a cell 
value is + and - respectively. And the only iterative control structure is a while loop [ /*code here*/] and will 
exit once the pointer has a value of 0.


Here is how to output "Hello, World!" found in helloworld.txt
                                                          
\>++++++++[<+++++++++>-]<.
                           
\>++++[<+++++++>-]<+.
                      
\+++++++..
                      
\+++.
                      
\>>++++++[<+++++++>-]<++.
                          
\------------.
                          
\>++++++[<+++++++++>-]<+.
                          
\<.
  
\+++.
  
\------.
  
\--------.
  
\>>>++++[<++++++++>-]<+.


-------------------------------------------
matrix.cpp & matrix.h
-------------------------------------------
Compile and Run:
g++ matrix.cpp -o matrix
./matrix

Short + Long: Files that contain the implementation of a Matrix ADT with the addition of functions that accept 
Matrix objects as arguments. These include basic linear algebra methods like: matrix multiplication, multiplying 
a matrix by a scalar, matrix subtraction, matrix addition; Finding the transpose, inverse, and determinant of a 
matrix (when appropriate). 
                         
Used primarily for demostration of C++ concepts like: encapsulation, inheritence, templating, operator 
overloading, overriding functions with virtual keyword, recursion and rule of three (copy assignment operator, 
copy constructor, destructor).
                         
Note: This file is not concerned with the speed of the code but demonstration of C++ concepts. For example, when 
overloading operator-, it would be more efficent to just copy the operator+ code and just subtract
each value. The implemented method multiplying the right hand matrix by -1 and then just adding the two matrix 
has less lines of code, is more readable, and shows how one can use previously defined operators to aid in 
computation. However, it is slower since multiplying a matrix by a scalar causes an entirely new matrix object to 
be created and then addition is performed. 


-------------------------------------------
covidDeltaData.ipynb
-------------------------------------------

Short: Data Visualization of COVID-19 data. Supports media outlets claims of when Delta variant started having a rapid effect in different countries.

