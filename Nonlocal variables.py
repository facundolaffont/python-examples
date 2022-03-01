def funcA():
    funcAVar = "funcAVar"

    def funcB():
        # 'nonlocal' allows usage of a variable in a higher hierarchy, but
        # can't be used with a global variable.
        nonlocal funcAVar
        funcAVar = "funcAVarModified"
    
    print(funcAVar)
    funcB()
    print(funcAVar)

funcA()