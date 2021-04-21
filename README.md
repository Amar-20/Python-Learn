# Python-Learn
## **What is Python?**

***** Python is an interpreter programming language. It is used for Software development, Web development, maths, system scripting, etc.,
* It interprets the score code line by line.
* It was created by Van Rossum in 1991.

## **Why Python?**

***** Python works on different platforms windows, ios, Linux, etc. 
* Python Syntax is easy just like the English language.
* Python runs on a system, meaning that code can be executed as soon as it is written.
* Python can be treated in a procedural way, an object-oriented way, or a functional way.

## **Inner working of python**

![alt text](<Mutable and immutable examples.png>)

Steps

1. When the source code is written it goes to the Python interpreter.
2. The Python interpreter consists of two components.
* Compiler
* VM (Python Virtual Machine)
3. The compiler converts the source code into “Byte code”(compiled python code)
*This compiled Python code consists of “Forzenbinaries”(with .pyc file)
* This “Byte file” is a low-level Python-independent file.
* This Byte code runs faster.
4. Then this “Byte code” is sent into the VM and the code is executed. 

NOTE: We also have “__pycache__” which is a system-built folder for all the .pyc files.
These .pyc  files can only be seen when we work on importing files. The .pyc file name combines the “Source file name(change)” and “Python version.” So whenever the source file changes, the frozen binaries will also change and create a sequence of new  .pyc files or change the existing  .pyc file. Python makes a system-built folder ”__pycache __” to keep these files in order. 

## **Modules in Python**

There are numerous in-built modules in Python. Some of them are 

**OS module:** The OS module is an in-built module that consists of methods for interacting with the operating system, like creating files and directories, managing files and directories, input, output, environment variables, process management, etc.

Examples: os, sys, math, random, collection, re, datetime, time, JSON , csv.
Example: os. getcwd - will get you the present working directory.

1. OS module: Python has a built-in os module with methods for interacting with the Operating system.
* os.getcwd() — to get the current working dir.
* os.abort() — Terminates the running process immediately.
* os. exit() — exit the process with the specified status.
2. SYS Module: The Python sys module **provides functions and variables that are used to manipulate different parts of the Python Runtime Environment**. 
* sys. version — returns a string containing the Python Interpreter version with some additional information
* sys. path — used to search modules from the list of paths.
3. Math Module: used to work with mathematical operations.

**NOTE**:  We can also create and import our modules into Python.   
While doing this if we change any module source code and want that change to be available in the imported code file rather than re-importing or closing and opening the file, we can just “Reload” the imported file by using a module called “importlib”.
Example: importlib.reload(<file_name>) (By this changes made in the module file are now available to the imported file.) 

NOTE:  A **"library" in Python is a collection of modules**, meaning a library is a broader concept encompassing multiple modules, whereas a “**module”** is a single Python file containing functions, classes, and variables that can be imported and used in other programs; essentially, a module is a building block of a library.

## Immutable and Mutable in Python:
![alt text](<mutable and immutable.png>)



- Almost everything in Python is an object, with its properties and methods.
- In Python, there are two types of datatypes: Immutable and Mutable.
    
    ![Untitled-2024-11-08-1343.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f113ec89-c97e-449f-808b-a9e44ada6c72/7cc9b85a-da4e-4103-8ad5-7b2a955aed93/Untitled-2024-11-08-1343.png)
    
- This Immutable and Mutable refers to the change in the internal memory of Python.
Examples of Immutable data types: 
1) Integers
2) Strings, tuple, bool 
Now, When we look at the internal function of the immutable data types.

![Untitled-2024-11-08-1343.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f113ec89-c97e-449f-808b-a9e44ada6c72/ad521de1-c5da-4902-b1e6-a4d07f8aa3e7/Untitled-2024-11-08-1343.png)

```python
>>> a= 12
>>> b=a
>>> a == b
>>> True
>>> a is b
>>> True
"""Here both a and b are referred to same object space, and their data values are also same.
"""
>>> a = 13
>>> b 
>>> 12
>>> a
>>> 13
>>> a == b
>>> False
>>> a is b
>>> False
"""Now, whenever we change the data value of a, python creates new object space memory
for a and now a is referred to changed value 13,b is still referred to old a value 12."""

```

## Garbage collection in Python.

In Python, the garbage collector is a mechanism that automatically manages memory by reclaiming memory occupied by objects that are no longer in use. Here's what it does:

**Identifies Unused Objects:**

- The garbage collector keeps track of all objects in memory and determines which ones are no longer accessible by the program.
- It does this primarily through reference counting, where it tracks the number of references pointing to an object. When an object's reference count drops to zero, it's considered garbage.

**Frees Up Memory:**

- Once the garbage collector identifies unused objects, it frees up the memory they occupy, making it available for other data.
- This prevents memory leaks, which occur when memory is allocated but never released, eventually leading to program crashes or performance issues.
- **Sometimes garbage collectors will not free up the space immediately especially with *number* and *string* data types objects because number and string data types objects are more often used again so, to free up space and create a new object space takes computation, to minimize this it won’t delete or free up space immediately.**

## When it comes to Mutable data types:

- The change happens within the memory rather than creating a new memory for the changed variable.
- It refers to the same memory.
    
    ```python
    #take list with are mutable data types.
    a= [1,2,3]
    b=a
    
    # Here a object space is created with a list [1,2,3] and is referred(pointed) to varible 'a'.
    # And the same object space is referred(pointed) to variable 'b'
    a[0]= 22
    >>>a
    >>>[22,2,3]
    >>>b
    >>>[22,2,3]
    
    """Here obsurve that 'a' variable list is changed and so as the 'b' variable list 
    rather than creaating a new object space for new value of list(as in as immutable data types)
    """
    
    """ Now """
    a=[12,13,14]
    b=[12,13,14]
    >>>a==b
    >>>true
    >>>a is b
    >>>false
    """-------------------------------------------------------------------------"""
    >>>a[0]=22
    >>>a
    >>>[22,13,14]
    >>>b
    >>>[12,13,14]
    >>>a == b # here we are checking data values.
    >>> false
    >>> a is b # Here we are checking object space reference.
    >>> false
    
    """If we create two varibles list with same values, 
    then python creates two objects spaces even the data values are same because these are 
     mutable data types."""
    """ Here two varibles are referred to two object spaces, if change the other remains the
    same."""
    -----------------------------------------------------------------------------------
    # Now lets talk about copy and deepcopy
    a =[1,2,3]
    b = a[:]
    """Here we think that both and 'a' and 'b' are pointed to same memory space but,
    they both referred to different memory spaces(as 'b' holds copy of 'a' 
    in different memory space) or we can also copy using import copy module."""
    
    import copy
    a= [12,13,14]
    b=copy.copy(a) 
    b= copy.deepcopy(a) # This copies nested list also if any.
    ```
    

## Variables in Python:

- Variables are containers for storing data values.
- Variables can be created at any time when you assign a value to them.
- All variable names are case-sensitive. (a =12 and A=12 diff )
- If we want to specify the data type of variable, that can be done using “Casting”.
- Always remember that the data type you specify will only be referred to or pointed to “object memory of the data value not to the variable name you given. ”
    
    ```python
    x=str(3) #casting
    y=float(3) #casting
    z=int(3) #casting
    
    print(x)
    -- '3'
    
    print(y)
    -- 3.0
    
    print(z)
    -- 3
    # We can also get the variable data type.
    print(type(z))
    -- int
    print(type(x))
    -- str
    ```
    
- Variable names can only start with letters or underscore char.
- Variable names can’t start with numbers.
- Variable names can only contain alphanumeric char and underscore.(A-Z, 0-9 and _)
- Variable names can’t have any Python keywords.
- In Python, we can also assign multiple values to multiple variables.
    
    ```python
    x,y,z = 1,'amar',12.3
    ```
    
- In Python, we can also assign multiple variables to one value.
    
    ```python
    x=y=z='amar'
    ```
    
- In Python, the Print() function is used to output the variables.
- Global variables:  These are the variables that are created outside of any function.
- Global variables can be used anywhere, everyone both inside and outside the functions.
    
    ```python
    x='awsome'
    print('Python is'+x)
    
    def myfun():
        print('python is',x)
    
    myfun()
    
    #O/p:- Python isawsome
    #      python is awsome
    ```
    
- Where as Local variables are the variables that are created inside the functions and are not accessible outside the function.
    
    ```python
     x='awsome'
    
    def myfun():
       x='ugly'
       print('python is',x)
    myfun()
    
    print('python is '+ x)
    
    #o/p:- python is ugly
    #      python isawsome
    ```
    
- Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
- To create a global variable inside a function, you can use the `global` keyword.

 

## **Data Types in Python:**

 

- In any programming language data types are important.
- Variables can store data of different data types.
- Some of the data types in Python are:
1. Text type: String Str()
2. Number type: int, float, complex
3. Sequence type: List, tuple, range()
4. Mapping: dict
5. Set type: set {}, frozenset({})
6. Boolean type: boolean (True or False)
7. None Type: None type
8. Binary type: bytes, byte array

Now let’s see what these represent.

```python
#Text type (immutable)
a="Amar"

#Number type(immutable)
a=12 #int 
b=12.23 #float
c= 1+3j #complex

#Sequence type
a=[12,'amar',12.4] # list (mutable)
b=(12,'amar',45.3) # tuple (immutable)
c=range(10) # range(mutable) 

#Mapping type
a={"name": "amar","age":27,"state":"michigan"} # dict (mutable)

#set type (mutable)
a={12,23,34} #set
b=({'amar','happy','dhru'}) #frozenset

#Boolean type (immutable)
a= true
b= false

# none type
a=none
```

## Operators in Python

- Operators are used to perform operations on variables and values.

Python divides the operators into the following groups:

- Arithmetic operators - Arithmetic operators are used with numeric values to perform common mathematical operations (+,-,/,%,**,//)
- Assignment operators - Assignment operators are used to assign values to variables (=,+=,-=,)
- Comparison operators(==,! =, >,<,< =,> = )
- Logical operators(and,or,not)
- Identity operators(is, is not) to check if both operands refer to the same object in memory.
- Membership operators,  (in, not in) Membership operators are used to test if a sequence is presented in an object:
- Bitwise operators - Bitwise operators are used to compare (binary) numbers (&, |, ^, ~, <<,>>)

## Numbers in Python

There are three numeric types in Python. These are Immutable data types.

- int
- float
- complex

INT or Integer is a whole number with either positive or negative numbers, without decimals, of unlimited length.

- 12324
- -12896865643243

FLOAT or Float point number is a number with one or more decimals, positive or negative numbers.

- 12.2
- -12134.34545
- 12e2 float can also be of scientific value.

A Complex number consists of the imaginary number ‘J’.

- 12+j
- 8+12j

NOTE: Always remember that we should perform any mathematical operation only with two similar data type values. For example

```python
a=12
b=12.23
a + b
24.23 # but its not a standard practice.so we have to use similar data type values.

# or we can give our intention like
int(a)+int(b)
24

#repr()- provides a detailed and unambigous representation of an object.
#str()- provides a human readble representation of an object.
#print() - displaying of given object or text.
```

In Python, we also have inbuilt modules such as math, and random to work with number data types.

Here are some examples

```python
import random
random.randint(2,9) # Here both 2 and 9 are included 
>>>2
random.randint(2,9)
>>>9
randint(2,9)
>>> 3

""" Now, we use randrange() """
random.randrange(2,10) #random number from 2,9 excluding 10.
random.randrange(2,10)
>>>2
random.randrange(2,10)
>>>4

""" We aslo have 'choice' in random module this can choose a single value from give list"""
a=[12,34,75,'amar']
random.choice(a)
>>>12
random.choice(a)
>>>'amar'

""" We also have 'shuffle' in random module this can shuffle entry list"""
random.shuffle(a)
a
>>>['amar',12,75,34]

"""If we are working with decimal values we can use 'decimal' module. For example """
import decimal
decimal.Decimal('0.1')+decimal.decimal('0.1')-decimal.Decimal('0.2')
>>>Decimal('0.0')

""" We can also use fractions module to work with fraction values"""
import fractions
fractions.Fracton()

"""we can also use math module to work to complex mathematical operatons"""
import math
math.sqtr(64)
>>>8.0
```

## Strings in Python

Strings in Python are surrounded either by single quotes, double quotes, or triple quotes. 

- ‘Amar’
- “Amar”
- “”” fcvkliuygtfyrdbikshua
fhgsjagsjhdbaksdja
hfscxhasvcjahbckba “””

### Slicing a string

- You can return a range of char using slicing syntax
- Specify the start index and end index number separated by a colon to return a part of the string.
    
    ```python
    a='India is a free country'
    print(a[0:5])
    >>> 'India' (not including the last value 5)
    
    ---------------------------------------------------------
    print(a[-1])
    >>>'y'
    -------------------
    print(a[1:8:2]) ## jumps 2 values in between
    ```
    

### Modifying a string;

- In Python, we have built-in methods that can be used on strings.
- All of these modifications won’t change the original string value.
1. Upper()
    
    ```python
    a='amar'
    print(a.upper())
    >>> 'AMAR'
    ```
    
2. Lower()
    
    ```python
    a='AMMA'
    print(a.lower())
    >>>'amma'
    ```
    
3. Split()
    
    ```python
    a='India is a free country'
    print(a.split(' '))
    >>> ['India','is','a','country'] # converts string into list
    ```
    
4. strip()
    
    ```python
    a=" India    "
    print(a.strip())  # clears starting and ending spaces
    >>> 'India'
    ```
    
5. Replace()
    
    ```python
    a='amar'
    print(a.replace('a','J'))
    >>> 'Jmar'
    ```
    

### String format

- In Python we can’t concat string and number data types so, we use string format.
- We have two ways to do this
1. F-String
- F-string allows you to format selected part of the string
    
    ```python
    age=27
    print(f'I am {age} years old!!')
    >>'I am 27 years old'
    ```
    
- To format values in an f-string, add placeholders `{}`, a placeholder can contain variables, operations, functions, and modifiers to format the value.
    
    ```python
    age= 27
    print(f'I am {age:.2f} years old!!')
    >>> 'I am 27.00 years old'
    
    age =27
    print(f'I am {12*2} years old!!')
    >>> 'I am 24 years old'
    ```
    
1. Format() type
    
    ```python
    price = 49
    txt = "The price is {} dollars"
    print(txt.format(price))
    >>> 'The price is 49 dollars'
    
    ----------------------------------------------------------------
    # multple values
    quantity = 3
    itemno = 567
    price = 49
    myorder = "I want {} pieces of item number {} for {:.2f} dollars."
    print(myorder.format(quantity, itemno, price))
    >>> 'I want 3 pieces of item number 567 for 49.00 dollars'
    ```
    

### Escape Characters

- To insert characters that are illegal in a string, use an escape character.
    
    ```python
    \'	Single Quote	
    \\	Backslash	
    \n	New Line	
    \r	Carriage Return	 ()
    \t	Tab	
    \b	Backspace	
    \f	Form Feed	
    \ooo	Octal value	
    \xhh	Hex value
    ```
    

### Methods In Strings:

- Python has some in-built methods that can be used on strings
- All the methods give changed values, but this won’t change the original data value.
    
    ```python
    # center()
    a='india'
    print(a.center(10))
    >>> '     india      ' # returns the string with 10 spaces and word in the center.
    
    # count()
    a='India is a free and independent country'
    print(a.count('i'))
    >>> 4
    
    # find()
    a='india is a country'
    print(a.find('is'))
    >>> 6
    
    # in
    a="masala tea"
    print("masala" in a)
    >>> True
    
    # We can also convert list[] to string
    a=['amar','is','a','boy']
    print(" ".join(a))    # we can also use '-','@',',' etc.,
    >>> 'amar is a boy'
    ## there are many more..
    ```
    

## LIST[ ]

- List in Python is used to store multiple values in a single variable.
- The list stores a collection of data values.
- List in Python is mutable
- List items are indexed [0] is the first item and [1] is the second item in the list

NOTE:  Python lists are Changeable and ordered, and allow duplicate values.

example: a=[’amar’,23,23,34.00]

### Access list items:

```python
a=['amar',12,90.89]
print(a[0])

>>> 'amar'

---------------------------
print(a[-2:-1])
>>> 12
```

### Change and Insert in the list

```python
a=['masala','ginger',12,90.8,'white']
a[3]='lemon'
print(a)
>>>['masala','ginger',12,'lemon','white']

# change multiple values
a[1:4] =[12,34,56]
print(a)
>>> ['masala',12,34,56,'white']

'''If you insert more items than you replace,
the new items will be inserted where you specified,
 and the remaining items will move accordingly: (this chnages and removes values)'''
a=[12,23,4,5,67,8,9,65]
a[1:3]=[76,87,32,21]
print(a)
>>> [12,76,87,32,21,5,67,8,9,65]

''' If you insert less items than you replace, the new items will be inserted where you specified, 
and the remaining items will move accordingly: (this chnages and removes data values)'''
a=[12,23,34,45,56]
a[1:4]=[90]
print(a)
>>>[12,90,56]

''' Insert values without removing and changing the data values'''
a=[12,23,34,45,56,67]
a[2:2]=[98,87,76]
print(a)
>>> [12,23,98,87,76,34,45,56,67] # values are inserted at position 2

''' we can insert at a given position'''
a=[12,23,45,67,78]
a.insert(2,90)
print(a)
>>> [12,23,90,45,67,78]

''' We can also insert empty list value.This removes the value'''
a=[12,23,34,45,56]
a[1:2]=[]
print(a)
>>> [12,34,45,56]
```

### Adding list items

```python
''' adding a list item at the end of list'''
a=[12,23,34,45,56]
a.append('orange')
print(a)
>>> [12,23,34,45,56,'orange']

''' Adding a list item at the given postition'''
a=[12,23,34,45]
a.insert(2,'amar')
print(a)
>>> [12,23,'amar',34,45]

''' adding a iterable at the end of the list.(iterables can be list, tuple,set,dict)'''
a=[12,23,45]
b=(32,43,54)
a.extend(b)
print(a)
>>> [12,23,45,32,43,54]

'''Joining the lists to create third list'''
a=[12,23]
b=[45,56]
c=a+b
print(c)
>>> [12,23,45,56]
```

### Remove list items

```python
# remove()
a=[12,23,45,'amar']
a.remove('amar')
print(a)
>>> [12,23,45]

# pop()
a=[12,23,34,45]
a.pop()
print(a)
>>>[12,23,34]
------------------ 
a.pop(1)
print(a)
>>>[12,34,45]

# del 
a=[12,23,34,45,56]
del a[0]
print(a)
>>> [23,34,45,56]
----------------------------
a=[12,23,34,45,56]
del a
print(a)
>>> '''come out error because we have completely deleted the list.'''

# clear
a=[12,23,34,45]
a.clear()
print(a)
>>> [] #empty list

```

### Looping through List

```python
#for loop
for n in [12,23,34,45]:
  print(n)

>>> 12
>>> 23
>>> 34
>>> 45

# we can also use end key word to avoid line breaks
for n in [12,23,34,45]
    print(n,end=" ")
>>> 12 23 34 45
```

### Sorting in List

```python
# sort()
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
>>> ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# sort(reverse=True) sort the descending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
>>> ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# reverse() reverses the order of list.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
>>> ['cherry', 'Kiwi', 'Orange', 'banana']
```

### Copy List

```python
# we can do it in three types
#copy() 
one=[12,'amar',45,78.0]
two=one.copy()
print(two)
>>> [12,'amar',45,78.0]

# using list()
first=[12,34,45,67]
second=list(first)
print(second)
>>> [12,34,45,67]

#using [:]
a=[12,23,34,45]
b=a[:]
print(b)
>>>[12,23,34,45]
```

 

## Tuples

- A tuple is a collection of data values.
- A tuple is ordered, unchangeable, and allows multiple values.
- It also allows multiple data types.
    
    ```python
    a=(12,23,'amar',True,67.90)
    
    print(a[0])
    >>>12
    
    print(a[0:3])
    >>> 12,23'amar'
    
    if 'amar' in a:
      print('True')
    else:
      print('False')
    
    >>> True
    ```
    
- Once the tuple is created we can not change the values, because it is immutable.
- But there is a workaround to change items in the tuple. That is we convert the tuple first into a list and then add, and remove items.
    
    ```python
    a=(12,'amar','is ',88)
    b=list(a)
    b[1]='kiwi'
    a=tuple(b)
    print(a)
    >>> (12,'kiwi','is',88)
    
    # we can also add items
    a=(12,23,'kiwi','orange')
    b=list(a)
    b.append('watermelon')
    a=tuple(b)
    print(b)
    >>> (12,23,'kiwi','orange','watermelon')
    
    # we can remove items using del and remove
    a=(12,23,34)
    b=list(a)
    b.remove(12)
    a=tuple(b)
    >>> (23,34)
    
    # using del
    a=(12,23,34)
    del a
    print(a)
    >>> error
    
    ```
    
- In Python, we are allowed to add tuples to tuples.
    
    ```python
    a=(12,23,34)
    b=(23,)
    c=a+b
    print(c)
    >>> (12,23,34,23)
    ```
    
- While creating a tuple we assign values called “packing”
- We can also unpack by assigning variables to the tuple values.
    
    ```python
    fruits=('watermelon','kiwi','strwaberry')
    (green,dotted,red)=fruits
    
    print(green)
    >>> 'watermelon'
    ```
    

## SET in Python

- Set in Python is used to store a collection of items.
- Sets are unordered and mutable, allow multiple data types, and no duplicates are allowed
- Set are written in { }

```python
theset={'amar',23,True,3.90}

# in set True and 1 are considered same even False and 0 are same.

print(len(theset))
>>> 4
```

- We can’t access set items using indexing because the set is an unordered iteral.

```python
theset={True,23,98.98,'amamr'}
for x in theset:
  print(x,end=" ")
>>> 23,True,amamr,98.98

theset ={True,34,'chintu',False}
if 'chintu' in theset:
  print(yea!!)
else:
  print(No!!)
```

- Once the set is created we can also add items and other literals to the set

```python
a={12,23,'amar',True,0}
a.add('orange')
print(a)
>>> {'orange',23,'amar',12,True,0}

# add using update() - upadte chnages the orginal set and doesn't create new set.

a={2,45,'amar',True,False}
b={34,True,False,'amar',33.98}
a.update(b)
print(a)
>>> {2,'amar',34,True,False,33.98,45}

#union() - you can create a new set by joining the items of two sets. we can also use (|) instead of union()
a={'orange','apple'}
b={'watermelon','kiwi'}
c = a.union(b)
print(c)
>>> {'watermelon','orange','kiwi','apple'}

# intersection() - to keep only the Duplicates. will return a new set. we can also use & instead of intersection()
a={'amar',23,'hello'}
b={'amar',4,90.88}
c=a.intersection(b)
print(c)
>>> {'amar'}
```

- To remove an item from the set we use Remove(), discard() clear() and del
- The empty set is always represented as ‘set()’

```python
a={'banana','orange','apple','watermelon','kiwi'}
a.remove('banana')
print(a)
>>> {'kiwi','apple','watermelon','orange'}

a.clear()
print(a)
>>> set()

del a
print(a)
>>> error.
```

## Dictionaries in Python

- Dictionaries are used to store key: value pairs.
- Dictionaries are the collection of ordered, Mutable, and do not allow duplicates.

```python
a={'amar':'chintu','dhruthi':'dru','Hridya':'happy'}
print(a)
>>> {'amar':'chintu','dhruthi':'dru','Hridya':'happy'}

print(a["amar"])
>>> 'chintu'

# We can get the value without using the []
print(a.get('Hridya'))
>>> 'Happy'

# We can get only the keys()
print(a.keys())
>>> dict_keys(['amar','dhruthi','Hridya'])

# we can get only the values()
print(a.values())
>>> dict_keys(['chintu','dru','happy'])

# The items() method will return each item in a dictionary, as tuples in a list.
print(a.items())
>>> ([('amar','chintu'),('dhruthi','dru'),('Hridya','happy')])

```

- Looping in dictionaries

```python
for x in a:
  print(x)
>>> {'amar':'chintu','dhruthi':'dru','Hridya':'happy'}

# we can also loop through keys and values
for x in a.keys():
  print(x)
>>>
---------------------
for x in a.values():
  print(x)
>>>
------------------------------------
for keys,value in a.items():
  print(keys,values)
  
>>> amar chintu
>>> happy hridya
>>> dhruthi dru
>>> mama ajju
```

- To add new values to the dictionaries we use update()

```python
a={'watermelon':'green','kiwi':'dotted','apple':'red'}
a['mango']='yellow'

print(a)
>>> {'watermelon':'green','kiwi':'dotted','apple':'red','mango':'yellow'}

# Are else we can use update()
a.update({'banana':'goldenyellow')
print(a)
>>> 
```

- To remove an item from the dict

```python
# we use pop()
a.pop('banana')
a.popitem() -- removes last inserted item
```

## NumPy Array:

Numpy is a general-purpose array processing package. It provides high-performance multidimensional array objects and tools for working with arrays. This is a reference type(mutable).

What is an Array?

An array is a data structure that stores the values of the same data type. This is the main difference between an array and a list. 

```python
## To install NumPy we use command
pip install numpy 

## to create an array 
import numpy as np
my_list = [1,2,3,4,5,6]

print(my_arr)
my_arr = np.array(my_list)
print(my_arr)
#o/p:- [1 2 3 4 5 6]
#o/p:- (6,)    represents Columns 

## creating two dimensional
my_list = [1,2,3,4]
my_list2 = [5,6,7,8]
my_list3 = [8,9,0,11]

my_arr1 = np.array([my_list,my_list2,my_list3])
print(my_arr1)
print(np.shape(my_arr1))
print(my_arr.reshape())

#o/p:-[[1,2,3,4],
       [5,6,7,8],
       [8,9,10,11]]
#o/p:- (3,4)

## reshaping the array.
print(my_arr1.reshape(4,3))
#o/p:- [[123]
        [456]
        [788]
        [91011]]

## indexing in single and multidimensional arrays
my_arr[0]
#o/p:- 1

my_arr1[0:2,0:2]
#o/p:- [[1,2]
        [5,6]]

 ## arange in numpy (array)
 print(np.arange(1,10))
 #o/p:- 1,2,3,4,5,6,7,8,9 
 
 ## linspace to get the points in the space between given range.
 print(np.linspace(1,2,50))
 # o/p:- we will get equally spaced 50 points between 1,2.

## copy function and brodcasting
arr=[1 2 3 4 5 6 ]

arr1 = arr
arr[0]=12
print(arr1)
# o/p:- [12 2 3 4 5 6]
### this is because arrays in numpy are mutable and reference type.
## so to overcome this we use copy function.

arr3 = [23 34 45 67 ]
arr4 = arr3.copy()
arr3[1] = [12]
print(arr3)
#o/p:- [23 12 45 67]
print(arr4)
# o/p:- [23 34 45 67] 

## How to create and reshape the array at once.
## to do that we have to create a single dimensional array (using arange().) and covert it into multi-dimensional.

my_arr = np.arange(1,6).reshape(3,6) 

## We also have random function etc.,
```


