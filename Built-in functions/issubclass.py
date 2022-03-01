class MyClass:
    def myFunc(self):
        print("MyClass.myFunc()")

class MyDerivedClass(MyClass):
    def myFunc(self):
        print("MyDerivedClass.myFunc()")

# Verify if a class is a subclass of another class.
print(issubclass(MyDerivedClass, MyClass))