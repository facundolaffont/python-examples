class MyClass:
    # To allow name mangling over a data attribute, its name should
    # be preceded with at least two underscores.
    __Attr = "MyClass.__Attr"
    ___Attr = "MyClass.___Attr"
    __Attr_ = "MyClass.__Attr_"
    ___Attr_ = "MyClass.___Attr_"

print(MyClass._MyClass__Attr) 
print(MyClass._MyClass___Attr)
print(MyClass._MyClass__Attr_)
print(MyClass._MyClass___Attr_)
# The following objects don't exist, because of data mangling mechanism:
#   MyClass.__Attr
#   MyClass.___Attr
#   MyClass.__Attr_