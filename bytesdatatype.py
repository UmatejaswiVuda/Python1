# BYTES
    # 1) It is a sequence of Integers.
    # 2) It is Immutable 
    # 3) 0-255
    
# Create bytes
    # with the help of byte literals:
    
# b1 = b'Hello'
# print(b1)          #b'Hello'
# print(type(b1))    #<class 'bytes'>

# print("----------------------------------------------")
#     # with the help of bytes function:
    
# b2 = bytes([65, 66, 67, 68, 69])
# print(b2)
# print(type(b2))

# print("----------------------------------------------")

# b3 = bytes('HELLO', 'utf-8')
# print(b3)
# print(type(b3))

# print("----------------------------------------------")

# b4 = bytes(range(97, 105))
# print(b4)
# print(type(b4))
################################################

# INDEXING UPON BYTES DATA TYPE:-
    # indexing will return the ascii of charecter
# b5 = b"PYTHON IS GREAT"
# print(b5[0])     #80--> P
# print(b5[2])     #72--> H

# print(b5[-2])    #65--> A

# print(b5[0:6])   #b'PYTHON'

#####################################
# Not possible to update
# b6 = b'HIllo'
# b6[1]==69
# print(b6)
#####################################


# b7 = b"GOODBYE"   # bytes data type
# print(b7)
# str1 = b7.decode('utf-8')
# print(str1)

##########################################

# b8 = b"HELLO WORLD, HOW ARE YOU ?"
# print(b8.count(b'L'))
# print(b8.count(b'H'))

#######################################

b9 = b"sdfghgfdghyfvbmvcxdyukkj"
print(b9.find(b'f'))
print(b9.rfind(b'f'))
