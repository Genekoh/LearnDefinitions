import sys
import learnDefinition
from tkinter import *

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit("definition file not defined")

    file = sys.argv[1]
    f = open(file, "r")
    termsList = learnDefinition.parseDefinitionFile(f.read())
    for i in termsList:
        print(i.name)

    root = Tk()

    root.mainloop()
