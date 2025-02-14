# assume that i have a variable x with value 10 and y with value 20
# x = 10
# y = 20
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)        # modulus operator is to get the reminder value in 01-python
# print(x ** y)       # exponent operator is to power the value
# print(x // y)       # floor division is to get the floor value of the division
'''
30
-10
200
0.5
10
100000000000000000000
0
'''

# now assume that i have a variable x with value 10 and y with value '20'
# can we add them?

x = 10
y = '20'
# print(x+y)      # see y got highlighted and what is the error? --- Expected type 'int', got 'str' instead

#TypeError: unsupported operand type(s) for +: 'int' and 'str'
# so we can not add interger with string value.
# --- then how to do that?

# we can convert the string value to integer
y = int(y)
print(x+y)

#what is f string
print(f"{x} + {y} = {x+y}")

#another way of formatting
print("{} + {} = {}".format(x,y,x+y))

