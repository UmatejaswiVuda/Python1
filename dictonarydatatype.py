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

employee_info = {
    'empId': '10001',
    'empPosition': 'Senior Engineer',
    'empName': 'Vishal',
    'empEmail': 'vishal@gmail.com',
    'empSalary': 50000,
    'empCompany': 'IBM'
}

employee_info['empEmail'] = 'vishal123@gmail.com'
employee_info['empCompany'] = 'Microsoft'
employee_info['empPf'] = 5000
employee_info['isMarried'] = True

print(employee_info)
