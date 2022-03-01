class MyClass:
    def myFunc(self):
        print("myFunc")

myClass = MyClass()

# Referencing the instance of a method object.
print(myClass.myFunc.__self__)

# Referencing the function object of a method object.
print(myClass.myFunc.__func__)