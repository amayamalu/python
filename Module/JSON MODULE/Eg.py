import json
print(dir(json))
#json
x='{"name":"amaya","age":12,"place":"vadakara"}'
print(type(x))

#parsing json to python
# y= json.loads(x)
# print(y)
# print(type(y))

#python to json
y=json.dump(x)
print(x)
print(type(x))
