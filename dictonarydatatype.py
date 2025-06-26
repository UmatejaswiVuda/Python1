# one variable & one value
name = 'shiv'
age = 32

# one variable & multiple values
names = ['shiv', 'kumar', 'ravi']
ages = (32, 45, 67)

# one variable and muliple variable & value pairs

person1 = {
    'name':"Shiv",
    'age':32,
    'city':"Hyderabad",
}

person2 ={
    'name': "Kumar",
    'age': 34,
    'city': "Solapur"
}

##########################################

# Dictionary is collection of multiple key and value pairs.
# Dictionary is Unordered
# Dictionary is Mutable
# Dictionary is Indexed by keys

#########################################

# INITIALIZATION OF DICTIONARY:-

    # Creating dictionary with the help of {}
    
# dict1 = {}
# print(dict1)
# print(type(dict1))

# print("---------------------------------------")

# dict2 = {'A':65, 'B':66, 'C':67, 'D':68}
# print(dict2)
# print(type(dict2))

# print("---------------------------------------")

# dict3 = {1:1, 2:4, 3:9, 4:16}
# print(dict3)
# print(type(dict3))

# print("---------------------------------------")

# dict4 = dict({'a':97, 'b':98, 'c':99})
# print(dict4)
# print(type(dict4))

# print("---------------------------------------")

# dict5 = dict(One=1, Two=2, Three=3)
# print(dict5)
# print(type(dict5))

# print("---------------------------------------")

# keys = ['Apple', 'Mango', 'Dragon Fruit', "Avocado"]
# values = ['Vit-A', 'Vit-M', 'Vit-D', 'Vit-AV']

# dict6 = dict(zip(keys, values))
# print(dict6)
# print(type(dict6))

# print("---------------------------------------")

# # result = {
# #     'rohan': 'Fail',
# #     'Ajay': 'Fail',
# #     'Sima': 'Fail'
# # }

# students = ['Atul', 'Mallesh', 'Nikhil', 'Kumar', "Soni"]

# dict7 = dict.fromkeys(students, 'Fail')
# print(dict7)
# print(type(dict7))

# print("---------------------------------------")

# dict8 = dict([('subjec1', 'Physics'), ('subject2', 'Chemistry'), ('subject3', 'Maths'), ('subjecct4', 'History')])
# print(dict8)
# print(type(dict8))


###########################################

# ACCESSING ELEMENTS FROM DICTIONARY:

# employee_info = {
#     'empId': '10001',
#     'empPosition': 'Senior Engineer',
#     'empName': 'Vishal',
#     'empEmail': 'vishal@gmail.com',
#     'empSalary': 50000,
#     'empCompany': 'IBM'
# }

# print(employee_info['empName'])
# print(employee_info['empSalary'])
# print(employee_info['empEmail'])

# print(employee_info.get('empCompany'))
# print(employee_info.get('empName'))

###############################################

# MODIFYING DICTIONARY:-

# employee_info = {
#     'empId': '10001',
#     'empPosition': 'Senior Engineer',
#     'empName': 'Vishal',
#     'empEmail': 'vishal@gmail.com',
#     'empSalary': 50000,
#     'empCompany': 'IBM'
# }

# employee_info['empEmail'] = 'vishal123@gmail.com'
# employee_info['empCompany'] = 'Microsoft'
# employee_info['empPf'] = 5000
# employee_info['isMarried'] = True

# print(employee_info)
###################################################

# REMOVE ELEMENTS FROM DICTIONARY:-

dict1 = {
    'name':'rahul',
    'fav_game': 'football',
    'fav_food': 'idli-sambhar',
    'fav_destination': 'manali',
    'best_friend': 'kiran'
 }
# print("Original Dictionary: ")
# print(dict1)
# print('----------------------------------------')

# dict1.pop('best_friend')
# print('updated dictionary: ')
# print(dict1)

# print('-------------------------------------')

# dict1.pop('fav_food')
# print('updated ditionary: ')
# print(dict1)

# del 
# print('original dictionary: ')
# print(dict1)

# print('--------------------------------------------------')
# del dict1['fav_game']
# print('updated dictionary ')
# print(dict1)

# print('''''''''''''''''''''''''''''''''''''''''''''''''''''''')
# del dict1['fav_food']
# print('updated dictionary: ')
# print(dict1)


##########################################################

# clear()

# print('original dictionary: ')
# print(dict1)
# print('-----------------------------------------')

# print('updated dictionary: ')
# dict1.clear()
# print(dict1)

##########################################################

# popitem()

# print('original dictionary: ')
# print(dict1)
# print('----------------------------------------------')

# print('updated dictionary: ')
# dict1.popitem()
# print(dict1)
###############################################

# dict2 = {
#     'id': 1001,
#     'cust_name': 'mallesh reddy',
#     'cust_address': 'patancheruvu',
#     'cust_email': 'mallu@gmail.com',
#     'cust_phone': '1234567890',
#     'cust_items':['Tea Powder','Milk packet', 'Rice', 'Jaggery', 'Oil', 'Chilly Powder', 'Salt']

# }
# print('Original Dictionary: ')
# print(dict2)

# print('----------------------------------------')
# print('Only Keys of a dict2:')
# # .keys()
# print(dict2.keys())
# print(type(dict2.keys()))
# # dict_keys(['id', 'cust_name', 'cust_address', 'cust_email', 'cust_phone', 'cust_items'])
# print('----------------------------------------------------')

# # list 
# print(list(dict2.keys()))

# print('-----------------------------------------------')
# # tuple
# print(tuple(dict2.keys()))

# print('-----------------------------------------------')
# print(set(dict2.keys()))

################################################################

# .values()
# dict2 = {
#     'id': 1001,
#     'cust_name': 'mallesh reddy',
#     'cust_address': 'patancheruvu',
#     'cust_email': 'mallu@gmail.com',
#     'cust_phone': '1234567890',
#     'cust_items':['Tea Powder','Milk packet', 'Rice', 'Jaggery', 'Oil', 'Chilly Powder', 'Salt']
# }

# print(dict2.values())
# print(type(dict2.values()))

# print('--------------------------------------------')

# # list()
# print(list(dict2.values()))

# print('----------------------------------------------')
# # tuple()
# print(tuple(dict2.values()))

# print('-----------------------------------------------')
# #set()
# # print(set(dict2.values()))  # TypeError: unhashable type: 'list'

###################################################

# dict2 = {
#     'id': 1001,
#     'cust_name': 'mallesh reddy',
#     'cust_address': 'patancheruvu',
#     'cust_email': 'mallu@gmail.com',
#     'cust_phone': '1234567890',
#     'cust_items':['Tea Powder','Milk packet', 'Rice', 'Jaggery', 'Oil', 'Chilly Powder', 'Salt']
# }


# # items()
# print('original dictionary:')
# print(dict2.items())
# print(type(dict2.items()))

# print('-----------------------------------')

# # list()
# print(list(dict2.items()))

# print('--------------------------------------------')
# # tuple()
# print(tuple(dict2.items()))

# # set()
# print(set(dict2.items()))  #TypeError: unhashable type: 'list'

# d1 = {1:1, 2:2, 3:3, 4:4, 5:5}
# d2 = {'A':'A', 'B':'B', 'C':'C'}

# d1.update(d2)
# print(d1)

##################################################

dict1 = {
    'person1':{
        'name': 'ravi',
        'age':12,
        'parent': 'shwetha',
        'city':'Deharadoon',
        'result':{
            'physics':50,
            'chemistry':100,
            'grade':'B'
        }
        },
    'person2':{
        'name': 'sameer',
        'age':8,
        'parent': 'Fathima',
        'city':'Madurai',
        'result':{
            'physics':50,
            'chemistry':100,
            'grade':'B'
        }
        },
    'person3':{
        'name': 'antony',
        'age':18,
        'parent': 'mayra',
        'city':'ladakh',
        'result':{
            'physics':50,
            'chemistry':100,
            'grade':'B'
        }
    }
}


# access sameer chemistry marks:
print(dict1['person1']['result']['chemistry']) 