class MyClass:
    attr = "MyClass.attr" # Class attribute of MyClass defined.

    def myClassFunc(self):
        print("myClassFunc")
# Defining a class object called MyDerivedClass, that inherits from MyClass.

class MyDerivedClass(MyClass):
    def __init__(self):
        self.attr = "self.attr" # MyClass.attr, which is a class data attribute,
                                # is this way overriden by an instance data attribute,
                                # and Python prioritizes this last data attribute,
                                # as show later.

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

# Showing how Python prioritizes an instance data attribute over a class one.
print(MyDerivedClass.attr) # It prints, as is supposed, the class data attribute that is inherited from MyClass.
print(myDerivedClass.attr) # It prints the instance data attribute, not the class data attribute.