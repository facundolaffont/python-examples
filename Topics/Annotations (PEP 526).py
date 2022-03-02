# Type annotation was introduced in Python in PEP 526
# in order to allow a better type cheking for third party
# software.

from typing import List, Tuple, Optional, ClassVar

varA: int # Variable without initial value.
varB: List[int] = [] # Variable with initial value.
varC: Tuple[int, ...] = (1, 2, 3) # Tuple packing with variable annotation syntax.
varD: Tuple[int, ...] = 1, 2, 3  # This only works in Python 3.8+.
varE: int = 'a' # Although this is going to produce an error in the third party
                # checker, it doesn't produce an error in Python console.
# Annotated variables without initial values can't be referenced.

# Tuple unpacking with variable annotation syntax.
header: str
kind: int
body: Optional[List[str]]
message = "Header", "Kind", "Body"
header, kind, body = message

# Also, duplicate type annotations are ignored.
varF: int
varF: str

# Class annotations.
class MyClass:
    varA: str = 'My varA inside MyClass' # Instance variable with default value.
    varB: int # Instance variable without default value.
    varC: ClassVar[int] = 5 # Class variable with default value
                             # (is mandatory to define it).
# Class annotations, if they are simple names, are stored in an attribute
# called __annotations__.
print(MyClass.__annotations__)

# Also the module has its __annotations__ attribute.
print(__annotations__)

# Annotations are writable.
__annotations__['varF'] = str

# Expression annotations.
(x): int # (x) is treated as an expression.
(y): int = 0 # (y) is treated as an expression.

# Annotations in for and with: variables that are part of 'for' and 'with'
# blocks should be annotated before the corresponding block.
"""
a: int
for a in myIterationVar:
    pass

f: MyFile
with myFunc() as f:
    pass
"""