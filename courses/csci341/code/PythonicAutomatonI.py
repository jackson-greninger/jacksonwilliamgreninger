def state1(instring):
    if instring == "":
        return True
    else:
        if instring[0] == "0":
            return state2(instring[1:])
        elif instring[0] == "1":
            return state1(instring[1:])


def state2(instring):
    if instring == "":
        return False
    else:
        if instring[0] == "0":
            return state2(instring[1:])
        elif instring[0] == "1":
            return state1(instring[1:])


# This just runs the program
while True:
    instring = input("Enter a string of 0s and 1s or quit: ")
    if "quit" in instring.lower():
        break
    else:
        print(state1(instring))

        