
# string interpolation is an old python2 method
# it will be mothballed from python3 at some point
age = 24
print("My age is %d years" % age)

major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("Pi is approximately %f" % (22 / 7))

# the one below is similar to how we specift precision using .format etc
print("Pi is approximately %60.50f" % (22 / 7))

# %x can replace fields with hexadecimals
# %o can replace fields with octals
# %e can replace fields with scientific notation
