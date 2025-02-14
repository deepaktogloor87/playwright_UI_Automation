# x=10
# y='20'

#can we define in single line? answer is yes
x, y = 10, '20'

# =========== addition ===========
y = int(y)
print(x+y)

#what is f string
print(f"{x} + {y} = {x+y}")

#another way of formatting
# print("{} + {} = {}".format(x,y,x+y))

# =========== multiplication ===========
#what is f string
print(f"{x} - {y} = {x-y}")

y = int(y)
print(x*y)

#what is f string
print(f"{x} * {y} = {x*y}")

# =========== exponent / power of  ===========
#what is f string
print(f"{x} ** {y} = {x**y}")

y = int(y)
print(x**y)

#what is f string
print(f"{x} ** {y} = {x*y}")

# =========== division  ===========
#what is f string
print(f"{x} / {y} = {x/y}")

y = int(y)
print(x/y)

#what is f string
print(f"{x} / {y} = {x/y}")

# =========== floor division  ===========
#what is f string
print(f"{x} // {y} = {x//y}")

y = int(y)
print(x//y)

#what is f string
print(f"{x} // {y} = {x//y}")

# =========== modulus  ===========
#what is f string
print(f"{x} % {y} = {x%y}")

y = int(y)
print(x%y)

#what is f string
print(f"{x} % {y} = {x%y}")