
"""
Sebbene Python venga in genere considerato un linguaggio interpretato,
in realtà il codice sorgente non viene convertito direttamente in linguaggio macchina. I
nfatti passa prima da una fase di pre-compilazione in bytecode,
che viene quasi sempre riutilizzato dopo la prima esecuzione del programma,
evitando così di reinterpretare ogni volta il sorgente e migliorando le prestazioni.
(linguaggio interpretato -> un interprete è un programma
in grado di eseguire altri programmi
a partire direttamente dal relativo codice sorgente
scritto in un linguaggio di alto livello,
senza la previa compilazione dello stesso (codice oggetto),
eseguendo cioè le istruzioni nel linguaggio usato traducendole di volta in volta
in istruzioni in linguaggio macchina del processore.)

To test a short amount of code in python sometimes it is quickest and easiest not to write the code in a file.
This is made possible because Python can be run as a command line itself.
scrivi python3 su terminale
"""

"""
Print is a function and includes newline
print("This line will be printed.")
"""

"""
Python does not use curly braces but it uses indentation 
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
"""

"""
Python is completely object oriented, and not "statically typed".
You do not need to declare variables before using them, or declare their type.
Every variable in Python is an object.
Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals). 
myint = 7
print(myint)
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
"""

"""
STRINGS
"""

"""
Strings are defined either with a single quote or a double quotes.
using double quotes makes it easy to include apostrophes 
(whereas these would terminate the string if using single quotes)
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
There are additional variations on defining strings that make it easier to include things such as 
carriage returns, backslashes and Unicode characters. 
These are beyond the scope of this tutorial, but are covered in the Python documentation.
"""

"""
START_PYTHON DOCUMENTATION
"""

"""
In the interactive interpreter, the output string is enclosed in quotes 
and special characters are escaped with backslashes.
The print() function produces a more readable output, 
by omitting the enclosing quotes and 
by printing (nel senso che compiono la loro azione) escaped and special characters.
If you don’t want characters prefaced by \ to be interpreted as special characters, 
you can use raw strings by adding an r before the first quote.
"""

"""
String literals can span multiple lines, TRIPLE QUOTES
\ per non andare a capo 
End of lines are automatically included in the string, 
but it’s possible to prevent this by adding a \ at the end of the line.
"""
#print("""
#Usage: thingy [OPTIONS]\
#     -h                        Display this usage message
#     -H hostname               Hostname to connect to
#""")

"""
Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 * 'un' + 'ium')
Two or more string literals (i.e. the ones enclosed between quotes) 
next to each other are automatically concatenated.
print('Py' 'thon')
This only works with two literals though, not with variables or expressions 
(var prefix contiene py, non puoi unirla a stringa thon mettendole accanto)
If you want to concatenate variables or a variable and a literal, use +
Strings can be indexed (subscripted), with the first character having index 0. 
There is no separate character type; a character is simply a string of size one:
word[0]
Indices may also be negative numbers, to start counting from the right:
word[-1] last
word[-2] second last
Note that since -0 is the same as 0, negative indices start from -1
In addition to indexing, slicing is also supported. 
While indexing is used to obtain individual characters, slicing allows you to obtain substring:
word[0:2] 0 included 2 excluded
an omitted first index defaults to zero, 
word[:2]
an omitted second index defaults to the size of the string being sliced.
word[2:]
word[-2:]
start is always included, and the end always excluded -> s[:i] + s[i:] is always equal to s, 
altrimenti carattere di indice i si ripeterebbe (?)
One way to remember how slices work is to think of the indices as pointing between characters, 
with the left edge of the first character numbered 0. 
Then the right edge of the last character of a string of n characters has index n, for example:
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
The slice from i to j consists of all characters between the edges labeled i and j
For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds.
Attempting to use an index that is too large will result in an error
word[42]  # the word only has 6 characters
IndexError: string index out of range
However, out of range slice indexes are handled GRACEFULLY when used for slicing:
>>> word[4:42]
'on'
>>> word[42:]
''
"""

"""
Python strings cannot be changed — they are immutable. 
Therefore, assigning to an indexed position in the string results in an error:
word[0] = 'J'
TypeError: 'str' object does not support item assignment
If you need a different string, you should create a new one
The built-in function len() returns the length of a string, obv including puntuation and spaces...
"""

"""
END_PYTHON DOCUMENTATION
"""

"""
Simple operators can be executed on numbers and strings
one = 1
two = 2
three = one + two
print(three)
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3, 4
Mixing operators between numbers and strings is not supported
"""

"""
LISTS
"""

"""
Lists are very similar to arrays. 
They can contain any type of variable, and they can contain as many variables as you wish. 
Lists can also be iterated over in a very simple manner. 
Here is an example of how to build a list.
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3 te la stampa andando a capo, uno per uno
for x in mylist:
    print(x)
    
se fai 
print(mylist)
te la stampa come una lista, tra le parentesi quadre, tutte di fila, separate da virgola, più carino
    
Accessing an index which does not exist generates an exception (an error).
"""

"""
BASIC OPERATORS
"""

"""
Just as any other programming languages, 
the addition, subtraction, multiplication, and division operators 
can be used with numbers.
number = 1 + 2 * 3 / 4.0
print(number) 
fa 2.5 (6 diviso 4, più 1) quindi python  follow order of operations
Another operator available is the modulo (%) operator, which returns the integer remainder of the division
Using two multiplication symbols makes a power relationship
squared = 7 ** 2
cubed = 2 ** 3
Python supports concatenating strings using the addition operator:
helloworld = "hello" + " " + "world"
Python also supports multiplying strings to form a string with a repeating sequence:
lotsofhellos = "hello" * 10
Lists can be joined with the addition operators:
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
print([1,2,3] * 3) per ripetere elemento dentro la lista, l'operatore * fuori dalla lista
output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
x = object()
name_list.count(x) conte le istanze di x dentro la lista
"""

"""
STRING FORMATTING
"""

"""
Python uses C-style string formatting to create new, formatted strings. 
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
together with a format string, which contains normal text together with "argument specifiers", 
special symbols like "%s" and "%d".
# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)
To use two or more argument specifiers, use a tuple (parentheses):
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))
puoi anche passare una sola lista che li contiene tutti, li mette in ordine
Any object which is not a string can be formatted using the %s operator as well. 
The string which returns from the "repr" method of that object is formatted as the string. 
PUOI STAMPARE (TUTTE LE) COSE CHE NON SONO UNA STRINGA SOTTO FORMA DI STRINGA SENZA TANTI PROBLEMI
For example:
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)
ris = 3.3
print("The result is: %s" % ris) FUNZIONA ANCHE SE HAI MESSO s INVECE CHE f

%s - String (or any object with a string representation, like numbers)

%d - Integers    

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
f al posto dell'ultimo s funziona ma number of digits no, problemi con <> (?)
print(format_string % data)
output:  Hello John Doe. Your current balance is $53.44.
"""

"""
BASIC STRING OPERATIONS
"""

"""
Strings are bits of text. They can be defined as anything between quotes
len(string) lunghezza della stringa con punt and spaces
string.index("o") indice di PRIMA occorrenza di o 
string.count("o") conta occorrenze di o
print(string[3:7]) 3 incl, 7 escl (casi particolari sopra in python documentation)
print(astring[3:7])
print(astring[3:7:1])
entrambi producono lo stesso output
sintassi: [start:stop:step]
print(astring[3:7:2])
salta un carattere
print(astring[::-1])
per stampare reverse (?)
astring = "Hello world!"
print(astring.upper()) output: HELLO WORLD
print(astring.lower()) output: hello world
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
This is used to determine whether the string starts with something or ends with something, respectively. 
The first one will print True, as the string starts with "Hello". 
The second one will print False, as the string certainly does not end with "asdfasdfasdf".
astring = "Hello world!"
afewwords = astring.split(" ")
This splits the string into a bunch of strings grouped together in a list. 
Since this example splits at a SPACE, the first item in the list will be "Hello", and the second will be "world!".
odd means dispari
"""

"""
CONDITIONS
"""

"""
Python uses boolean logic to evaluate conditions. 
The boolean values True and False are returned when an expression is compared or evaluated.
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
Notice that variable assignment is done using a single equals operator "=", 
whereas comparison between two variables is done using the double equals operator "==". 
The "not equals" operator is marked as "!=".
The "and" and "or" boolean operators allow building complex boolean expressions, for example:
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
The "in" operator could be used to check if a specified object exists within an iterable object container, 
such as a list:
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
Python uses indentation to define code blocks, instead of brackets. 
The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent. 
Notice that code blocks do not need any termination.
pass (?)
A statement is evaulated as TRUE if one of the following is correct: 
1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 
2. An object which is not considered "empty" is passed. 
Here are some examples for objects which are considered as EMPTY: 
1. An empty string: "" 2. An empty list: [] 3. The number zero: 0 4. The false boolean variable: False
Unlike the double equals operator "==", the "is" operator does not match the values of the variables, 
but the INSTANCES themselves. For example:
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
Using "not" before a boolean expression inverts it
"""

"""
LOOPS
There are two types of loops in Python, for and while.
FOR loops iterate over a given sequence. Here is an example:
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. 
The difference between range and xrange is that the range function returns a new list with numbers of that specified range, 
whereas xrange returns an ITERATOR, which is more efficient. 
(Python 3 uses the RANGE FUNCTION, which acts like xrange). 
Note that the range function is ZERO BASED. (estremo sx included, dx excluded)
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
WHILE loops repeat as long as a certain boolean condition is met.
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
BREAK is used to exit a for loop or a while loop, 
whereas CONTINUE is used to skip the current block, and return to the "for" or "while" statement. 
A few examples:
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:  # se è pari non lo stampa, non fa istruzione dopo, torna alla guardia for
        continue
    print(x)
Unlike languages like C,CPP.. we can use ELSE for loops. 
Quando esco dal ciclo perché condizione è diventata falsa eseguo else, se esco per break non eseguo else
When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
If a break statement is executed inside the for loop then the "else" part is skipped. 
Note that the "else" part is executed even if there is a continue statement. (?) (condizione è falsa, perciò dovrei uscire, ma c'è continue, eseguo comunque else)
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
RICORDA DUE PUNTI AL POSTO DI DOVE USERESTI PARENTESI
punti e virgola non esistono
i++ non esiste, scrivi i+=1
"""

"""
FUNCTIONS
"""

"""
Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. 
Also functions are a key way to define interfaces so programmers can share their code.
Python makes use of blocks.
block_head:
    1st block line
    2nd block line
    ...
Where a block line is more Python code (even another block), 
and the block head is of the following format: block_keyword block_name(argument1,argument2, ...) 
Block keywords you already know are "if", "for", and "while".
Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. 
For example:
def my_function():
    print("Hello From My Function!")
Functions may also receive arguments (variables passed from the caller to the function). 
For example:
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
Functions may return a value to the caller, using the keyword- 'return' . 
For example:
def sum_two_numbers(a, b):
    return a + b
To call function in Python: simply write the function's name followed by (), 
placing any required arguments within the brackets.
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1,2)
"""

"""
OBJECTS
"""

"""
Objects are an encapsulation of variables and functions into a single entity. 
Objects get their variables and functions from classes. 
Classes are essentially a template to create your objects.
A very basic class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
We'll explain why you have to include that "self" as a parameter
To assign the above class(template) to an object you would do the following:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
Now the variable "myobjectx" holds an object of the class "MyClass" 
that contains the variable and the function defined within the class called "MyClass".
To access the variable inside of the newly created object "myobjectx" you would do the following:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjectx.variable
You can create multiple different objects that are of the same class(have the same variables and functions defined). 
However, each object contains independent copies of the variables defined in the class.
Modifichi una delle due copie, altra rimane uguale.
To access (call) a function
myobjectx.function()
RICORDA PER LE STRINGHE LE VIRGOLETTE
RICORDA DI ISTANZIARE L'OGGETTO
diecimila non si scrive 10,000 ma 10000
"""

"""
DICTIONARIES
"""

"""
A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. 
Each value stored in a dictionary can be accessed using a key, 
which is any type of object (a string, a number, a list, etc.) 
instead of using its index to address it.
database of phone numbers
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
Alternatively, a dictionary can be initialized with the same values in the following notation:
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, does not keep the order of 
the values stored in it. To iterate over key value pairs, use the following syntax:
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
To remove a specified index, use either one of the following notations:
del phonebook["John"]
phonebook.pop("John")
To add
non c'è add append... semplicemente fai dizionario[chiave nuova] = valore nuovo
"""

"""
MODULES AND PACKAGES
"""

"""
In programming, a MODULE is a piece of software that has a specific functionality. 
For example, when building a ping pong game, one module would be responsible for the game logic, and
another module would be responsible for drawing the game on the screen. 
Each module is a different file, which can be edited separately.
Modules in Python are simply Python files with a .py extension. The name of the module will be the name of the file.
A Python module can have a set of functions, classes or variables defined and implemented. 
mygame/
mygame/game.py
mygame/draw.py
The Python script game.py will implement the game. It will use the function draw_game from the file draw.py,
or in other words, thedraw module, that implements the logic for drawing the game on the screen.
Modules are imported from other modules using the import command. In this example, 
the game.py script may look something like this:
# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
The draw module may look something like this:
# draw.py

def draw_game():
    ...

def clear_screen(screen):
    ...
In this example, the game module IMPORTS the draw module, which enables it to use functions implemented in that module. 
The main function would use the local function play_game to run the game, and then draw the result of the game using a 
function implemented in the draw module called draw_game. 
To use the function draw_game from the draw module, we would need to specify in which module the function is implemented,
using the DOT OPERATOR. To reference the draw_game function from the game module, we would need to import the draw 
module and only then call draw.draw_game(). 
When the import draw directive will run, the Python interpreter will look for a file in the DIRECTORY which the script 
was executed from, by the name of the module with a .py suffix, so in our case it will try to look for draw.py. 
If it will find one, it will import it. If not, he will continue to look for built-in modules.
You may have noticed that when importing a module, a .pyc file appears, which is a compiled Python file. 
Python compiles files into Python BYTECODE so that it won't have to parse the files each time modules are loaded. 
If a .pyc file exists, it gets loaded instead of the .py file, but this process is TRANSPARENT to the user.

We may also import the function draw_game directly into the main script's namespace, by using the from command.
# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)
You may have noticed that in this example, draw_game does not precede with the name of the module it is imported from, 
because we've specified the module name in the import command.
The advantages of using this notation is that it is easier to use the functions inside the current module because 
you don't need to specify which module the function comes from.
However, any namespace cannot have two objects with the exact same name, so the import command may replace an existing 
object in the namespace.
We may also use the import * command to import all objects from a specific module, like this:
# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)
This might be a bit risky as changes in the module might affect the module which imports it, 
but it is shorter and also does not require you to specify which objects you wish to import from the module.
We may also load modules under any name we want.
This is useful when we want to import a module conditionally to use the same name in the rest of the code. 
For example, if you have two draw modules with slighty different names - you may do the following:
# game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)
The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. 
If another module in your code imports the same module again, it will not be loaded twice but once only 
- so LOCAL VARIABLES INSIDE the module act as a "SINGLETON" - they are initialized only once.
This is useful to know, because this means that you can rely on this behavior for initializing objects. For example:
# draw.py

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# INITIALIZE MAIN_SCREEN AS A SINGLETON
main_screen = Screen()

There are a couple of ways we could tell the Python interpreter where to look for modules, aside from the default, 
which is the local directory and the built-in modules. 
METHOD 1 (?)
You could either use the environment variable PYTHONPATH to specify additional directories to look for modules in, 
like this:
PYTHONPATH=/foo python game.py (?)
This will execute game.py, and will enable the script to load modules from the foo directory as well as the local directory.
METHOD 2    FUNZIONA
Another method is the sys.path.append function. You may execute it BEFORE running an IMPORT command:
sys.path.append("/foo") questo va bene se foo si trova in cwd, altrimenti devi specificare percorso preciso da cwd
This will add the foo directory to the list of paths to look for modules in as well.

You don't set PYTHONPATH, you add entries to sys.path. 
It's a list of directories that should be searched for Python packages, 
so you can just append your directories to that list.
sys.path.append('/path/to/whatever')
In fact, sys.path is initialized by splitting the value of PYTHONPATH on the path separator character 
(: on Linux-like systems, ; on Windows).

Check out the full list of BUILT-IN MODULES in the Python standard library here.
Two very important functions come in handy when exploring modules in Python - the dir and help functions.
If we want to import the module urllib, which enables us to create read data from URLs, we simply import the module:
# import the library
import urllib
# use it
urllib.urlopen(...)
per trovarsi a interagire da terminale, trovarsi inside the python interpreter (>>>) scrivi python3 su terminale, 
per uscire ctrl z
We can look for which functions are implemented in each module by using the dir function:
>>> import urllib
>>> dir(urllib)
When we find the function in the module we want to use, we can read about it more using the help function, 
inside the Python interpreter:
help(urllib.urlopen)

Writing PACKAGES
Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, 
but with a twist.
Each package in Python is a directory which MUST contain a special file called __init__.py
nome della directory è nome del package, dentro package ho file init e altri file.py che sono moduli (submodules)
package diversi possono avere moduli con stesso nome, saranno moduli diversi che differiscono anche di nome grazie a 
dot notation
This file can be empty, and it indicates that the directory it contains is a Python package, 
so it can be imported the same way a module can be imported. 
Il file __init__.py può anche contenere codice che viene eseguito ogni volta che package importato.
If we create a directory called foo, which marks the package name, 
we can then create a module inside that package called bar. 
We also must not forget to add the __init__.py file inside the foo directory.
To use the module bar, we can import it in two ways:
import foo.bar
from foo import bar
In the first method, we must use the foo prefix whenever we access the module bar. In the second method, we don't, 
because we import the module to our module's namespace.
The __init__.py file can also decide which modules the package exports as the API, 
while keeping other modules internal, by overriding the __all__ variable, like so:
__init__.py:

__all__ = ["bar"] # sto esportando solo il modulo bar del package  (?)

assuming that the directory simple_package is either in the directory from which you call the shell 
or that it is contained in the search path or environment variable "PYTHONPATH" (from your operating system)

import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))

aggiungere a array, APPEND
eliminare da array, POP(indice) o REMOVE(elemento), remove rimuove solo prima occorrenza
esiste funzione sorted
"""

"""
NUMPY ARRAYS
"""

"""
Numpy arrays are great alternatives to Python Lists. Some of the key advantages of Numpy arrays are that they are fast, 
easy to work with, and give users the opportunity to perform calculations across entire arrays.
In the following example, you will first create two Python lists. Then, you will import the numpy package and create 
numpy arrays out of the newly created lists.
NumPy è una libreria open source per il linguaggio di programmazione Python, che aggiunge supporto a grandi matrici e 
array multidimensionali insieme a una vasta collezione di funzioni matematiche di alto livello per poter operare 
efficientemente su queste strutture dati. 
Per avere questa libreria devi usare PIP
Se PIP non funziona usa anaconda, che è distribuzione di python che già di suo supporta numpy


# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
print(type(np_height)) (?)

BMI = indice di massa corporea = peso / qudrato di altezza
Now we can perform element-wise calculations on height and weight. For example, you could take all 6 of the height and 
weight observations above, and calculate the BMI for each observation with a single equation. These operations are very 
fast and computationally efficient. They are particularly helpful when you have 1000s of observations in your data.
Sono 6 osservazioni sullo stesso individuo
bmi = np_weight / np_height ** 2  QUANDO STAMPI BMI È UN ARRAY CON 6 POSIZIONI OGNUNA CONTENTE RISULTATO
print(bmi) # stampa array con 6 posizioni ognuna ris
print(bmi > 23) # stampa array con 6 pos ognuna true o false in base a se bmi > 23
print(bmi[bmi > 23]) # stampa solo pos con bmi > 23
Another great feature of Numpy arrays is the ability to subset. For instance, if you wanted to know which observations 
in our BMI array are above 23, we could quickly subset it to find out.
# For a boolean response
bmi > 23 (?)
# Print only those observations above 23
bmi[bmi > 23]
"""

"""
PANDAS BASICS
"""

"""
Pandas is a high-level data manipulation tool developed by Wes McKinney. 
It is built on the Numpy package and its key data structure is called the DataFrame. 
DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.
There are several ways to create a DataFrame. One way way is to use a DICTIONARY. For example:
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
As you can see with the new brics DataFrame, Pandas has assigned a key for each country 
as the numerical values 0 through 4. If you would like to have different INDEX VALUES, say, the two letter country code,
 you can do that easily as well.
 # Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)
Another way to create a DataFrame is by importing a CSV file using Pandas. Now, the csv cars.csv is stored and can be 
imported using pd.read_csv:
csv file -> Il comma-separated values è un formato di file basato su file di testo utilizzato per l'importazione 
ed esportazione di una tabella di dati.
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

There are several ways to INDEX a Pandas DataFrame. 
One of the easiest ways to do this is by using square bracket notation.
In the example below, you can use square brackets to select one column of the cars DataFrame. 
You can either use a single bracket or a double bracket. 
The SINGLE bracket will output a Pandas Series, while a DOUBLE bracket will output a Pandas DataFrame.
Pandas Series -> One-dimensional ndarray with axis labels (?)    NON PUOI STAMPARE PIÙ DI UNA COLONNA
# Import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series    NON PUOI STAMPARE PIÙ DI UNA COLONNA, mette indici ma non titolo
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame  PUOI STAMPARE PIÙ DI UNA COLONNA (te le da con ordine che specifichi) infatti guarda esempio dopo, indici e titolo
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])
Square brackets can also be used to access observations (ROWS) from a DataFrame. For example:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0) (?)

# Print out first 4 observations
print(cars[0:4])

# Print out fifth and sixth observation
print(cars[4:6])
You can also use loc and iloc to perform just about any data selection operation. 
LOC (USALO SOLO SE HAI DATO INDICI ALTERNATIVI A NUMERI?) is label-based, which means that you have to specify rows and columns based on their row and column labels. 
ILOC (INDEX) is integer index based, so you have to specify rows and columns by their integer index like you did 
in the previous exercise.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2]) (?) è automatico che 2 indica la riga

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']]) (?) è automatico che indica riga
"""

"""
GENERATORS
"""

"""
Generators are very easy to implement, but a bit difficult to understand.

Generators are used to create iterators, but with a different approach. 
Generators are simple FUNCTIONS which return an iterable set of items, ONE ITEM AT A TIME, in a special way.
When an iteration over a set of item starts using the for statement, the generator is run. 
Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop,
returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants, 
yielding each one in its turn.
Here is a simple example of a generator function which returns 7 random integers:
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
       
# a ogni esecuzione lottery ret un numero, tramite for e poi ultimo #
# ! all'esecuzione i+1 riprende da esecuzione i, non riparte da capo ! #
This function decides how to generate the random numbers on its own, and executes the yield statements one at a time, 
pausing in between to yield execution back to the main for loop.

esercizio non fatto
"""

"""
LIST COMPREHENSION
"""

"""
List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.

Quindi, una List Comprehension è creata utilizzando delle parentesi quadre contenenti al loro interno un'espressione, un ciclo for ed eventuali if se necessari.

For example, let's say we need to create a list of integers which specify the length of each word in a certain sentence, 
but only if the word is not the word "the".
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)
Using a list comprehension, we could SIMPLIFY this process to this notation:
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
  
# Using list comprehension
[print(i) for i in list]
"""

"""
MULTIPLE FUNCTION ARGUMENTS
"""

"""
*args, **kwds
*args, **kwargs !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Every function in Python receives a predefined number of arguments, if declared normally, like this:
def myfunction(first, second, third):
    # do something with the 3 variables
    ...
It is possible to declare functions which receive a variable number of arguments, using the following syntax:
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))
The "therest" variable is a list of variables, which receives all arguments which were given to the "foo" function 
after the first 3 arguments. So calling foo(1, 2, 3, 4, 5) will print out:
First: 1
Second: 2
Third: 3
And all the rest... [4, 5]
It is also possible to send functions arguments by KEYWORD, so that the order of the argument does not matter, 
using the following syntax. The following code yields the following output: The sum is: 6 Result: 1
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
The "bar" function receives 3 arguments. If an additional "action" argument is received, and it instructs on summing up 
the numbers, then the sum is printed out. Alternatively, the function also knows it must return the first argument, 
if the value of the "number" parameter, passed into the function, is equal to "first".
# edit the functions prototype and implementation
def foo(a, b, c, *args):
    return len(args)    # non c'+ bisogno di specificare che è lista

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7   # ritorna booleano


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
    
if():
elif():
else:
"""

"""
REGULAR EXPRESSIONS
"""

"""
A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check 
if a particular string matches a given regular expression (or if a given regular expression matches a particular string, 
which comes down to the same thing).

import re
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
# Your pattern here!
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)

output: passano tutte
"""

"""
EXCEPTIONS
"""

"""
When programming, errors happen. It's just a fact of life. Perhaps the user gave bad input. 
Maybe a network resource was unavailable. Maybe the program ran out of memory. 
Or the programmer may have even made a mistake!
Python's solution to errors are exceptions. You might have seen an exception before.
print(a)
#error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
</module></stdin>
Oops! Forgot to assign a value to the 'a' variable.
But sometimes you don't want exceptions to completely stop the program. 
You might want to do something special when an exception is raised. This is done in a try/except block.
Here's a trivial example:
Suppose you're iterating over a list. You need to iterate over 20 numbers, but the list is made from user input, 
and might not have 20 numbers in it. After you reach the end of the list, you just want the rest of the numbers 
to be interpreted as a 0. Here's how you could do that:
def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()

# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name(): 
    return actor["name"].split(" ")[1]
    

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())

"""

"""
SETS
"""

"""
Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:
print(set("my name is Eric and Eric is my name".split()))
This will print out a list containing "my", "name", "is", "Eric", and finally "and". 
Since the rest of the sentence uses words which are already in the set, they are not inserted twice.
Sets are a powerful tool in Python since they have the ability to calculate differences and intersections between other 
sets. For example, say you have a list of participants in events A and B:
a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)
To find out which members attended both events, you may use the "INTERSECTION" method:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))
To find out which members attended only one of the events, use the "SYMMETRIC_DIFFERENCE" method:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
stampano la stessa cosa

To find out which members attended only one event and not the other, use the "DIFFERENCE" method:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.difference(b))
print(b.difference(a))
stampano due cose diverse, il primo quelli in a e non in b, il secondo quelli in b e non in a

To receive a list of all participants, use the "UNION" method:
a = set(["Jake", "John", "Eric"])   # devi trasformarli in set altrimenti non funziona !
b = set(["John", "Jill"])
print(a.union(b))
"""

"""
SERIALIZATION
"""

"""
Python provides built-in JSON libraries to encode and decode JSON.
In Python 2.5, the simplejson module is used, whereas in Python 2.7, the json module is used. 
Since this interpreter uses Python 2.7, we'll be using json.
In order to use the json module, it must first be imported:
import json
There are two basic formats for JSON data. Either in a string or the object datastructure. 
The OBJECT DATASTRUCTURE, in Python, consists of lists and dictionaries nested inside each other. 
The object datastructure allows one to use python methods (for lists and dictionaries) to add, list, search and 
remove elements from the datastructure.
The STRING format is mainly used to pass the data into another program or load into a datastructure.

FROM JSON TO PYTHON     JSON STRING -> LOADS -> PYTHON DICTIONARY
To load JSON back to a data structure, use the "LOADS" method. This method takes a STRING
and turns it back into the JSON OBJECT DATASTRUCTURE:
import json 
print(json.loads(json_string))
oppure esempio su altro tutorial

FROM PYTHON TO JSON     PYTHON OBJECT -> DUMPS -> JSON STRING
To encode a data structure to JSON, use the "DUMPS" method. This method takes an OBJECT and returns a STRING:
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
oppure esempio su altro tutorial

JSON STRING = JSON OBJ glie lo passi e funziona

Python supports a Python proprietary data serialization method called PICKLE (and a faster alternative called cPickle).
You can use it exactly the same way. (== JSON)
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries_python = json.loads(salaries_json)
    salaries_python[name] = salary
    salaries_json = json.dumps(salaries_python)

    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
"""

"""
PARTIAL FUNCTIONS
"""

"""
You can create partial functions in python by using the partial function from the functools library.
Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values 
set for the more limited function.
Import required:
from functools import partial
from functools import partial

def multiply(x, y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))
An IMPORTANT note: the default values will start replacing variables from the left. 
The 2 will replace x. y will equal 4 when dbl(4) is called.
in questo esempio non crea differenze (2*4 = 4*2), 
ma in quello sotto sì

#Following is the exercise, function provided:
from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x
p_func = partial(func, 5, 5, 5)
print(p_func(15))
"""

"""
CODE INTROSPECTION
"""

"""
Code introspection is the ability to examine classes, functions and keywords 
to know what they are, what they do and what they know.
Python provides several functions and utilities for code introspection.
help()
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance() 
__doc__ 
__name__
Often the most important one is the help function, since you can use it to find what other functions do.
# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
print(dir(Vehicle))
"""

"""
CLOSURES
"""

"""
technique by which the data is attached to some code even after end of those other original functions 
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
Firstly, a NESTED FUNCTION is a function defined inside another function. It's very important to note that the nested 
functions can access the variables of the enclosing scope. However, at least in python, they are only readonly. However, 
one can use the "NONLOCAL" keyword explicitly with these variables in order to modify them.
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter() # sta dentro funz transmit_to_space

print(transmit_to_space("Test message"))

This works well as the 'data_transmitter' function can access the 'message'. 
To demonstrate the use of the "nonlocal" keyword, consider this
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)

sta accedendo a number funzione esterna print_msg quando fa print(number), non la funzione nested printer
funzione più esterna non potrebbe farlo, ma c'è nonlocal quindi può  (?)
Without the nonlocal keyword, the output would be "3 9", however, with its usage, we get "3 3", that is the value 
of the "number" variable gets modified.
Now, how about we RETURN THE FUNCTION OBJECT rather than calling the nested function within. 
(Remember that even FUNCTIONS are OBJECTS. (It's Python.))
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter
    
And we call the function as follows:
fun2 = transmit_to_space("Burn the Sun!")
fun2()
Even though the execution of the "transmit_to_space()" was completed, the message was rather preserved. 
This technique by which the data is attached to some code even after end of those other original functions 
is called as closures in python
ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.
(Eg. When there are few methods in a class, use closures instead).
Also, Decorators in Python make extensive use of closures.
def multiplier_of(n):
# enclosure func
    def multiplier(number):
    # nested fun
        return number*n # nested func può ritornare roba
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
"""

"""
DECORATORS
"""

"""
Put simply: decorators wrap a function, modifying its behavior.
una funzione che prende come parametro un’altra funzione, aggiunge delle funzionalità e restituisce un’altra funzione, 
senza appunto, alterare il codice sorgente della funzione passata come parametro.
Questo è possibile per il fatto che in Python, le funzioni sono First Class Objects il che significa in maniera molto 
sintetica, che possono essere passate come parametro e restituite come qualsiasi altro valore, definite all’interno di 
altre funzioni (nel qual caso si parla di funzioni annidate) e assegnate a delle variabili.

def funzione_decoratore(funzione_parametro):
    def wrapper():
         nome convenzionale - wrapper significa 'incarto, confezione' 
        print("... codice da eseguire prima di 'funzione_parametro' ...")
        funzione_parametro()
        print("... codice da eseguire dopo di 'funzione_parametro' ...")
    return wrapper

def mia_funzione():
    print("Hello World!")

mia_funzione = funzione_decoratore(mia_funzione)

mia_funzione()
output:
... codice da eseguire prima di funzione_parametro ...
Hello World!
... codice da eseguire dopo di funzione_parametro ...

equivalent to

@funzione_decoratore
def mia_funzione():
    print("Hello World!")

mia_funzione()
# output:

... codice da eseguire prima di funzione_parametro ...
hello world!
... codice da eseguire dopo di funzione_parametro ...

sostituire una funzione con un’altra.
    
decorator is just another function which takes a functions and returns one
In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, 
just like any other object (string, int, float, list, and so on). 
Decorators allow you to make simple modifications to callable objects like functions, methods, or classes. 
We shall deal with functions for this tutorial. The syntax
@decorator
def functions(arg):
    return "value"
Is EQUIVALENT to:
def function(arg):
    return "value"
The so-called decoration happens at the following line: ->
function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions
As you may have seen, a decorator is just another function which takes a functions and returns one. 
For example you could do this:
def repeater(old_function):
    def new_function(*args, **kwds): # See learnpython.org/en/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value
The *args and **kwargs keywords allow you to pass a variable number of arguments to a Python function. 
The *args keyword sends a list of values to a function. **kwargs sends a dictionary with values associated 
with keywords to a function. 
This would make a function repeat twice.
>>> @repeater
def multiply(num1, num2):
    print(num1 * num2)

>>> multiply(2, 3)
6
6
You can also make it change the output
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) # modify the return value
    return new_function
change input
def double_Ii(old_function):
    def new_function(arg): # only works if the old function has one argument
        return old_function(arg * 2) # modify the argument passed
    return new_function
and do checking.
def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument") # This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function

funzione1 che prende in input una funzione2 e la fa qualcosa 
(quel qualcosa è definito in new function, che è valore ritornato da funzione1)


def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num
EQUIVALENT TO return_num = multiply(3)(return_num)
# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15   !!!!!!!!!!!!!!!!!!!!!
il multiplier è 3 
la new function ritorna 3*old function()
la old function è return num(5) che ritorna 5
3*5 = 15

il decorator multiply(3) prende in input la old function return_num(5)

def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])

Note that the order in which the inner functions are defined does not matter. Like with any other functions, 
the printing only happens when the inner functions are executed. (?)
Note that you are returning first_child without the parentheses. 
Recall that this means that you are returning a REFERENCE to the function first_child.
In contrast first_child() with parentheses refers to the result of EVALUATING the function.
Finally, note that in the earlier example you executed the inner functions within the parent function, 
for instance first_child(). However, in this last example, you did not add parentheses 
to the inner functions—first_child—upon returning. That way, you got a reference to each function that you could call 
in the future. Make sense?

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

say_whee = my_decorator(say_whee)
In effect, the name say_whee now points to the wrapper() inner function.
Remember that you return wrapper as a function when you call my_decorator(say_whee):

esercizio
def type_check(correct_type):
    def check_generator(old_function):
        def new_function(*args, **kwargs):
            if(isinstance(old_function(*args, **kwargs ),correct_type)):
                return old_function(*args, **kwargs)
            else:
                print("Bad Type")
        return new_function
    return check_generator
    
    chaining
    
@star
@percent
def printer(msg):
    print(msg)
    

printer("Hello")

equivalent

def printer(msg):
    print(msg)
printer = star(percent(printer))

ORDER MATTERS

This is also called metaprogramming because a part of the program tries to modify another part of the program 
at compile time.

DECORATOR CON ARGOMENTO OLTRE ALLA FUNZIONE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@type_check(int)
def times2(num):
    return num*2
    
# times2 = (type_check(int))(times2)

def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(old_function(arg),correct_type)):
                print(old_function(arg))
            else:
                print("Bad Type")
        return new_function
    return check
    
    il decoratore ha un argomento oltre alla old function, per questo motivo servono due funzioni interne, altrimenti ne basta una
    
DECORATOR CON SOLO UN ARGOMENTO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@decorator
def old_f(num):
    do something

equiv to

old_f = decorator(olf_f)

quando chiami old_f la chiami "DECORATA" cioè fa roba in più

def repeater(old_function):
    def new_function(*args, **kwds): # See learnpython.org/en/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value
    
PROPERTIES IN PYTHON
classe con variabile temperatura
non vuoi che vada sotto una certa soglia
la rendi privata (_temperature) e fai getter e settere che rispettano questo vincolo
However, the bigger problem with the above update is that all the programs that implemented our previous class have to modify their code from obj.temperature to obj.get_temperature() and all expressions like obj.temperature = val to obj.set_temperature(val).
This refactoring can cause problems while dealing with hundreds of thousands of lines of codes.
All in all, our new update was not backwards compatible. This is where @property comes to rescue.
temperature = property(get_temperature, set_temperature)
property object temperature. Simply put, property attaches some code (get_temperature and set_temperature) to the member attribute accesses (temperature).
any code that retrieves the value of temperature will automatically call get_temperature() instead of a dictionary (__dict__) look-up. Similarly, any code that assigns a value to temperature will automatically call set_temperature().
even when we created an object.
In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:
property(fget=None, fset=None, fdel=None, doc=None)
temperature = property(get_temperature, set_temperature)
equivalente a
# make empty property
temperature = property()
# assign fget
temperature = temperature.getter(get_temperature)
# assign fset
temperature = temperature.setter(set_temperature)
con decorators...

"""

"""
MAP FILTER REDUCE
Map, Filter, and Reduce are paradigms of functional programming. They allow the programmer (you) to write simpler, 
shorter code, without neccessarily needing to bother about intricacies like loops and branching.
Essentially, these three functions allow you to apply a function across a number of iterables, in one fell swoop.
map and filter come built-in with Python (in the __builtins__ module) and require no importing.
reduce, however, needs to be imported as it resides in the functools module.
"""

"""
MAP 
The map() function in python has the following syntax:
map(func, *iterables)
Where func is the function on which each element in iterables (as many as they are) would be applied on.
Notice the asterisk(*) on iterables? It means there can be as many iterables as possible,
in so far func has that exact number as required input arguments.
Before we move on to an example, it's important that you note the following:
1) In Python 2, the map() function returns a list. In Python 3, however, the function returns a map object which is a 
generator object. To get the result as a list, the built-in list() function can be called on the map object. 
i.e. list(map(func, *iterables))
2) The number of arguments to func must be the number of iterables listed. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Say I have a list (iterable) of my favourite pet names, all in lower case and I need them in uppercase. Traditonally, 
in normal pythoning, I would do something like this:
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)
Which would then output ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
With map() functions, it's not only easier, but it's also much more flexible. I simply do this:
# Python 3
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)
Which would also output the same result.
Note that using the defined map() syntax above, func in this case is str.upper and iterables is the my_pets list -- 
just one iterable. Also note that we did not call the str.upper function (doing this: str.upper()), 
as the map function does that for us on each element in the my_pets list.
What's more important to note is that the str.upper function requires only one argument by definition and so we passed 
just one iterable to it.
So, if the function you're passing requires two, or three, or n arguments, then you need to pass in two, three 
or n iterables to it. 
Say I have a list of circle areas that I calculated somewhere, all in five decimal places.
And I need to round each element in the list up to its position decimal places, meaning that I have to round up the 
first element in the list to one decimal place, the second element in the list to two decimal places, the third element 
in the list to three decimal places, etc.
Python already blesses us with the round() built-in function that takes two arguments -- the number to round up and the 
number of decimal places to round the number up to.
So, since the function requires two arguments, we need to pass in two iterables.
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))
range(1,7) = 1, 2, 3, 4, 5, 6

print(result)
The range(1, 7) function acts as the second argument to the round function (the number of required decimal places per 
iteration). So as map iterates through circle_areas, during the first iteration, the first element of circle_areas, 
3.56773 is passed along with the first element of range(1,7), 1 to round, making it effectively become round(3.56773, 1). 
During the second iteration, the second element of circle_areas, 5.57668 along with the second element of range(1,7), 
2 is passed to round making it translate to round(5.57668, 2). 
This happens until the end of the circle_areas list is reached.
I'm sure you're wondering: "What if I pass in an iterable less than or more than the length of the first iterable? 
And the answer is simple: nothing! Okay, that's not true. "NOTHING" happens in the sense that the map() function will 
not raise any exception, it will simply iterate over the elements until it can't find a second argument to the function, 
at which point it simply stops and returns the result.
Python simply stops when it can't find the next element in one of the iterables. 
To consolidate our knowledge of the map() function, we are going to use it to implement our own custom zip() function. 
The zip() function is a function that takes a number of iterables and then creates a tuple containing each of the 
elements in the iterables.
# Python 3

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)
I didn't even need to create a function using the def my_function() standard way
I simply used a lambda function.
This is not to say that using the standard function definition method (of def function_name()) isn't allowed, 
it still is. I simply preferred to write less code  (esempio con def in filter)

LAMBDA FUNCTION
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
lambda arguments : expression
x = lambda a, b : a * b
print(x(5, 6)) 
x mi rappresenta funzione
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n 
Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
!!! mydoubler prende quello che viene restituito da myfunc, ossia funzione lambda che ha un parametro
!!! perciò posso moltiplicare quel parametro (ogni volta passo quello che voglio io) con quello che fa myfunc (anche questo lo decido io volta per volta)
"""

"""
FILTER
While map() passes each element in the iterable through a function and returns the result of all elements having passed 
through the function, filter(), first of all, requires the function to return boolean values (true or false) and 
then passes each element in the iterable through the function, "filtering" away those that are false. 
It has the following syntax:
filter(func, iterable)
1) Unlike map(), only one iterable is required. (puoi passarne solo uno)
2) The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to 
it. Also, as only one iterable is required, it's implicit that func must only take one argument.
3) filter passes each element in the iterable through func and returns only the ones that evaluate to true. 
I mean, it's right there in the name -- a "filter".
The following is a list (iterable) of the scores of 10 students in a Chemistry exam. Let's filter out those who passed 
with scores more than 75...using filter.
# Python 3
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

The next example will be a palindrome detector. A "palindrome" is a word, phrase, or sequence that reads the same 
backwards as forwards. Let's filter out words that are palindromes from a tuple (iterable) of suspected palindromes.
# Python 3
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
"""

"""
REDUCE
reduce applies a function of two arguments cumulatively to the elements of an iterable, 
optionally starting with an initial argument. It has the following syntax:
reduce(func, iterable[, initial])
Where func is the function on which each element in the iterable gets cumulatively applied to, and initial is 
the optional value that gets placed before the elements of the iterable in the calculation, and serves as a default 
when the iterable is empty.
The following should be noted about reduce(): 
1) func requires two arguments, the first of which is the first element in iterable (if initial is not supplied) and the 
second element in iterable. If initial is supplied, then it becomes the first argument to func and the first element in 
iterable becomes the second element.
2) reduce "reduces" (I know, forgive me) iterable into a single value. 
Let's create our own version of Python's built-in sum() function.
The sum() function returns the sum of all the items in the iterable passed to it.
# Python 3
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)
As usual, it's all about iterations: reduce takes the first and second elements in numbers and passes them to custom_sum
respectively. custom_sum computes their sum and returns it to reduce. reduce then takes that result and applies it as 
the first element to custom_sum and takes the next element (third) in numbers as the second element to custom_sum. 
It does this continuously (cumulatively) until numbers is exhausted. 
Let's see what happens when I use the optional initial value.
# Python 3
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers, 10)
print(result)
The result, as you'll expect, is 78 because reduce, initially, uses 10 as the first argument to custom_sum.

map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
se non metto lambda x, non riconosce la x
se non metti lambda definisci fuori con def
o altrimenti funzione deve essere già esistente (roundo str.upper), e non specifici parametri
"""



"""
MAP argomenti di lista iterable (2 liste se funz prende 2 arg) passati a funz
FILTER argomenti di lista iterable (puoi passare solo un iterable) passatia funz se danno booleano true
REDUCE primo argomento passato a funz è primo di iterable (se initial non specificato), secondo argomento è secondo di 
    iterable, se invece initial è specificato lui è primo, secondo sarà primo di it, accumula risultato, riduce iterable
"""

"""
e.compile(pattern, flags=0)
Compile a regular expression pattern into a regular expression object, which can be used for matching using its 
match(), search() and other methods, described below.

Pattern.search(string[, pos[, endpos]])
Scan through string looking for the first location where this regular expression produces a match, and return a 
corresponding match object. Return None if no position in the string matches the pattern; note that this is 
different from finding a zero-length match at some point in the string.

Python offers two different primitive operations based on regular expressions: re.match() checks for a match only at
the beginning of the string, while re.search() checks for a match anywhere in the string 
(this is what Perl does by default).

fullmatch, suggerisce il significato

Raw string notation (r"text") keeps regular expressions sane. Without it, every backslash ('\') in a regular expression 
would have to be prefixed with another one to escape it. For example, the two following lines of code are functionally i
dentical:
>>>
>>> re.match(r"\W(.)\1\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>
>>> re.match("\\W(.)\\1\\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>
When one wants to match a literal backslash, it must be escaped in the regular expression. With raw string notation, 
this means r"\\". Without raw string notation, one must use "\\\\", making the following lines of code functionally identical:
>>> re.match(r"\\", r"\\")
<re.Match object; span=(0, 1), match='\\'>
>>> re.match("\\\\", r"\\")
<re.Match object; span=(0, 1), match='\\'>
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be 
used without invoking their special meaning. This collides with Python’s usage of the same character for the same 
purpose in string literals; for example, to match a literal backslash, one might have to write '\\\\' as the pattern 
string, because the regular expression must be \\, and each backslash must be expressed as \\ inside a regular Python 
string literal. Also, please note that any invalid escape sequences in Python’s usage of the backslash in string 
literals now generate a DeprecationWarning and in the future this will become a SyntaxError. This behaviour will happen 
even if it is a valid escape sequence for a regular expression.
The solution is to use Python’s raw string notation for regular expression patterns; 
backslashes are not handled in any special way in a string literal prefixed with 'r'. 
So r"\n" is a two-character string containing '\' and 'n', while "\n" is a one-character string containing a newline. 
Usually patterns will be expressed in Python code using this raw string notation.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

\
per fare il match con special caracter tipo ? * []

(...|...) or operator

se uno special caracter lo metti senza backslash davanti -> esegue sua funzionalità
se senza r -> doppio backslash
con r -> basta un backslash


# Example:
import re
pattern = re.compile(r"\[(on|off)\]") # Slight optimization
# se una stringa contiene [on] oppure [off] -> match
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-("))
# Doesn't return anything.
# End Example


ANY: The any(iterable) function returns True if any element of an iterable is True. If not, it returns False. 
iterable: list, string, dictionary etc.

PRINT E SEP
print(*TRAINING_DATA, sep="\n")
The separator between the arguments to print() function in Python is space by default (softspace feature) , which can be modified and can be made to any character, integer or string as per our choice. The ‘sep’ parameter is used to achieve the same, it is found only in python 3.x or later. It is also used for formatting the output strings.
In Python, usiamo il singolo asterisco (*) e il doppio asterisco (**) per indicare un numero variabile di argomenti.
print("ciao", "ciao")  # li stampa accanto
print("ciao", "ciao", sep="\n") # li stampa a capo

ASTERISCO IN DEFINIZIONE DI FUNZIONE
Possiamo passare qualsiasi numero di argomenti in una funzione Python in uno dei seguenti modi.
Argomenti posizionali (*)
Argomenti delle parole chiave (**)

ASTERISCO IN CHIAMATA DI FUNZIONE
È l'operatore "splat": accetta un elenco come input e lo espande in argomenti posizionali effettivi nella chiamata di funzione.
>>> def foo(a, b=None, c=None):
...   print a, b, c
... 
>>> foo([1, 2, 3]) se non metto asterisco di fronte a lista che passo a chiamata di funzone, LISTA È UN SOLO ARGOMENTO
[1, 2, 3] None None
>>> foo(*[1, 2, 3])    se metto asterisco di fronte a lista che passo a chiamata di funzione, QUELLI DENTRO LISTA SONO GLI ARGOMENTI DELLA CHIAMATA DI FUNZIONE
1 2 3

F-STRINGS
Also called “formatted string literals,” f-strings 
are string literals that have an f at the beginning and curly braces containing expressions 
that will be replaced with their values. 
The expressions are evaluated at runtime and then formatted using the __format__ protocol. 
>>> name = "Eric"
>>> age = 74
>>> f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'
name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")
'Hello, Eric. You are 74.'

altro modo per stringhe formattate
says_str = "A {name} says {sound}"
print(self.says_str.format(name=self.name, sound=out_sound))
self perché ero dentro classe

# ends the output with a <space> 
print("Welcome to" , end = ' ') 
print("GeeksforGeeks", end = ' ')

classe a 
classe b che è sottoclasse di a
classe b (a)
per creare sottoclasse passagli come argomento superclasse

if
elif 
else
non ci sono parentesi

class Adapter(Target, Adaptee): # ereditarietà multipla

metto self in metodo di una classe altrimenti non riesco a raggiungere componenti di un oggetto, in alcuni linguaggi è implicito. in python lo devi mettere, ma nelle chiamate passi dal secondo in poi

string.join(iterable) 
JOIN
list = ["a", "b", "c"]
print(f"Branch({'+'.join(list)})")
# OUTPUT: Branch(a+b+c)
Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) 

results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


variabile: tipo

non ci sono interfacce
se non vuoi implementare metti pass
tipo questa che segue è tipo interfaccia, in quanto dichiara solo metodi, ma in python la chiami classe, poi farai una classe child che la implementa
class Component():
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> str:
        pass
        
class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def operation(self) -> str:
        return "ConcreteComponent"
        


metti sempre self come primo parametro (si può chiamare come vuoi ma questa è convenzione)
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

n = int(input().strip())
funzione input per perndere input da tastiera a programma in corso

OPTIONAL ARGUMETNS VALUES
def student(firstname, lastname ='Mark', standard ='Fifth'):
     print(firstname, lastname, 'studies in', standard, 'Standard')
 
# 1 positional argument
student('John')
 
# 3 positional arguments                        
student('John', 'Gates', 'Seventh')    
 
# 2 positional arguments 
student('John', 'Gates')                 
student('John', 'Seventh')

OUTPUT:
John Mark studies in Fifth Standard
John Gates studies in Seventh Standard
John Gates studies in Fifth Standard
John Seventh studies in Fifth Standard

inner class : a class inside another class

sample() is an inbuilt function of random module in Python that returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set. Used for random sampling without replacement
Syntax : random.sample(sequence, k)

from ranomd import sample
return "".join(sample(ascii_letters, length)) # così te lo mette come stringa    tra le lettere non mette nemmneo nuo spazio

str.replace(old, new[, max])

parametri

    vecchio - sarà sostituito con la stringa.
    new - nuova stringa, che sostituisce vecchia stringa.
    max - stringa opzionale per sostituire non più di volte max 
    
    randrange(0, 10)
    
non c'è keyword implemets o extends, semplicemente gli passo classe

Python supports both function and operator overloading.

assert
An expression is tested, and if the result comes up false, an exception is raised. AssertionError exception.

print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
Note: In line 11, the f before the string indicates that this is an f-string, which is a convenient way to format a text string. :0.4f is a format specifier that says the number, toc - tic, should be printed as a decimal number with four decimals.

# path assoluto: "C:/example/cwd/mydir/myfile.txt"

# path assoluto 
import os

simp_path = 'demo/which_path.docx'
abs_path = os.path.abspath(simp_path)

print(abs_path)

"""




