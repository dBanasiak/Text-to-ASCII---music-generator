def CREATE_SYMPHONY(numString):
    trioArr = SET_TRIO(numString)
    notes = SET_SOUND(trioArr)
    return notes

def SET_TRIO(numString):
    newArr = []
    temp = []
    string = ''

    for x in range(0, int(len(numString) / 3)):
        for i in range(0, 3):
            temp.append(numString[0])
            numString = numString[1:]
        string = string.join(temp)
        newArr.append(string)
        temp = []
        string = ''
    return newArr

def SET_SOUND(trioArr):
    temp = ''

    for trio in trioArr:
        note = SET_NOTE(trio[0])
        octave = int(SET_OCTAVE(trio[1]))
        lengt = SET_LENG(trio[2])
        leng = '(1/' + str(lengt) + ')'
        if lengt == 1:
            notes = str(note) + ' ' + str(octave) + ' ' + str(leng) + " :=: "
        else:
            notes = str(note) + ' ' + str(octave) + ' ' + str(leng) + " :+: "
        temp = notes + temp
    return temp

def SET_NOTE(numNote):
    numNote = int(numNote)

    if numNote == 1:
        return 'a'
    elif numNote == 2:
        return 'b'
    elif numNote == 3:
        return 'c'
    elif numNote == 4:
        return 'd'
    elif numNote == 5:
        return 'e'
    elif numNote == 6:
        return 'f'
    elif numNote == 7:
        return 'g'
    elif numNote == 8:
        return 'a'
    elif numNote == 9:
        return 'b'

def SET_OCTAVE(octNote):
    octNote = int(octNote)

    if octNote <= 5:
        return octNote
    elif octNote % 2 == 0:
        return octNote / 2
    else:
        return (octNote - 1) / 2

def SET_LENG(lenNote):
    lenNote = int(lenNote)

    if lenNote % 2 == 0:
        return lenNote
    elif lenNote == 1:
        return 1
    else:
        return lenNote - 1