hoeveel = input("Hoeveel spelers zijn er? ")

print("Het aantal gekozen spelers:")
print(hoeveel)

lijst=[]
while True:
    naam = input("Wat is je naam? ") 
    lijst.append(naam) 
    if lijst == hoeveel:
        continue
    else:
        
    print("De ingevulde namen zijn:")
    print(naam)
    break


#nog niet af
