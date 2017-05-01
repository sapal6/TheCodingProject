# Boolean values
# True or False
# 0 and 1

# Examples of boolean values
# Task --> compare ios and android


OS1 = 'ios'
OS2 = 'android'

# Compare OS

print(OS1 == OS2)  # returns a false as ios is not android
print(OS1 is not OS2)  # returns a true as ios is not android


# some more examples
# use the "and" operator & 'or' operator

drinks = "beer"  # we need beer
food = "wafers"  # we need wafers


#  your choice -->
for_party = "mojito"  # only need mojito


# is your choice similar to my choice or not
print((for_party) == (drinks or food))
#
## to check if your choice aren't equal to my choice
print((for_party) is not (drinks or food))


#  summarize
# True and True --> True
# True and False --> False
# False and True --> False
# True or True --> True
# True or False --> True
# False or True --> False

