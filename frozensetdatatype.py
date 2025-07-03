# What type of datatype is frozenset ?
    # Exactly like set but immutable.
    # It can be used as keys in dictionary
    # It is hashable
    # It is an unordered
    # it is randomly placed
    # it does not support Indexing
    # Only unique elements are allowed
    
# How to create a frozenset.
    # with the help frozenset()
    
# f_set1 = frozenset()
# print(f_set1)    #frozenset()
# print(type(f_set1))     #<class 'frozenset'>

# f_set1 = frozenset('APPLE')
# print(f_set1)
# print(type(f_set1))

# print("--------------------------------------------------------")

# f_set2 = frozenset([12, 23, 34, 45, 55, 67, 21, 12, 23, 34])
# print(f_set2)
# print(type(f_set2))

# print("--------------------------------------------------------")

# f_set3 = frozenset((90, 89, 67, "A", True, 1))
# print(f_set3)
# print(type(f_set3))

# print("--------------------------------------------------------")

# f_set4 = frozenset({1.2, "w", False, 5+6j})
# print(f_set4)
# print(type(f_set4))

# MEMBERSHIP

# f_set5 = frozenset({12, 23, 34, 32, 21, 54, 45, 67,89, 90})
# print(21 in f_set5)


################################################

# UNION:-

# f_1 = frozenset({12, 34, 56, 43, 21, 89, 90, 66, 58})
# f_2 = frozenset([55, 23, 12, 89, 99, 55, 34, 43, 100])

# f_3 = f_1 | f_2
# print(f_3)
# print(type(f_3))

# INTERSECTION

# f_1 = frozenset({12, 34, 56, 43, 21, 89, 90, 66, 58})
# f_2 = frozenset([55, 23, 12, 89, 99, 55, 34, 43, 100])

# f_4 = f_1 & f_2
# print(f_4)
# print(type(f_4))

# DIFFERENCE
# f_1 = frozenset({12, 34, 56, 43, 21, 89, 90, 66, 58})
# f_2 = frozenset([55, 23, 12, 89, 99, 55, 34, 43, 100])

# f_5 = f_1 - f_2
# print(f_5)

# f_6 = f_2 - f_1
# print(f_6)

# SYMMETRIC DIFFERENCE
# f_1 = frozenset({12, 34, 56, 43, 21, 89, 90, 66, 58})
# f_2 = frozenset([55, 23, 12, 89, 99, 55, 34, 43, 100])

# f_7 = f_1 ^ f_2
# print(f_7)

# .difference
# print(f_1.difference(f_2))


# .intersection
# print(f_1.intersection(f_2))

# .symmetric_difference
# print(f_1.symmetric_difference(f_2))


# isdijoint()

# print(f_1.isdisjoint(f_2))

#issubset()
# print(f_1.issubset(f_2))

#issuperset()
# print(f_2.issubset(f_1))
# print(f_1.issuperset(f_2))

###############################################

# dict1 = {
#     frozenset("ALMOND"):"Dryfruit",
#     "Origin":"India",
#     "Price":1000
# }

# print(dict1)
