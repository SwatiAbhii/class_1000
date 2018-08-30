a = 'Hi'
b = 'Welcome'
c= 'DigitalLync'

# print(b,'to',c)

# Inbult function string
# ===========================

# len()-----------> length of the string

# print(len(a))
# print(a.upper())
# print(b.upper())
# print(b.lower())
# print(a.isalnum())
# print(a.isdecimal())
print(c.center(3))
print(a.istitle())
# INBULT METHOD IN strings
# =======================================

# Python String capitalize()	Converts first character to Capital Letter
# Python String center()	Pads string with specified character
# Python String casefold()	converts to casefolded strings
# Python String count()	returns occurrences of substring in string
# Python String endswith()	Checks if String Ends with the Specified Suffix
# Python String expandtabs()	Replaces Tab character With Spaces
# Python String format()	formats string into nicer output
# Python String index()	Returns Index of Substring
# Python String isalnum()	Checks Alphanumeric Character
# Python String isalpha()	Checks if All Characters are Alphabets
# Python String isdecimal()	Checks Decimal Characters
# Python String isdigit()	Checks Digit Characters
# Python String isidentifier()	Checks for Valid Identifier
# Python String islower()	Checks if all Alphabets in a String are Lowercase
# Python String isnumeric()	Checks Numeric Characters
# Python String isprintable()	Checks Printable Character
# Python String isspace()	Checks Whitespace Characters
# Python String istitle()	Checks for Titlecased String
# Python String isupper()	returns if all characters are uppercase characters
# Python String join()	Returns a Concatenated String
# Python String ljust()	returns left-justified string of given width
# Python String rjust()	returns right-justified string of given width
# Python String lower()	returns lowercased string
# Python String upper()	returns uppercased string
# Python String swapcase()	swap uppercase characters to lowercase; vice versa

# Python String lstrip()	Removes Leading Characters
# Python String rstrip()	Removes Trailing Characters
# Python String strip()	Removes Both Leading and Trailing Characters

# d= 'Batman'
# print(d.index('m'))

# e = 20*'*'+'hyderabd,hyd,hyd,hbyd'+20*'-'+30*'#'
# print(e)
# # print(e.strip('*Ave'))
# print(e.lstrip('*'))
# print(e.rstrip('#'))

# print(e.casefold())

# print(e.upper())

# print(e.count('h'))

# String Formating styles
# =================================================

# old formating styles
# # -------------------------------
# %s ------------ str()
# %d ---------- int()
# %f --------- float()
# %b ---------- bin()
# %h -------- hex()
# %o ------- oct()

a = 'Batman'
b = 'Superman'
c = 45.323565432345
d = 33.434456
# b = 'cat'
# a = 'congo'
# print('%s and %s are the avengers'%(a,b))
# print('%s and %s of roll number %d and %d had scored %f and %f markin in the exam'%(a,b,45,54,99.8765,55.889))


# New formating styles or fanciedr formating style
# ===========================================

# .format()---------------- inbuilt method

print('{1} and {0} are the avengers'.format(a,b))

print('{:.4s} and {:.3s} are the avengers marks are {:.3f} and {:.2f}  resp'.format(a,b,c,d))
