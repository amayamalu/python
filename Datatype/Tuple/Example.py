tp=("annu","amaya",1,2,3,4,[5,6])
print(tp)

"""ACCESSING ELEMENTS"""
marks=(50,60,70)
print(marks[1])
print(tp[6][1])

"""change"""
tp=("annu","amaya",1,2,3,4,[5,6])
print(tp)
tp[6][1]=23
print(tp)

"""count"""
tp=("annu","amaya",1,3,3,2,3,4,[5,6])
print(tp.count(3))

"""membership in python"""
my_tuple=("amaya","anu","aju")
print("amaya" in my_tuple )
print("vishnu" in my_tuple)


"""iterating through a tuple"""
names=('anu','aju','ali')
for name in names:
    print("hello",name)


"""BUILTIN FUNCTIONS"""