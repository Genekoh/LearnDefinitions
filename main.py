import sys
import random
import PySimpleGUI as sg
import learnDefinition


if __name__ == "__main__":
    if len(sys.argv) <= 1:  # Check for the definition file
        sys.exit("definition file not defined")

    # Open and parse definition file
    file = sys.argv[1]
    f = open(file, "r")
    termsList = learnDefinition.parseDefinitionFile(f.read())

    # Set Color Theme
    sg.theme("LightGray1")

    # Functions
    def genNextTerm(
        ctname, tl
    ):  # Randomly Generates a new Term from the definition list that isn't the same as the current term
        nt = None
        while True:
            nt = random.choice(tl)

            if nt.name != ctname:
                break
        return nt

    # Variables and States
    ansState = False
    randomTerm = genNextTerm("", termsList)
    userAns = ""

    # Initial GUI Layout
    layout = [
        [sg.Text("Learn Definitions", font=("", 20))],
        [sg.Text(f"Term:\t{randomTerm.name}", font=("", 12), key="LINE1TEXT")],
        [
            sg.Text("Definition:\t", font=("", 12), key="LINE2TEXT"),
            sg.Input(font=("", 12), focus=True, visible=True, key="LINE2INPUT"),
        ],
        [
            sg.Button(
                "Reveal Definition",
                font=("", 10),
                bind_return_key=True,
                key="SUBMITBUTTON",
            )
        ],
    ]

    # Creating Window
    window = sg.Window("Window Title", layout)

    # Event Loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        # Dealing with Events in Input Screen
        if ansState == False:
            userAns = values["LINE2INPUT"]

            window["LINE1TEXT"].update(
                value=f"Definition Answer:\t{randomTerm.definition}"
            )
            window["LINE2TEXT"].update(value=f"Your Answer:\t{userAns}")
            window["LINE2INPUT"].update(value="", visible=False)
            window["SUBMITBUTTON"].update(text="Next")

            usreAns = ""
            ansState = True

        # Dealing with Events in Answer Screen
        else:
            randomTerm = genNextTerm(randomTerm.name, termsList)

            window["LINE1TEXT"].update(value=f"Term:\t{randomTerm.name}")
            window["LINE2TEXT"].update(value=f"Definition:\t")
            window["LINE2INPUT"].update(visible=True)
            window["SUBMITBUTTON"].update(text="Reveal Definition")

            ansState = False

    window.close()
