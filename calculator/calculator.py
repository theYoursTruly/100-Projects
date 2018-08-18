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
[ MC][ MR][ M+][ ( ][ ) ][ % ][ / ]
[sin][cos][tan][ 7 ][ 8 ][ 9 ][ * ]
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
    for idx, elem in enumerate([" ( ", " ) ", " % ", " / "], 3):
        app.addButton(elem, push, 2, idx)
    # row 3
    for idx, elem in enumerate(["sin", "cos", "tan", " 7 ", " 8 ", " 9 ", " * "]):
        app.addButton(elem, push, 3, idx)
    # row 4
    for idx, elem in enumerate([" xⁿ", " √ ", "mod", " 4 ", " 5 ", " 6 ", " - "]):
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
    if text == "xⁿ":
        text = "^"
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

# Process equal button pressing
def calculate(button):
    text = "0" if app.getLabel("operation") == "" else app.getLabel("operation")
    result = process("(" + text + ")")
    app.setLabel("result", result)

# Process text and print the result of calculations
def process(text):
    result = 0
    pos = 1
    number_str = ""
    number_dig = 0
    while pos <= len(text)-2:
        char_type, valid = get_type(text[pos], text[pos-1], text[pos+1]):
        if not valid:
            result = 0
            break
        if char_type == "number" or char_type == "dot":
            number += text[pos]
        elif char_type == "extra":
            number = str(math.pi) if text[pos] == "π" else str(math.e)
        elif char_type in ["preop", "postop", "dblop"]:

        pos += 1
    app.setLabel("result", result)

# Each character is either a number, extra number or operator.
# Check what it is and if it has valid neighbours.
# |Group            | Allowed after        | Can be followed by   | Members                     |
# | --------------- | -------------------- | -------------------- | --------------------------- |
# |Number           | Number, Operator     | Number, Operator     | 0 .. 9                      |
# |Extra number     | Operator             | Operator             | e, π                        |
# |Prefix operator  | Number, Extra number | Operator             | x!, %, )                    |
# |Postfix operator | Operator             | Number, Extra number | (, √, ln, log, sin, cos, tan|
# |Double operator  | Number, Extra number | Number, Extra number | /, *, -, +, xⁿ, mod         |
# |Dot operator     | Number               | Number               | .                           |
def get_type(item, pre, post):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    extras  = ["e", "π"]
    dot     = ["."]
    preop   = ["!", "%", ")"]
    postop  = ["(", "√", "ln", "log", "sin", "cos", "tan"]
    dblop   = ["/", "*", "-", "+", "^", "mod"]
    operators = dot + preop + postop + dblop
    
    if item in numbers:
        return ("number", pre in (numbers + operators) and post in (numbers + operators))
    elif item in extras:
        return ("extra", pre in operators and post in operators)
    elif item in preop:
        return ("preop", pre in (numbers + extras) and post in operators)
    elif item in postop:
        return ("postop", pre in operators and post in (numbers + extras))
    elif item in dblop:
        return ("dblop", pre in (numbers + extras) and post in (numbers + extras))
    elif item in dot:
        return ("dot", pre in numbers and post in numbers)
    else: # fail any other character
        return ("unknown", False)

if __name__ == "__main__":
    with gui("Calculator") as app:
        configure_gui()
        set_keybinds()
        draw_ui()
