'''This file outlines examples four four different error functions. NameError, TypeError, SyntaxError, AttributeError.
Their inputs are either an integer, str, or object. The functions are written do not return anything but print statements.Instead of actual print statements they produce errors.'''

def NameE(a):
# here we get a name error because we are attempting to access a variable that doesnt exist
    print(y)

def TypeE(b):
# here we get a type error because we can not perform math on a str object
    b =2
    print('b' + b)

def SyntaxE(c):
# we receive this error because we attempt a variable assignment and print statement without the proper syntax 
    if c == 7 print(c)

def AttributeE(object):
# we get this error here because we are atempting to access an attribute that does not exist.
	class Zero_attributes(object):
                 	pass
	o = Zero_attributes()
	print o.an_attribute

