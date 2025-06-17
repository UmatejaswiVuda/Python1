# STRING DATATYPE:-
    # String is a sequence of charecters.
    # String is an immutable datatype. --> Once created can not be modified.
    # String is an Ordered Datatype.--> It supports Indexing.
    # String must initialized inside quotes.
        # single quotes --> ''
        # double quotes --> ""
        # tripple single quotes --> ''' '''
        # tripple double quotes --> """ """

# EXAMPLES OF INITIALIZING STRING:-

# str_1 = 'python'
# print(str_1)
# print(type(str_1))  #<class 'str'>

# str_2 = "Angular"
# print(str_2)
# print(type(str_2))

# str_3 = '''MS SQL SERVER'''
# print(str_3)
# print(type(str_3))

# str_4 = """Django"""
# print(str_4)
# print(type(str_4))


# str_5 = '''Sujith is the """tallest among all""" the classmates.'''

# str_6 = 'ameerpet'
# str_7 = "Punjagutta"

# str_8 = '''This is a python class. class starts at 9 am ist'''

# METHODS:-
    # Methods are nothing but functions where the programme/ code/ functionality is defined.
    
    # Built in methods
    # user defined methods.
    
# SOME BUILT IN METHODS OF STRING:-

    # CASE CONVERSION METHODS:-
        # CASE CONVERSION METHODS IMPLY UPON ONLY THOSE CHARECTERS WHICH
        # ARE ALPHABETIC IN STRING.
        
        # str_9 = 'SAM@123'
        
# str_10 = 'jamaica'

# print(str_10.lower())  #jamaica
# print(str_10.upper())  #JAMAICA

# str_11 = "INDIA"
# print(str_11.lower())  # india
# print(str_11.upper())  # INDIA



# str_12 = 'sam@123'
# print(str_12.lower())  #sam@123
# print(str_12.upper())  #SAM@123


# str_13 = '''inida is my country, all indians are my brothers.'''

# print(str_13.lower())  #inida is my country, all indians are my brothers.
# print(str_13.upper())  #INIDA IS MY COUNTRY, ALL INDIANS ARE MY BROTHERS.
# print(str_13.capitalize())  #Inida is my country, all indians are my brothers.
# print(str_13.title()) #Inida Is My Country, All Indians Are My Brothers.


# str_14 = 'aPplE a DAy kEEpS DoctoR AWay.'
# print(str_14.swapcase()) #ApPLe A daY KeePs dOCTOr awAY.

######################################

# SEARCH & REPLACE METHODS:-

str1 = 'Hello Buddy, This is Shiv here, luck..!'

# find()
# print(str1.find('B'))
# print(str1.find('Z'))

# print(str1.find('l'))

# rfind()
# print(str1.rfind('l'))
# print(str1.rfind('k'))
# print(str1.rfind('j'))

str1 = 'Hello Buddy, This is Shiv here, luck..!'
# index()
# print(str1.index('B'))
# print(str1.index('l'))
# print(str1.index('z'))   #ValueError: substring not found

# rindex()
# print(str1.rindex('l'))
# print(str1.rindex('w'))  #ValueError: substring not found

# replace()
# str2 = 'Apple A Day Kepps Doctor Away'

# print(str2.replace('A', 'a')) #apple
# print(str2)


##############################################
# CHECKING CONTENT 

str3 = 'My Dear Friend'

# strtswith()
# print(str3.startswith('My'))  #True
# print(str3.startswith('my'))  #False
# print(str3.startswith('My  Dear')) #False
# print(str3.startswith('My Dea')) #True
# print(str3.startswith(' My Dear')) #False
# print(str3.startswith('My Dear Friend'))

str3 = 'My Dear Friend'
# endswith()
# print(str3.endswith('My Dear')) #False
# print(str3.endswith('end'))  #True
# print(str3.endswith('Friend'))
# print(str3.endswith('My Dear Friend')) #True




