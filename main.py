from random import randint
schenker = []
empfaenger = []
gruppennummer_schenker = []
gruppennummer_empfaenger = []
z = 0
auflisten_namen = True
auflisten_gruppen = True

while(auflisten_namen):
    name = input("Gib die Namen der Teilnehmer an. Oder einfach Enter, wenn du fertig bist")
    if(name == ""):
        auflisten_namen = False
    else:
        schenker.append(name)
        empfaenger.append(name)

while(z < len(schenker)):
    print(schenker)
    print(gruppennummer_schenker)
    gruppe = input("Gib die Gruppen der Personen an. Gruppe 0 hat keine Restriktionen")
    print(gruppennummer_schenker)
    gruppennummer_schenker.append(gruppe)
    gruppennummer_empfaenger.append(gruppe)
    z += 1

print(gruppennummer_schenker)

while (len(schenker)>0):
    z1 = randint(0,len(schenker)) - 1
    z2 = randint(0,len(schenker)) - 1
    if(gruppennummer_schenker[z1] != gruppennummer_empfaenger[z2] or gruppennummer_schenker[z1] == "0" and schenker[z1] != empfaenger[z2]):
        print(schenker[z1] + " schenkt " + empfaenger[z2] + " etwas")
        del schenker[z1]
        del empfaenger[z2]
        del gruppennummer_schenker[z1]
        del gruppennummer_empfaenger[z2]

