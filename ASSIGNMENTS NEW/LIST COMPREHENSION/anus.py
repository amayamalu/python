"""5.write a program to print the strings that starts with the letter 'c' and end with the letter'b'"""
names=['chb','ydb','thd','hgt','cqyb','cdsjb']
new_names=[i for i in names if i.endswith('b') & i.startswith('c')]
print(new_names)
