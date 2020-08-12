import math

# multiple assignment
a = b = c = 1
a, b, c = "hello", 0, 0.0

# delete variables
del a, b, c

# numbers
print('NUMBERS')
# - int (signed integers)
print(-1)
# - long (long integers, they can also be represented in octal and hexadecimal)
print(0o11)  # octal (base 8)
print(0xA0)  # hexadecimal (base 16)
# - float (floating point real values)
print(32.3)
print(32.3e18)
print(70.2e-12)
# - complex (complex numbers)
print(9.32 - 36j)
print(9.32e-36j)
# number constants
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

# strings
print('\n\nSTRINGS')
string = 'Hello World!'
para_str = """this is a long string that is made up of
several lines and non-printable characters 
such as TAB ( \t )
"""
print(string)  # Prints complete string
print(string[0])  # Prints first character of the string
print(string[:-2])  # print up to second to last character
print(r'\n\n\n')  # raw string
print(u'Hello, world!')  # unicode string
print(para_str)

# list
print('\n\nLISTS')
listt = ['abcd', 786, 2.23, 'john', 70.2]
print(listt[0])
print(listt)
print(listt * 2)

# tuples - read-only list
print('\n\nTUPLES')
tuplee = ('abcd', 786, 2.23, 'john', 70.2)
tupled = 'abcd', 786, 2.23, 'john', 70.2
print(tuplee)
print(tupled)
print(tuplee[0])
print(tuplee)
print(tuplee * 2)

# dictionary
print('\n\nDICTIONARY')
dictt = {}
dictt['one'] = "This is one"
dictt[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dictt['one'])  # Prints value for 'one' key
print(dictt[2])  # Prints value for 2 key
print(tinydict)  # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values

# set
print('\n\nSETS')
set_one = {1, 2, 3, 100, '606', 50, 60}
# print(max(set_one))
print(set_one)
print(len(set_one))
print(set_one.pop())
print(set_one)
print(set_one.discard('606'))
print(set_one)
print(set_one.clear())
print(set_one)
print(set_one.add(20))
print(set_one)
print(set_one.remove(20))
print(set_one)

# data conversion
print('\n\nDATA CONVERSION')
print(tuple(list(set([50, "606", 2, 3, 100, 1, 1, 2, 1, 50, 60, 100, 50]))))
print(set((50, "606", 2, 3, 100, 1, 1, 2, 1, 50, 60, 100, 50)))
