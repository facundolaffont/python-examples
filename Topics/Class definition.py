# Defining a class function outside of its class.
def functionDefinedOutside(self):
    return "functionDefinedOutside"

# Class definition.
class MyClass:
    classDataAttr = "MyClass data attribute" # Class data attribute definition.

    def __init__(self, instanceDataAttrValue): # Constructor definition.
        # Instance data attribute, called instanceDataAttr, added here. It'll be
        # created when the instance is constructed.
        self.instanceDataAttr = instanceDataAttrValue
    
    # Function object definition, that'll become a method instance attribute (also called
    # method object) when the instance is created.
    def myClassFunc(self): # The first argument of a class function not necesarily has to be
                           # called 'self', although there has to be an argumento, and this name
                           # is used by convention (some class browser may look for an argument
                           # called 'self', so this name is recommended).
        return self.instanceDataAttr

    def myOtherFunc(self):
        return self.myClassFunc() # This is how a class function calls another class function.

    # Adds function defined outside to this class definition.
    myFuncDefinedOutside = functionDefinedOutside
# When interpreter gets here, MyClass class object is created, and then it can be used to instantiate.

myNumber = 50
if(myNumber == 50):
    # Defining a class object inside an if statement (if myNumber value is changed,
    # the class will not be created).
    class ClassDefinedInsideIf():
        attr = "ClassDefinedInsideIf data attribute"
    # Here, ClassDefinedInsideIf is created.

# Defining a class object inside a function definition.
def myFunc():
    class ClassDefinedInsideFunction():
        attr = "ClassDefinedInsideFunction data attribute"
    # Here, ClassDefinedInsideFunction is created.

    return ClassDefinedInsideFunction()

# Creating an instance of MyClass.
myClass = MyClass("Instance data attribute inside myClass")

# Creating an instance of ClassDefinedInsideIf.
myClassInsideIf = ClassDefinedInsideIf()

# Creating an instance of ClassDefinedInsideFunction.
myClassInsideFunction = myFunc()

# Referencing an instance data attribute.
print(myClass.instanceDataAttr)

# Referencing method objects.
print(myClass.myClassFunc()) # Same as MyClass.myClassFunc(myClass)
print(myClass.myOtherFunc()) # Same as MyClass.myOtherFunc(myClass)
print(myClass.myFuncDefinedOutside()) # Same as MyClass.myFuncDefinedOutside(myClass)

# Referencing class data attributes.
print(myClassInsideIf.attr) # Same as print(ClassDefinedInsideIf.attr)
print(myClassInsideFunction.attr) # Same as print(ClassDefinedInsideFunction.attr)

# Printing an object's class.
print(myClass.__class__)