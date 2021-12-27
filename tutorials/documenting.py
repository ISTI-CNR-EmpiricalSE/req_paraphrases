# DIFFERENCE BETWEEN COMMENTING AND DOCUMENTING
"""
In general, commenting is describing your code to/for developers. The intended main audience is
the maintainers and developers of the Python code. In conjunction with well-written code,
comments help to guide the reader to better understand your code and its purpose and design:
Documenting code is describing its use and functionality to your users. While it may be helpful in the development process,
the main intended audience is the users.
"""

# COMMENTING
"""
brief statements,  few sentences,
According to PEP 8, comments should have a maximum length of 72 characters.
If greater: using multiple lines
Outline areas of improvement  BUG, FIXME, and TODO.

RULES
1 Keep comments as close to the code being described as possible. Comments that aren’t near their describing code are frustrating to the reader and easily missed when updates are made
2 Don’t use complex formatting (such as tables or ASCII figures). Complex formatting leads to distracting content and can be difficult to maintain over time
3 Don’t include redundant information. Assume the reader of the code has a basic understanding of programming principles and language syntax
4 Design your code to comment itself. The easiest way to understand code is by reading it. When you design your code using clear, easy-to-understand concepts, the reader will be able to quickly conceptualize your intent

UTILE
per portare punto 4 to the next level -> Type Hinting

def hello_name(name: str) -> str:
    return(f"Hello {name}")
print(hello_name("Isabella"))

così ->
def hello_name(name: str) -> str:return(f"Hello {name}")
"""

# DOCUMENTING USING DOCSTRINGS
"""
!!!!!!!!!!!!!!!!!!!!!!!!! PEP 257 -- Docstring Conventions per roba più dettagliata
DOCSTRINGS BACKGROUND
to provide your users with a brief overview of the object.
Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
commenti vengono del tutto ignorati da python interpreter, invece a queste puoi accedere con attributo doc
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
print(square.__doc__)
Documenting your Python code is all centered on docstrings. 
These are built-in strings that, when configured correctly, can help your users and yourself with your project’s documentation. 
Along with docstrings, Python also has the built-in function help() that prints out the objects docstring to the console. 
Here’s a quick example:
>>> help(str) funzionalità che stampa le docstrings che documentano una certa classe
Help on class str in module builtins:
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors are specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 # Truncated for readability
 
 capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
stringa = str('bo')
print(stringa.capitalize())

How is this output generated? Since everything in Python is an object, you can examine the directory of the object using the dir() command. Let’s do that and see what find:
>>> dir(str)
['__add__', ..., '__doc__', ..., 'zfill'] # Truncated for readability
Within that directory output, there’s an interesting property, __doc__. If you examine that property, you’ll discover this:
>>> print(str.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors are specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.

Voilà! You’ve found where docstrings are stored within the object. This means that you can directly manipulate that property. 
However, there are restrictions for builtins:
>>> str.__doc__ = "I'm a little string doc! Short and stout; here is my input and print me for my out"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't set attributes of built-in/extension type 'str'
Any other custom object can be manipulated:
def say_hello(name):
    print(f"Hello {name}, is it me you're looking for?")

say_hello.__doc__ = "A simple function that says hello... Richie style"

>> help(say_hello)
Help on function say_hello in module __main__:

say_hello(name)
    A simple function that says hello... Richie style
    
Python has one more feature that simplifies docstring creation. Instead of directly manipulating the __doc__ property, 
the strategic placement of the string literal directly below the object will automatically set the __doc__ value. 
Here’s what happens with the same example as above:
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
input:
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")

>>> help(say_hello)
output:
Help on function say_hello in module __main__:

say_hello(name)
    A simple function that says hello... Richie style
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
"""
"""
DOCSTRING TYPES
Docstring conventions are described within PEP 257. Their purpose is to provide your users with a brief overview of the
object. They should be kept concise enough to be easy to maintain but still be elaborate enough for new users 
to understand their purpose and how to use the documented object.
In all cases, the docstrings should use the triple-double quote string format. This should be done whether the docstring is multi-lined or not.
At a bare minimum, a docstring should be a quick summary of whatever is it you’re describing and should be contained within a single line:
MULTI-LINED docstrings are used to further elaborate on the object beyond the summary. All multi-lined docstrings have the following parts:
A one-line summary line
A blank line proceeding the summary
Any further elaboration for the docstring
Another blank line
"""This is the summary line

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

# Notice the blank line above. Code should continue on this line.

All docstrings should have the same max character length as comments (72 characters). 
Docstrings can be further broken up into three major categories:
Class Docstrings: Class and class methods
Package and Module Docstrings: Package, modules, and functions
Script Docstrings: Script and functions

CLASS DOCSTRINGS
Class Docstrings are created for the class itself, as well as any class methods. The docstrings are placed immediately following the class or class method indented by one level:
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""

        print(f'Hello {name}')

Class docstrings should contain the following information:
A brief summary of its purpose and behavior
Any public methods, along with a brief description
Any class properties (attributes)
Anything related to the interface for subclassers, if the class is intended to be subclassed

The class constructor parameters should be documented within the __init__ class method docstring. Individual methods should be documented using their individual docstrings. 
Class method docstrings should contain the following:
A brief description of what the method is and what it’s used for
Any arguments (both required and optional) that are passed including keyword arguments
Label any arguments that are considered optional or have a default value
Any side effects that occur when executing the method
Any exceptions that are raised
Any restrictions on when the method can be called

Let’s take a simple EXAMPLE of a data class that represents an Animal. This class will contain a few class properties, instance properties, a __init__, and a single instance method:

class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs=4):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used. se non lo passo uso quello settato con costruttore, se anche quello è none si solleva eccezione

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))
        

PACKAGE AND MODULE DOCSTRINGS
Package docstrings should be placed at the top of the package’s __init__.py file
This docstring should list the modules and sub-packages that are exported by the package.

module = class - modul function = class method
Module docstrings are similar to class docstrings. Instead of classes and class methods being documented, it’s now the module and any functions found within. 
Module docstrings are placed at the top of the file even before any imports. Module docstrings should include the following:
A brief description of the module and its purpose
A list of any classes, exception, functions, and any other objects exported by the module
The docstring for a module function should include the same items as a class method:
A brief description of what the function is and what it’s used for
Any arguments (both required and optional) that are passed including keyword arguments
Label any arguments that are considered optional
Any side effects that occur when executing the function
Any exceptions that are raised
Any restrictions on when the function can be called


SCRIPT DOCSTRINGS
Scripts are considered to be single file executables run from the console. Docstrings for scripts are placed at the top of the file and should be documented well enough for users to be able to have a sufficient understanding of how to use the script. It should be usable for its “usage” message, when the user incorrectly passes in a parameter or uses the -h option.

ARGPARSE
The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

If you use argparse, then you can omit parameter-specific documentation, assuming it’s correctly been documented within the help parameter of the argparser.parser.add_argument function. It is recommended to use the __doc__ for the description parameter within argparse.ArgumentParser’s constructor. Check out our tutorial on Command-Line Parsing Libraries for more details on how to use argparse and other common command line parsers.
Finally, any custom or third-party imports should be listed within the docstrings to allow users to know which packages may be required for running the script. Here’s an example of a script that is used to simply print out the column headers of a spreadsheet:
"""Spreadsheet Column Printer

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

import argparse

import pandas as pd


def get_spreadsheet_cols(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    list
        a list of strings used that are the header columns
    """

    file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=str,
        help="The spreadsheet file to pring the columns of"
    )
    args = parser.parse_args()
    get_spreadsheet_cols(args.input_file, print_cols=True)


if __name__ == "__main__":
    main()
"""
"""
DOCSTRING FORMAT
io userò reStructured Text
Official Python documentation standard; Not beginner friendly but feature rich
"""Gets and prints the spreadsheet's header columns

:param file_loc: The file location of the spreadsheet
:type file_loc: str
:param print_cols: A flag used to print the columns to the console
    (default is False)
:type print_cols: bool
:returns: a list of strings representing the header columns
:rtype: list


# così ->
def my_function(my_arg, my_other_arg):
    """A function just for me.

    :param my_arg: The first of my arguments.
    :param my_other_arg: The second of my arguments.

    :returns: A message (just for me, of course).
    """



"""
DOCUMENTING YOUR PYTHON PROJECT
The general layout of the project and its documentation should be as follows:
project_root/
│
├── project/  # Project source code
├── docs/
├── README
├── HOW_TO_CONTRIBUTE
├── CODE_OF_CONDUCT
├── examples.py

Projects can be generally subdivided into three major types: Private, Shared, and Public/Open Source.

Private Projects
Private projects are projects intended for personal use only and generally aren’t shared with other users or developers. Documentation can be pretty light on these types of projects. There are some recommended parts to add as needed:
Readme: A brief summary of the project and its purpose. Include any special requirements for installation or operating the project.
examples.py: A Python script file that gives simple examples of how to use the project.
Remember, even though private projects are intended for you personally, you are also considered a user. Think about anything that may be confusing to you down the road and make sure to capture those in either comments, docstrings, or the readme.

Shared Projects
Shared projects are projects in which you collaborate with a few other people in the development and/or use of the project. The “customer” or user of the project continues to be yourself and those limited few that use the project as well.
Documentation should be a little more rigorous than it needs to be for a private project, mainly to help onboard new members to the project or alert contributors/users of new changes to the project. Some of the recommended parts to add to the project are the following:
Readme: A brief summary of the project and its purpose. Include any special requirements for installing or operating the project. Additionally, add any major changes since the previous version.
examples.py: A Python script file that gives simple examples of how to use the projects.
How to Contribute: This should include how new contributors to the project can start contributing.

Public and Open Source Projects
Public and Open Source projects are projects that are intended to be shared with a large group of users and can involve large development teams. These projects should place as high of a priority on project documentation as the actual development of the project itself. Some of the recommended parts to add to the project are the following:
Readme: A brief summary of the project and its purpose. Include any special requirements for installing or operating the projects. Additionally, add any major changes since the previous version. Finally, add links to further documentation, bug reporting, and any other important information for the project. Dan Bader has put together a great tutorial on what all should be included in your readme
How to Contribute: This should include how new contributors to the project can help. This includes developing new features, fixing known issues, adding documentation, adding new tests, or reporting issues
Code of Conduct: Defines how other contributors should treat each other when developing or using your software. This also states what will happen if this code is broken. If you’re using Github, a Code of Conduct template can be generated with recommended wording. For Open Source projects especially, consider adding this
License: A plaintext file that describes the license your project is using. For Open Source projects especially, consider adding this
docs: A folder that contains further documentation. The next section describes more fully what should be included and how to organize the contents of this folder

-> The Four Main Sections of the docs Folder
Tutorials: Lessons that take the reader by the hand through a series of steps to complete a project (or meaningful exercise). Geared towards the user’s learning.
How-To Guides: Guides that take the reader through the steps required to solve a common problem (problem-oriented recipes).
References: Explanations that clarify and illuminate a particular topic. Geared towards understanding.
Explanations: Technical descriptions of the machinery and how to operate it (key classes, functions, APIs, and so forth). Think Encyclopedia article.

 	                Most Useful When We’re Studying 	Most Useful When We’re Coding
Practical Step 	            Tutorials 	                        How-To Guides
Theoretical Knowledge 	    Explanation 	                    Reference

Documenting your code, especially large projects, can be daunting. Thankfully there are some tools out and references to get you started:
vedi sito

Along with these tools, there are some additional tutorials, videos, and articles that can be useful when you are documenting your project:

Sometimes, the best way to learn is to mimic others. Here are some great examples of projects that use documentation well:
vedi sito
Django: Docs (Source)
Requests: Docs (Source)
Click: Docs (Source)
Pandas: Docs (Source)



"""

