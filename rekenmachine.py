print("selecteer wat je wil uitrekenen")


def add(x, y):
  return x + y

def subtract(x, y):
 return x - y

def multiply(x, y):
 return x * y


def divide(x, y):
 return x / y


print("1.Plus")
print("2.Keer")
print("3.Delen")
print("4.Min")
kies = input("kies uit: (1/2/3/4): ")

while True:
  try:
    num1 = float(input("Voer hier het eerste getal in: "))
    num2 = float(input("Voer hier het tweede getal in: "))
    break
  except:
    print("Vul alleen nummers in, geen letters!")
    

if kies == '1':
 print(num1, "+", num2, "=", add(num1, num2))

if kies == '2':
  print(num1, "*", num2, "=", multiply(num1, num2))

if kies == '3':
  print(num1, "/", num2, "=", divide(num1, num2))

if kies == '4':
  print(num1, "-", num2, "=", subtract(num1, num2))


#werkt wel, nog niet helemaal compleet.
#Volgorde klopt niet 