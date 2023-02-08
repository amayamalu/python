"""FUNCTION OVERRIDING"""
class rectangle:
    def area(self,l,b):
        print("the area of rectangle is:",l*b)  #base class method is virtual
class square(rectangle):
    def area(self,l,b):
        print("the area of square is:",l*b)
obj=square()
obj.area(10,20)

