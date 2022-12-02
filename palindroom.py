woord = input("Vul het woord in: ")                       #-- Een input die de gebruiker vraagt om een woord in te vullen, die het script vervolgens plaatst in de variable "woord"
if woord == woord[::-1]:                                  #-- :: selecteerd het hele woord en -1 betekent dat hij achteraan de string begint
    print ("Het ingevulde woord is een palindroom!")      #-- Als het originele woord, omgedraait nog steeds hetzelfde is als het origineel dan is het een palindroom.
else:                                                     #-- Als het bovenstaande niet het geval is, dus als het omgedraaide woord anders is dan het orgineel dan is het geen palindroom.
    print("Het ingevulde woord is helaas geen palindroom")#-- Toon dat het geen palindroom is, als het " else " statement waar is.


        # IS AF
#Punten voor gekregen