konsonant = [ 'b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'j']
vokaler = ['a', 'e', 'i', 'o', 'u', 'y', 'å','ä','ö']


word  = input("Välj ord: ")

def Rövar(konsonant, vokaler):
    mening = []
    for i in range(len(word)):
        if word[i] in vokaler:
            mening.append(word[i])   
        if word[i] in konsonant:
            letter_konsonant = word[i] + "o" + word[i]
            mening.append(letter_konsonant)
        if word[i] == " ":
            mening.append(" ")
    mening = "".join(mening)
    print(mening)

def Svenska(konsonant, vokaler):
    mening = []
    i = 0
    while i < len(word):
        if word[i] == " ":
            mening.append(" ")
            i += 1
        elif word[i] in vokaler:
            letter_vokal = word[i]
            mening.append(letter_vokal)
            i += 1
        elif word[i] in konsonant:
            mening.append(word[i])
            if i + 2 < len(word):
                i += 3
            else:
                i += 1
    mening = "".join(mening)
    print(mening)

def analysering_process(konsonant, vokaler):
    i = 0 
    j = 1
    while i < len(word):
        if word[i] in vokaler or word[i] == " ":
            i += 1
        elif i+2 < len(word) and word[i] in konsonant and word[i + 1] == "o" and word[i] == word[i + 2]:
            j += 1
            i += 3
        else:
            return Rövar(konsonant, vokaler)
    return Svenska(konsonant, vokaler)

analysering_process(konsonant, vokaler)
