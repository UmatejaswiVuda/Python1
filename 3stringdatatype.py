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

# str1 = 'Hello Buddy, This is Shiv here, luck..!'

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


# isalpha()
# str1 = 'grapes'
# print(str1.isalpha())

# str2 = 'Grapes'
# print(str2.isalpha())

# str3 = 'Grape@'
# print(str3.isalpha())

# str4 = 'Grape12223'
# print(str4.isalpha())

# str5 = 'Grapes@123'
# print(str5.isalpha())

# isdigit()
# str11 = '12345'
# print(str11.isdigit())

# str12 = 'g@123'
# print(str12.isdigit())

# str13 = '123.45'
# print(str13.isdigit())

# str14 = '12 23 34 56'
# print(str14.isdigit())

# isalnum()

# str15 = '123456qwert'
# print(str15.isalnum())

# str16 = 'Ganesh@123'
# print(str16.isalnum())

# str17 = '12356789'
# print(str17.isalnum())

# str18 = 'asdfghj'
# print(str18.isalnum())

# isspace()
# str19 = '     .'
# print(str19.isspace())


#islower()
# str20 = 'asdfgh'
# print(str20.islower())

# str21 = 'asdfghj234'
# print(str21.islower())

# str22 = 'qertyu@134'
# print(str21.islower())

# str23 = 'ASDFGHJ'
# print(str23.islower())

# str24 = 'XCVBNM'.lower()
# print(str24.islower())

# str25 = 'sdfghj'.upper()
# print(str25.islower())

# isupper()
# str26 = 'asdfghj'
# print(str26.isupper())

# str27 = 'ERTYU'
# print(str27.isupper())

# str28 = '2345678'
# print(str28.isupper())


# istitle()

# str29 = 'Python Is Great'
# print(str29.istitle())

# str30 = 'I Am 29 Years Old'
# print(str30.istitle())

####################################

# strip()

str31 = '    Helloo    Bujji     '
print(str31)

# print(str31.strip())
# print(str31.lstrip())
# print(str31.rstrip())

#######################################

# INDEXING 
    # Positive Indexing:-
        # positive indexing start from 0
        # positive indexing goes left to right
    
    # Negative Indexing
        # negative indexing starts from -1
        # negative indexing goes right to left
        

# str32 = 'Where what there is will, there is will a way'
# print(str32.find('will'))
# print(str32.index('will'))
# print(str32.rfind('will'))

# print(str32.rindex('will'))

##############################3

# SLICING

str33 =  'MANORAMA'
print(str33[0:3:1])

print(str33[4:7:1])