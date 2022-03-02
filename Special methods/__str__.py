class MyClass:
    def __init__(self, attrA, attrB, attrC):
        self.attrA = "attrA"
        self.attrB = "attrB"
        self.attrC = "attrC"

    def __str__(self):
        return f'"({self.attrA}, {self.attrB}, {self.attrC})"'

myInstance = MyClass("A", "B", "C")
print(myInstance) # Same as 'print(str(myInstance))'