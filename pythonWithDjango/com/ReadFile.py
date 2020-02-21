#!C:\Users\admin\AppData\Local\Programs\Python\Python38

import math
from pip._vendor.distlib.compat import raw_input


print('Application')
if True:
    print("True")
else:
    print ("False")
if True:
    print( "Answer")
    print( "True")
else:
    print ("Answer")
    print( "False")

print("================================================================================")

'''
raw_input("\n\nPress the enter key to exit.")
import sys; x = 'foo'; sys.stdout.write(x + '\n')
'''


counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print( counter)
print (miles)
print (name)
print("================================================================================")
a = b = c = 1
a,b,c = 1,2,"john"
print( a)
print (b)
print (c)
print("================================================================================")
var1 = 1
var2 = 10

print( var1)
print (var2)

#del var1, var2  -------> print(var1) will say var1 is not define
print("================================================================================String")
str = 'Hello World!'

print (str )         # Prints complete string
print (str[0]  )     # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:] )     # Prints string starting from 3rd character
print( str * 2 )     # Prints string two times
print (str + "TEST") # Prints concatenated string
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')
print("================================================================================")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0] )      # Prints first element of the list
print (list[1:3] )    # Prints elements starting from 2nd till 3rd
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2 ) # Prints list two times
print (list + tinylist) # Prints concatenated lists
print("================================================================================")
a = 10
b = 2
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
    print( "Line 1 - a is available in the given list")
else:
    print ("Line 1 - a is not available in the given list")

if ( b not in list ):
    print ("Line 2 - b is not available in the given list")
else:
    print ("Line 2 - b is available in the given list")

print("================================================================================")
var = 100
if ( var == 100 ) : print ("Value of expression is 100")
else: print("not Value of expression")
print ("Good bye!")
print("================================================================================")
var = 2
while var == 1 :  # This constructs an infinite loop
    num = raw_input("Enter a number  :")
    print ("You entered: ", num)

print ("Good bye!")
print("================================================================================")
for letter in 'Python':     # First Example
    print ('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
    print ('Current fruit :', fruit)

print ("Good bye!")
print("================================================================================")
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print( 'Current fruit :', fruits[index])

print ("Good bye!")
print("================================================================================")
for num in range(10,20):     #to iterate between 10 to 20
    for i in range(2,num):    #to iterate on the factors of the number
        if num%i == 0:         #to determine the first factor
            j=num/i             #to calculate the second factor
            print ('%d equals %d * %d' % (num,i,j))
            break #to move to the next number, the #first FOR
    else:                  # else part of the loop
        print (num, 'is a prime number')
print("================================================================================Break")
for letter in 'Python':     # First Example
    if letter == 'y' :
        #print('Current Letter :',letter)
        continue
    if letter == 'h':
        pass
        print ('This is pass block')
    if letter == 'o':
        break
    print ('Current Letter :', letter)
print("================================================================================")
print ("math.floor(-45.17) : ", math.floor(-45.17))
print ("math.floor(100.12) : ", math.floor(100.12))
print ("math.floor(100.72) : ", math.floor(100.72))
#print ("math.floor(119L) : ", math.floor(119L))
print(math.pi)
print ("math.floor(math.pi) : ", math.floor(math.pi))
print("================================================================================")
print ('C:\\nowhere')
print (r'C:\\nowhere')
print (u'Hello, world!') #Unicode String
print("================================================================================")
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print (str.split( ))
print (str.split(' ', 1 ))
print("================================================================================")
print ("My name is %s and weight is %d kg!" % ('Zara', 21))
print("================================================================================")
list1 = ['physics', 'chemistry', 1997, 2000];
print (list1)
del list1[2];
print ("After deleting value at index 2 : ")
print (list1)
print("================================================================================")
print("tuple is a sequence of immutable Python objects.")
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
print("================================================================================")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
print("================================================================================")
import time;

localtime = time.localtime(time.time())
print ("Local current time :", localtime)
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

import calendar

cal = calendar.month(2020, 2)
print ("Here is the calendar:")
print (cal)
print("================================================================================")
# Function definition is here
def printme( str ):
    "This prints a passed string into this function"
    print (str)
    return str+" 123";

# Now you can call printme function
var3 = printme("I'm first call to user defined function!")
printme("Again second call to the same function")
print(var3)
print("================================================================================")
# Function definition is here
def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
print("================================================================================")
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
print("================================================================================")

total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
    # Add both the parameters and return them."
    total = arg1 + arg2; # Here total is local variable.
    print ("Inside the function local total : ", total)
    return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total)
print("================================================================================")
# Import module support
import support
import sys

# Now you can call defined function that module as follows
support.print_func("Zara")
print("================================================================================")
print("Local variables: ",locals())
print("Global variables: ",globals())
print("================================================================================")
bytes = "Hello World!".encode()
fo = open("foo.txt", "rb+").write(bytes)
#print ("Name of the file: ", fo.name)
#print ("Closed or not : ", fo.closed)
#print ("Opening mode : ", fo.mode)
var = 'Python is a great language.Yeah its great!!'
#fo.close()
print("================================================================================")

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(11);
print ("Read String is : ", str)
# Close opend file
fo.close()
print("================================================================================")
import os

# Create a directory "test"
os.rmdir("Siraj Diwan")
os.mkdir("Siraj Diwan")
print("================================================================================Exception")
def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32
print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
#print (KelvinToFahrenheit(-5))
'''
Traceback (most recent call last):
  File "C:/Users/admin/IdeaProjects/pythonWithDjango/ReadFile.py", line 262, in <module>
    print (KelvinToFahrenheit(-5))
  File "C:/Users/admin/IdeaProjects/pythonWithDjango/ReadFile.py", line 258, in KelvinToFahrenheit
    assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
'''
print("================================================================================")
try:
    fh = open("testfile", "w")
    #fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
else:
    print ("Written content in the file successfully")
    fh.close()
print("================================================================================")
try:
    fh = open("testfile2", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print ("Error: can\'t find file or read data")
print("================================================================================")
try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print ("Going to close the file")
        fh.close()
except IOError:
    print ("Error: can\'t find file or read data")
print("================================================================================")
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
print("================================================================================ssl")