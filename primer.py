# Coursera course: Data science with real world data in Pharma
# Date: May 07, 2026


# Comments start with a '#' sign. 
# you can print with the print() function
print("Hello, World!")
# the assignent to a variable is done with = 
a = 1
print(a)

# 1 - Basic data types
# 1.1 Numbers
# integers
a = 1
print(a)
print(type(a))
# floats
b = 2.0 
print(b)
print(type(b))

# you can do the basic operations as expected
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# you can do the logical comparisons as expected
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

# 1.2 strings
c = "I am a string"
print(c)
# you can use single or double quotes
d = 'another string'
# you can concatenate strings with the + operator
print(c+d)
print(c+", "+d)

# 1.3 Booleans
# Booleans are True or False (observe the capital first letter!)
print(True==True)
print(False==True)

2 - Basic data structures
# 2.1 Lists 
# lists can contain elements of any type, you can define them with square brackets
alist = [10, 20, a, b, c, d]
print(alist)
# check if an element is in the list
print( 20 in alist)
# add elements 
alist.append(50)
print(alist)
# reference elements: index starts at 0 in python!
print(alist[0])
print(alist[2])
print(alist[-1])
# change an element
alist[0] = 100 
print(alist)

# 2.2 Dictionaries 
# define a dictionary with curly brackets
adict = {'a': 1, 'b': [1,2,3]}
# retrieve element by key
print(adict['a'])
print(adict['b'])
# add an element 
adict['c'] = "a string"
print(adict)

3 - Flow Control
# 3.1 For loops
numbers = [1,2,3,4,5]
print(numbers)

# for loop, observe the indentation and the colon!
for n in numbers: 
    print(n)

# 3.2 If, elif, else
a = 10 
if a <= 3:
    print("A")
elif a>3 and a<=7:
    print("B")
else:
    print("C") 

4 - Pandas dataframes
In Python there is not a native dataframe data type, therefore we need to use a third party package. The most used at the moment is pandas. 
In order to use it, the first thing we need to do is to import it. We can then use the keyword "as" to give it a shorter alias, by convention "pd". 
Once imported we can access its methods (functions insdide an object) with the dot.

import pandas as pd

# Let's define a simple dataframe from a dictionary of lists, where each list is a column
patients = ['patient1', 'patient2', 'patient3']
age = [60, 65, 70]
dead = [True, False, True]
disease = ['lung cancer', 'diabetes', 'coronary disease']

# the keys in the dictionary will be the column names
datadict = {'patients': patients, 
    'age': age,
    'dead': dead,
    'disease': disease}

# define a dataframe
df = pd.DataFrame(datadict)
# By default, the Jupyter Notebook will display the last object in the cell
df

# describe numerical variables (use include='all' to include everything)
df.describe()

# As you have seen Jupyter displays the last object in the cell, but you can also use the print function
# to print objects explicitly in the middle of the cell
# how many rows (observations)
print(len(df))
# what columns do I have?
df.columns

# What are the data types?
df.dtypes

# In addition to the print function we can also use the display function to show objects in a nicer format
from IPython.display import display
# look at one column
display(df['dead'])
# the dot notation also works
df.dead

# look at the top n rows
df.head(5)

# slicing and filtering with the loc method
df.loc[df['dead']==True]

# get only a couple of columns
df.loc[df.dead==True, ['patients', 'disease']]

# get elemennts that are in a list
df.loc[df['disease'].isin(['diabetes', 'coronary disease'])]

# adding a new columns
df['new_columns'] = df.age/2
df

5 - Functions
# We define functions with the keyword "def"
# return is mandatory, observe the indentation and the colon!
def mult(number):
    return number*2

print(mult(5))

# we can use default arguments when defining our functions
def mult2(number, multiplier=2):
    return number*multiplier
print(mult2(5))
print(mult2(5, multiplier=5))

# recoding with apply 
def remap_disease(disease):
    if disease == "lung cancer":
        return 'LC'
    elif disease == 'diabetes':
        return 'DB'
    elif disease == 'CD':
        return 'CD'
    else: 
        return 'ERROR'

# let's first test with a single string
print(remap_disease('diabetes')) 

# now recode the whole column with apply
df['disease3'] = df['disease'].apply(remap_disease)
# let's look at the result
df.head() 





