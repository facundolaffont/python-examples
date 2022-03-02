# Tuples are one of the four built-in data types in Python to store collections of data.
# The other three are List, Set, and Dictionary. A tuple is a collection of different types
# of data which is ordered, unchangeable after creation, and allow duplicate values.
# Its elements are indexed, from 0.

# Creating a tuple.
colors = "Red", "Green", "Blue" # Same as 'colors = ("Red", "Green", "Blue")'
                                # and 'colors = tuple(("Red", "Green", "Blue"))' (notice the double parenthesis).

# Referencing its values.
print(colors)

# Referencing one of its values.
print(colors[1])

# Printing the lenght of the tuple.
print(len(colors))

# Creating a tuple with one item (it's important to write the final comma).
newColor = "Magenta", # Same as 'newColor = ("Magenta",)'.
print(type(newColor))

# Creating a tuple with different values.
myTuple = "Dog", 50, True
print(type(myTuple))
print(myTuple)

# Unpaking a tuple: that is asigning each value of the tuple in the right side
# of the equal sign to the variables in the left side, in the order proposed.
colorA, colorB, colorC = colors # Same as '(colorA, colorB, colorC) = colors'.
print(colorA)
print(colorB)
print(colorC)

# Creating another tuple.
moreColors = "Black", "Yellow", "Purple", "Orange", "Cyan"

# When unpacking, an asterisc mean that the adjacent variable (the asterisc must be
# placed at the left side of a variable) will store all the necesary tuple values to
# complete asignation in the order proposed, and they will be stored as a list.
colorA, *colorB, colorC = moreColors
print(colorA)
print(colorB)
print(colorC)