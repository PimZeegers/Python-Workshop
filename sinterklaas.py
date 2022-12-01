lijst=[]

while True:                                                             #-- Zorgt voor een loop, dat het script blijft vragen naar een invoer van de cadeautjes
        
        cadeautjes = input("Wat wil je graag hebben voor sinterklaas, vul klaar in als je klaar bent. ") #vraagt d.m.v een input wat je graag wil hebben voor sinterklaas en slaat dit op in de variable "cadeautjes"
        if cadeautjes == "klaar":                                       #-- Als de gebruiker klaar invoert in de variable "cadeautjes" invoert, ga dan door
                lijst.sort()                                            #-- Sorteer de lijst op alfabetische volgorde
                print("Je hebt de volgende Cadeautjes gekozen:")        #-- Laat zien op het scherm wat tussen de haakjes staat
                print(lijst)                                            #-- Toon de lijst op het scherm
                break                                                   #-- Eindig de loop
        lijst.append(cadeautjes)                                        #-- zorgt ervoor dat alles uit de variable cadeautjes in de variable lijst wordt toegevoegd  


