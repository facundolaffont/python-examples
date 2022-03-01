# 'global myGlovalVar = <definition>' Doesn't work.
global myGlobalVar
myGlobalVar = "myGlobalVar"

def myFunc():
    global myGlobalVar # If I don't declare this, I can't use the global
                       # variable inside myFunc.
    print("myFunc(): " + myGlobalVar)
    myGlobalVar = "myGlobalVarModified"
    print("myFunc(): " + myGlobalVar)

    myLocalVar = "myLocalVar"
    mySecondLocalVar = "mySecondLocalVar"

    def mySecondFunc():
        nonlocal myLocalVar # If I don't use 'nonlocal' I can't reference the outer variable 'myLocalVar'.
        print("mySecondFunc(): " + myLocalVar)
        myLocalVar = "myLocalVarModified"
        print("mySecondFunc() " + myLocalVar)

        mySecondLocalVar = "mySecondLocalVarModified" # Due to not using 'nonlocal', 'mySecondLocalVar is local,
                                                      # and modifications only apply to this local scope.
        print("mySecondFunc(): " + mySecondLocalVar)
    
    print("myFunc(): " + myLocalVar)
    print("myFunc(): " + mySecondLocalVar)
    mySecondFunc()
    print("myFunc(): " + myLocalVar)
    print("myFunc(): " + mySecondLocalVar)

print("global: " + myGlobalVar)
myFunc()
print("global: " + myGlobalVar)
