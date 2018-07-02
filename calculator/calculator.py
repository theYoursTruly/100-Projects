""" 
    Calculator
    A simple scientific calculator with GUI.

    REQUIREMENTS:
    appJar
"""
import math
from appJar import gui

# GLOBALS
mem = 0     # memory

# Set general app configuration
def configure_gui():
    app.setBg("#333333", override=False)
    app.setPadding([1,1])
    app.setInPadding([7,3])
    app.setFont(size=20, family="Verdana")
    app.setButtonFont(size=14, family="Consolas")
    app.setStretch("both")
    app.setSticky("nesw")

# Assign actions for keys for keyboard control
def set_keybinds():
    for button in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "/",
                   "*", "+", "-", "(", ")", "<BackSpace>", "<Return>", "<Escape>"]:
        app.bindKey(button, key_press)

# React to a keypress
def key_press(key):
    if key == "<BackSpace>":
        undo("")
    elif key == "<Return>":
        calculate("")
    elif key == "<Escape>":
        exit(0)
    elif key in ["1", "2", "3", "4", "5", "6", "7", "8", "9",
                      "0", ".", "/", "*", "+", "-", "(", ")"]:
        push(key)

""" Create a gui (buttons and such)

UI looks like this:
[                       operation ]
[                          result ]
[ MC][ MR][ M+][ ( ][ ) ][ % ][ : ]
[sin][cos][tan][ 7 ][ 8 ][ 9 ][ x ]
[x^y][ √ ][mod][ 4 ][ 5 ][ 6 ][ - ]
[log][ ln][ x!][ 1 ][ 2 ][ 3 ][ + ]
[ e ][ π ][ . ][ C ][ 0 ][      = ]
"""
def draw_ui():
    # row 0
    app.addLabel("operation", "", 0, 0, 7)
    app.setLabelAlign("operation", "right")
    app.setLabelFg("operation", "grey")
    # row 1
    app.addNumericEntry("result", 1, 0, 7)
    app.setEntry("result", "0", callFunction=True)
    app.setEntryAlign("result", "right")
    # row 2
    for idx, elem in enumerate([" MC", " MR",  " M+"]):
        app.addButton(elem, memory, 2, idx)
    for idx, elem in enumerate([" ( ", " ) ", " % ", " : "], 3):
        app.addButton(elem, push, 2, idx)
    # row 3
    for idx, elem in enumerate(["sin", "cos", "tan", " 7 ", " 8 ", " 9 ", " x "]):
        app.addButton(elem, push, 3, idx)
    # row 4
    for idx, elem in enumerate([" x\u207F", " √ ", "mod", " 4 ", " 5 ", " 6 ", " - "]):
        app.addButton(elem, push, 4, idx)
    # row 5
    for idx, elem in enumerate(["log", " ln", " x!", " 1 ", " 2 ", " 3 ", " + "]):
        app.addButton(elem, push, 5, idx)
    # row 6
    for idx, elem in enumerate([" e ", " π ", " . "]):
        app.addButton(elem, push, 6, idx)
    app.addButton(" C ", undo, 6, 3)
    app.addButton(" 0 ", push, 6, 4)
    app.addButton("       = ", calculate, 6, 5, 2)

# Add given character to the current calculation line
def push(button):
    text = button.strip()
    if text == "x\u207F":
        text = "^2"
    elif text == "x!":
        text = "!"
    app.setLabel("operation", app.getLabel("operation") + text)

# Manage calculator memory
def memory(button):
    global mem
    if button.strip() ==  "MC":
        mem = 0
    if button.strip() ==  "MR":
        app.setEntry("result", mem)
    if button.strip() ==  "M+":
        mem += app.getEntry("result")

# Remove last character from the current calculation line
def undo(button):
    operation = app.getLabel("operation")
    if len(operation) > 0:
        operation = operation[:-1]
        app.setLabel("operation", operation)

# Make an actual calculation
def calculate(button):
    pass #TODO

if __name__ == "__main__":
    with gui("Calculator") as app:
        configure_gui()
        set_keybinds()
        draw_ui()
