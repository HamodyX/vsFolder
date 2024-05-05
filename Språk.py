konsonant = [ 'b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vokaler = ['a', 'e', 'i', 'o', 'u', 'y', 'å','ä','ö']

print("1. Från Rövar till Svenska")
print("2. Från Svenska till Rövar")
print("3. Språk Analysering")

Option = int(input("Välj Alternativ: "))


def Rövar(konsonant, vokaler):
    mening = []
    word = str(input("Svenska Ordet: "))
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
    word = str(input("Rövar order: "))
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
    word = str(input("Checka: "))
    while i < len(word)-2:
        print("check")
        if word[i] in vokaler:
            print(word[i])
            i += 1
        elif word[i] == " ":
            i += 1
        elif word[i] in konsonant and word[i + 1] == "o" and word[i] == word[i + 2]:
            print(f"Rövarspråk detected, NANI! {j * 10}%")
            j += 1
            i += 3
        else:
            return print("Analysis complete -Failed To meet requirements")
    return print("Rövar språk 100%")



if Option == 1:
    Svenska(konsonant, vokaler)
elif Option == 2:
    Rövar(konsonant, vokaler)
elif Option == 3:
    analysering_process(konsonant, vokaler)
else:
    print("Wrong option")