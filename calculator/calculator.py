""" 
    Calculator
    A simple scientific calculator with GUI.

    REQUIREMENTS:
    appJar
"""
import math
from appJar import gui


""" UI looks like this:
[                          result ]
[ MC][ M+][ M-][ ( ][ ) ][ % ][ : ]
[sin][cos][tan][ 7 ][ 8 ][ 9 ][ x ]
[x^y][ √ ][mod][ 4 ][ 5 ][ 6 ][ - ]
[log][ ln][ x!][ 1 ][ 2 ][ 3 ][ + ]
[ e ][ π ][ . ][ C ][ 0 ][      = ]
"""
def draw_ui():
    # row 0
    app.addSelectableLabel("result", "0", 0, 0, 7)
    # row 1
    for idx, elem in enumerate([" MC", " M+",  " M-"]):
        app.addButton(elem, memory, 1, idx)
    for idx, elem in enumerate([" ( ", " ) ", " % ", " : "], 3):
        app.addButton(elem, operation, 1, idx)
    # row 2
    for idx, elem in enumerate(["sin", "cos", "tan", " 7 ", " 8 ", " 9 ", " x "]):
        app.addButton(elem, operation, 2, idx)
    # row 3
    for idx, elem in enumerate([" x\u207F", " √ ", "mod", " 4 ", " 5 ", " 6 ", " - "]):
        app.addButton(elem, operation, 3, idx)
    # row 4
    for idx, elem in enumerate(["log", " ln", " a!", " 1 ", " 2 ", " 3 ", " + "]):
        app.addButton(elem, operation, 4, idx)
    # row 5
    for idx, elem in enumerate([" e ", " π ", " . ", " C ", " 0 "]):
        app.addButton(elem, operation, 5, idx)
    app.addButton("       = ", calculate, 5, 5, 2)

def operation(button):
    pass    # TODO

def memory(button):
    pass    # TODO

def calculate(button):
    pass    # TODO


if __name__ == "__main__":
    app = gui("Calculator")
    app.setIcon("appJar/resources/icons/calculator-alt.png")
    app.setBg("white", override=False)
    app.setPadding([1,1])
    app.setInPadding([7,3])
    app.setFont(size=20, family="Verdana")
    app.setButtonFont(size=14, family="Consolas")

    draw_ui()

    app.go()
