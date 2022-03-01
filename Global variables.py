# Global variable defined.
myGlobalVar = "myGlobalVar"

def myFunc():
    global myGlobalVar # 'global' allows usage of a global variable.
    myGlobalVar = "myGlobalVarModified"

print(myGlobalVar)
myFunc()
print(myGlobalVar)