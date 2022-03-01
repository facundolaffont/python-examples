class MyClass:
    def myFunc(self):
        print("MyClass.myFunc()")

class MyDerivedClass(MyClass):
    def myFunc(self):
        print("MyDerivedClass.myFunc()")

myClass = MyClass()
myDerivedClass = MyDerivedClass()

# Verify if myClass is an instance of MyClass.
print(isinstance(myClass, MyClass))
print(isinstance(myDerivedClass, MyClass))