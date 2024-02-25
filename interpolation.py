# String interpolation is an old python2 method for string replacement fields
# It will be mothballed from python3 at some point but still works in Jan 2024

age = 24
print("My age is %d years" % age)

major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("Pi is approximately %f" % (22 / 7))

# The code below is similar to how we specify precision using '.format()' etc
print("Pi is approximately %60.50f" % (22 / 7))

# %x can replace fields with hexadecimals
# %o can replace fields with octals
# %e can replace fields with scientific notation
