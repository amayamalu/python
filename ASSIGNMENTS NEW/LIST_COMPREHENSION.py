"""1..find all of the words in a string that are less than 4 letters"""

sentence=input("Enter a sentence:")
words=sentence.split( )
print(words)
result=[x for x in words if len(x)<4]
print(result)
#
"""2..Transpose of a matrix is the interchanging of rows and columns"""
matrix=[[1,2],
        [3,4],
        [5,6],
        [7,8]]
transpose=[[row[i] for row in matrix]for i in range(2)]
print(transpose)

"""3..Write a program to extract numbers from a string by using list comprehension"""

stringg="the room number 45 and 67 are vaccant"
new=[x for x in stringg if x.isdigit()]
print(new)


"""4..Write a program to print integer values in a list using list comprehension"""
lst=[2,4,76.8,59,7,89.9,67,8,98.2]
result=[x for x in lst if type(x)==int]
print(result)

"""5.write a program to print the strings that starts with the letter 'c' and end with the letter'b'"""
names=['chb','ydb','thd','hgt','cqyb','cdsjb']
new_names=[i for i in names if i.endswith('b') & i.startswith('c')]
print(new_names)

"""6.DICTIONARY COMPREHENSION:changing from kilogram to pounds"""
old_weights={'book':0.5,'milk':2.0,'tv':7.0}
new_weights={key:value*2.2 for (key,value)in old_weights.items()}
print(new_weights)