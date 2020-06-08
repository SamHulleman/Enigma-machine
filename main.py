# maak hier de hele enigma machine in python :D

alphabet = "abcdefghijklmnopqrstuvwxyz"
# functie rotor
def draaiRotor(rotor,aantaldraaien): 
  rotorEind = rotor[26 - aantaldraaien:26]
  rotorBegin = rotor[0:26 - aantaldraaien]
  return rotorEind + rotorBegin 
  
# beginstand rotoren
def StandenRotoren():
  for x in range(3):
    print("Stand van rotor {}:".format(x+1))

#rotorA = draaiRotor(alphabet, 26)
#print (rotorA)

#rotorB = draaiRotor(alphabet, 2)
#print (rotorB)

#rotorC = draaiRotor(alphabet, 3)
#print (rotorC)

# woord vervangen/husselen/door rotors heen
def WoordDoorRotoren(InvoerLetter):
  if alfabet.find(InvoerLetter)= -1:
    return Invoerletter
#door de rotoren heen
  for rotorA
    InvoerLetter = alfabet.index(Invoerletter)
  for rotorB
    InvoerLetter = alfabet.index(Invoerletter)
  for rotorC
    InvoerLetter = alfabet.index(Invoerletter)
#alfabet andersom
InvoerLetter = alfabet[::-1][alfabet.index(InvoerLetter)]

#andersom door de rotoren
InvoerLetter = rotorC.index(Invoerletter)
InvoerLetter = rotorB.index(Invoerletter)
InvoerLetter = rotorA.index(Invoerletter)


aantaldraaien = 0 
nieuwwoord = ""
nieuwwoord.lower()
for letter in "aap":
  aantaldraaien += 1
  rotorA = draaiRotor(rotorA, 1)

  if not letter in alphabet: 
    nieuwwoord += letter 
    continue

  positie = alphabet.index(letter)
  nieuwLetter = rotorA[positie]

# als A 26 heeft gedraaid draait B
  if aantaldraaien % 26 == 0:
    rotorA = 0
    rotorB = draaiRotor(rotorB, 1)
    rotorB += 1
    
 # positie = alphabet.index(letter)
 # nieuwLetter = rotorB[positie]
  
  # positie = alphabet.index(letter)
  # nieuwLetter = rotorC[positie]
  
  nieuwwoord += nieuwLetter

print(nieuwwoord)