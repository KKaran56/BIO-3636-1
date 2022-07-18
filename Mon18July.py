
# Monday 18 July 2022

# Functions that we have already used:
    # abs()
    # len()
    # sum()
    # These are default functions that are already inbuilt in python.

# We can write our own functions.

# Function to find the fluctuation index.
def fl_index(a):
    b = [abs(a[i + 1] - a[i] for i in range(len(a) - 1))]
    fi = sum(b) / sum(a)
    return fi

# Function to find the cube of a number.
def cube(a):
    return a**3

# Importing the function.
from fluctuation import fl_index

# We can store the name of the function inside a list.
a = [sq, cube, qd, penta]
for i in a:
    print(i(3))

# Making graphical user interfaces with easygui.
import easygui
# or
import easygui as eg
eg.msgbox("Hello world!")
from easygui import *
msgbox("Hello world!")
msgbox(msg = "Hello world!", title = "Message box")
a = buttonbox(msg = "How are you?", title = "Just checking", choices = ["Good", "not well"])
print(a)
a = choicebox(msg = "How are you?", title = "Just checking", choices = ["Good", "not well"])
print(a)
a = multchoicebox(msg = "How are you?", title = "Just checking", choices = ["Good", "not well"])
print(a)
a = enterbox(msg = "How are you?", title = "Just checking")
print(a)
fileopenbox()