# BYTEARRAY
    # 1) Mutable Sequesnt of bytes
    # 2) Can be altered
    # 3) Encodes Binary Data
    
# CREATE BYTEARRAY:-
# # from list of integers
# b_ar1 = bytearray([120, 119, 118, 117, 116, 115])
# print(b_ar1)         #bytearray(b'xwvuts')
# print(type(b_ar1))   #<class 'bytearray'>

# print("-------------------------------------------------------")
# #from bytes datatype
# b1 = b"HELLO"
# b_ar2 = bytearray(b1)
# print(b_ar2)
# print(type(b_ar2))

# print("-------------------------------------------------------")
# #from string
# str1 = "HYMA"
# b_ar3 = bytearray(str1, 'utf-8') 
# print(b_ar3)
# print(type(b_ar3))

# print("-------------------------------------------------------")

# #from integer
# b_ar4 = bytearray(4)
# print(b_ar4)
# print(type(b_ar4))


##################################################

# ACCESSING & MODIFYING BYTEARRAY:-

# b_ar5 = bytearray(b"WOWW...! This is so cool.")

# print(b_ar5[0])    #87
# print(b_ar5[-3])   #111
# print(b_ar5[0:4])  #bytearray(b'WOWW')

# b_ar5[0] = 65
# print(b_ar5)

#######################################

b_ar6 = bytearray(b"Hello")
# b_ar6.append(87)
# b_ar6.append(90)
# print(b_ar6)

# b_ar6.extend([97,98, 99, 100])
# print(b_ar6)

# del b_ar6[0::]
# print(b_ar6)