# maak hier de hele enigma machine in python :D

alfabet = "abcdefghijklmnopqrstuvwxyz"

class Enigma:
  a = 0
  b = 0
  c = 0
  
 # maakt de classvariabelen aan voor aanroepen
  def __init__(self, a,b,c) :
    self.a = a
    self.b = b
    self.c = c

  # schuif letters op voor het gegeven aantal (encrypten)
  def schuiven(self, aantal_verschuivingen):    
    aantal_verschuivingen = aantal_verschuivingen % 26 
    verschuifd_alfabet = list(alfabet)
    for i in range(aantal_verschuivingen):
      verschuifd_alfabet.insert(0, verschuifd_alfabet[-1])
      verschuifd_alfabet.pop(-1)
    return verschuifd_alfabet

  # schuif de letters terug voor het gegeven aantal (decrypten)
  def schuiven_omkeren(self, aantal_verschuivingen):
    verschuifd_alfabet = list(alfabet)
    for i in range(aantal_verschuivingen):
        verschuifd_alfabet.append(verschuifd_alfabet[0])
        verschuifd_alfabet.pop(0)
    return verschuifd_alfabet

   # zet de letters naar voor en verandert de positie van de aangegeven letter (encrypten)
  def volgende_letter(self, rotor, char) :
    verschuifd_alfabet = self.schuiven(rotor)
    letterIndex = alfabet.index(char)
    return verschuifd_alfabet[letterIndex] 

  # zet de letters naar achter en verandert de positie van de aangegeven letter (decrypten)
  def vorige_letter(self, rotor, char) :
    verschuifd_alfabet = self.schuiven_omkeren(rotor)
    letterIndex = alfabet.index(char)
    return verschuifd_alfabet[letterIndex]
     
  # rotors b en c gaan draaien op het juiste moment
  def rotors_draaien(self, positie) :
    self.a = self.a + 1

    if(positie % 26 == 0):
      self.b = self.b + 1

    if(positie % (26*26)==0):     
      self.c = self.c + 1

  # de instellingen voor de in te voeren tekst
  def versleutelen(self, tekst) :
    tekst = tekst.lower()      
    nieuwe_tekst = []
    positie = 0

  # andere tekens dan letters mogelijk maken
    for char in list(tekst) :
      if not char in alfabet :
        nieuwe_tekst.append(char)
        continue
        
  # door de rotoren heen
      nieuwe_letter = self.volgende_letter(self.a, char)

      nieuwe_letter = self.volgende_letter(self.b, nieuwe_letter)  

      nieuwe_letter = self.volgende_letter(self.c, nieuwe_letter)  
       
  # alfabet omkeren
      omgekeerde_alfabet = [letter for letter in reversed(alfabet)]
      
  # en weer terug door de rotoren, maar nu de andere kant op
      nieuwe_letter = omgekeerde_alfabet[alfabet.index(nieuwe_letter)]

      nieuwe_letter = self.vorige_letter(self.c, nieuwe_letter)

      nieuwe_letter = self.vorige_letter(self.b, nieuwe_letter)

      nieuwe_letter = self.vorige_letter(self.a, nieuwe_letter)

  # uiteindelijk komt er uit de rotoren een nieuwe letter 
      nieuwe_tekst.append(nieuwe_letter)
      
      self.rotors_draaien(positie)
      positie = positie + 1

    return str.join("",nieuwe_tekst)

  # code en rotorstanden invoeren
print("Wat wil ontcijferen of versleutelen?")
invoertekst = input()

a = int(input("Rotorstand 1: "))
b = int(input("Rotorstand 2: "))
c = int(input("Rotorstand 3: "))

e = Enigma(a, b, c)
versleuteld = e.versleutelen(invoertekst)

print("Ontcijferd/Versleuteld:")
print(versleuteld)
