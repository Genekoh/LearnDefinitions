class Term:
    def __init__(self, name, definition):
        self.name = name
        self.definition = definition

    def compareDefinitions(self, userAns):
        if userAns == self.definition:
            return True

        return False


def convertLinesToTerms(l):
    t = l.split(" - ", 1)
    if len(t) == 1:
        return

    return Term(t[0], t[1])


def parseDefinitionFile(fileText):
    try:
        lines = fileText.split("\n")
        termsList = list(filter(lambda t: t != None, map(convertLinesToTerms, lines)))

        return termsList

    except:
        print("an error has occured whie parsing definition file")
        return None
