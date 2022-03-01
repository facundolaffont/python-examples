class MyClass:
    def myClassFunc(self):
        print("myClassFunc")
# Defining a class object called MyDerivedClass, that inherits from MyClass.

class MyDerivedClass(MyClass):
    # Redefinition of base class function attribute.
    def myClassFunc(self):
        print("myClassFunc redefined")
    
    def myDerivedClassFunc(self):
        print("myDerivedClassFunc")

myClass = MyClass()
myDerivedClass = MyDerivedClass()

myClass.myClassFunc()
myDerivedClass.myClassFunc()
myDerivedClass.myDerivedClassFunc()