#find()    return -1 if the value is not find
a='luminar technolab'
print(a.find('l'))
print(a.find('o'))
print(a.find('m',1,6))
print(a.find('l',8,16))
print(a.find('u',4,9))   #returns -1

#index()   return value error if string is not found
b='amala paul'
print(b.index('l'))
print(b.index('m',0,4))
#print(b.index('x'))      #value error

#rfind()
c='this is a good is example'
print(c.rfind('is'))   #last index will be exxecuted

#count()
f="eagle eyes"
print(f.count('e'))
print(f.count('e',0,5))