# maak hier de hele enigma machine in python :D

alphabet = "abcdefghijklmnopqrstuvwxyz"
# functie rotor
def draaiRotor(rotor,aantaldraaien): 
  rotorEind = rotor[26 - aantaldraaien:26]
  rotorBegin = rotor[0:26 - aantaldraaien]
  return rotorEind + rotorBegin 
  
# beginstand rotoren
rotorA = draaiRotor(alphabet, 0)
print (rotorA)

# rotorB = draaiRotor(alphabet, 2)
# print (rotorB)

# rotorC = draaiRotor(alphabet, 3)
# print (rotorC)

# draaien rotoren 
rotorA = draaiRotor(rotorA, 1)
print(rotorA)

# woord vervangen/husselen/door rotor A heen
nieuwwoord = ""
for letter in "aap":
  rotorA = draaiRotor(rotorA, 1)

  if not letter in alphabet: 
    nieuwwoord += letter 
    continue

  positie = alphabet.index(letter)
  nieuwLetter = rotorA[positie]
  
 # positie = alphabet.index(letter)
 # nieuwLetter = rotorB[positie]
  
  # positie = alphabet.index(letter)
  # nieuwLetter = rotorC[positie]
  
  nieuwwoord += nieuwLetter

print(nieuwwoord)