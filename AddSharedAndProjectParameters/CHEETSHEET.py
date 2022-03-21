# Python Build-in Function
#----------------------------------------------------------------

abs(x)
# Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing __abs__(). If the argument is a complex number, its magnitude is returned.

all(iterable)
# Return True if all elements of the iterable are true (or if the iterable is empty).

any(iterable)
# Return True if any element of the iterable is true. If the iterable is empty, return False.

callable(object)
# Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a __call__() method.

chr()
# Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord(). The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range.

@classmethod
# Transform a method into a class method.

delattr(object, name)
# This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.

dict()
# Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types — dict for documentation about this class. For other containers see the built-in list, set, and tuple classes, as well as the collections module.

dir([object])
# Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

dirmod(a, b)
# Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).

enumerate(iterable, start=0)
# Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.

    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons))
    # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    list(enumerate(seasons, start=1))
    # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

    def enumerate(sequence, start=0):
        n = start
        for elem in sequence:
            yield n, elem
            n += 1

eval(expression[, globals[, locals]])
# The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.

# The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace. If the globals dictionary is present and does not contain a value for the key __builtins__, a reference to the dictionary of the built-in module builtins is inserted under that key before expression is parsed. This means that expression normally has full access to the standard builtins module and restricted environments are propagated. If the locals dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is executed with the globals and locals in the environment where eval() is called. Note, eval() does not have access to the nested scopes (non-locals) in the enclosing environment.

# The return value is the result of the evaluated expression. Syntax errors are reported as exceptions.

filter(function, iterable)
# Equivalent
(item for item in iterable if function(item))
# Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.

float()
# Return a floating point number constructed from a number or string x.

format()
# Convert a value to a “formatted” representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument, however there is a standard formatting syntax that is used by most built-in types: Format Specification Mini-Language.
# https://docs.python.org/3/library/string.html#formatspec

frozenset()
# The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable. Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.

getattr(object, name[, default])
# Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.

globals()
# Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

hasattr(object, name)
# The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not.)

hash(object)
# Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).

hex(x)
# Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. If x is not a Python int object, it has to define an __index__() method that returns an integer.

id(object)
# Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

input([prompt])
# If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised.

int(x, base=10)
# Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x defines __int__(), int(x) returns x.__int__(). If x defines __index__(), it returns x.__index__(). If x defines __trunc__(), it returns x.__trunc__(). For floating point numbers, this truncates towards zero.

# If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer literal in radix base. Optionally, the literal can be preceded by + or - (with no space in between) and surrounded by whitespace. A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 10 to 35. The default base is 10. The allowed values are 0 and 2–36. Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code. Base 0 means to interpret exactly as a code literal, so that the actual base is 2, 8, 10, or 16, and so that int('010', 0) is not legal, while int('010') is, as well as int('010', 8).

isinstance(object, classinfo)
# Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns False. If classinfo is a tuple of type objects (or recursively, other such tuples), return True if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.

issubclass(class, classinfo)
# Return True if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked. In any other case, a TypeError exception is raised.

iter(object[, sentinel])
# Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, object must be a collection object which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then object must be a callable object. The iterator created in this case will call object with no arguments for each call to its __next__() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.

len(s)
# Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

list([iterable])
# Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.

map(function, iterable, ...)
# Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

max()
memoryview()
min()


next()
# Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

object()
# Return a new featureless object. object is a base for all classes. It has the methods that are common to all instances of Python classes. This function does not accept any arguments.

oct(x)
# Convert an integer number to an octal string prefixed with “0o”. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer. 

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised. See Reading and Writing Files for more examples of how to use this function.

# file is a path-like object giving the pathname (absolute or relative to the current working directory) of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, it is closed when the returned I/O object is closed, unless closefd is set to False.)

# mode is an optional string that specifies the mode in which the file is opened. It defaults to 'r' which means open for reading in text mode. Other common values are 'w' for writing (truncating the file if it already exists), 'x' for exclusive creation and 'a' for appending (which on some Unix systems, means that all writes append to the end of the file regardless of the current seek position). In text mode, if encoding is not specified the encoding used is platform dependent: locale.getpreferredencoding(False) is called to get the current locale encoding. (For reading and writing raw bytes use binary mode and leave encoding unspecified.)

ord(c)
# Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

print()
# Print objects to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments.

property(fget=None, fset=None, fdel=None, doc=None)
# Return a property attribute. fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.
# @property
#   def test():
#       ...
# @test.getter | @test.setter | @test.deleter (put the new function unter that)
# @test.getter
# def test(self, name):
#   self.name = name

range(start, stop[, step])

reversed(seq)
# Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).

round(number[, ndigits])
# Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

set([iterable])
# Return a new set object, optionally with elements taken from iterable. set is a built-in class. See set and Set Types — set, frozenset for documentation about this class.

setattr(object, name, value)
# This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.

slice(stop)
slice(start, stop, [step])
# Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). They have no other explicit functionality; however they are used by Numerical Python and other third party extensions. Slice objects are also generated when extended indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i].

sorted(iterable, *, key=None, reverse=False)
# Return a new sorted list from the items in iterable. Has two optional arguments which must be specified as keyword arguments. key specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly). reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

@staticmethod
# @staticmethod
# def f(arg1, arg2, ...): ...
# Transform a method into a static method.

str(object=b'', encoding='utf-8', errors='strict')
# Return a str version of object. See str() for details.

sum(iterable, /, start=0)
# Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.

super([type[, object-or-type]])
# Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.

tuple([iterable])
# Rather than being a function, tuple is actually an immutable sequence type, as documented in Tuples and Sequence Types — list, tuple, range.

type(object)
type(name, bases, dict, **kwds)
# With one argument, return the type of an object. The return value is a type object and generally the same object as returned by object.__class__.
# With three arguments, return a new type object. This is essentially a dynamic form of the class statement. The name string is the class name and becomes the __name__ attribute. The bases tuple contains the base classes and becomes the __bases__ attribute; if empty, object, the ultimate base of all classes, is added. The dict dictionary contains attribute and method definitions for the class body; it may be copied or wrapped before becoming the __dict__ attribute. 

vars([object])
# Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.

zip(*iterables)
# Make an iterator that aggregates elements from each of the iterables.
# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
# The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

from itertools import zip_longest
zip_longest(list1, list2,...., fillvalue = "something")
# Make an iterator that aggregates elements from each of the iterables.
# Make the tuple according to longest list, empty values will be None as default fillvalue = None
# list(zip_longest())

.__doc__
# Descrition of a function