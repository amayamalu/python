"""STRING"""
#find()
a="luminar tecnolab"
print(a.find("r"))
print(a.find("l"))
print(a.find("y"))
ab="luminar technolab"
print(ab.find("a",1,6))
print()

#index()
abc="amaya"
print(abc.index("m"))

#count()
print(abc.count("a",0,3))

#rfind()
print(a.rfind("mi")) #starting of the word

str1="hello"
str2="python"
ac=str1+str2
print(ac)
print()

#indexing
str1="hello world"
print(str1[3])
print(str1[0:5])
print(str1[-1])
print(str1[::-1])
print(str1[:-6])
print(str1[-1:6:-1])
print()

"""QUESTIONS"""
a="amaajan Annna kla"
print(a.istitle())
w=a.split("a")
print(w)
print(a.strip())


"""
1....
What is an f-string and how do you use it?
New in python 3.6, f-strings make string interpolation really easy. Using f-strings is similar to using format().

F-strings are denoted by an f before the opening quote.

name = 'Chris'
food = 'creme brulee'
f'Hello. My name is {name} and I like {food}.'
#=> 'Hello. My name is Chris and I like creme brulee

2....
difficulty = 'easy'
thing = 'exam'
'That {} was {}!'.format(thing, difficulty)
#=> 'That exam was easy!'

3...
Join a list of strings into a single string, delimited by hyphens
Python’s join() function can join characters in a list with a given character inserted between every element.

'-'.join(['a','b','c'])
#=> 'a-b-c

4...
 Remove whitespace from the left, right or both sides of a string
lstrip(), rstrip() and strip() remove whitespace from the ends of a string.

string = '  string of whitespace    '
string.lstrip() #=> 'string of whitespace    '
string.rstrip() #=> '  string of whitespace'
string.strip() #=> 'string of whitespace


5...
Remove vowels from a string
One option is to iterate over the characters in a string via list comprehension. If they don’t match a vowel then join them back into a string.

string = 'Hello 1 World 2'
vowels = ('a','e','i','o','u')
''.join([c for c in string if c not in vowels])
#=> 'Hll 1 Wrld 2''"""


"""LISTT IN PYTHON"""

















