# cycling.py
"""Klassen-hiërarchie 'onderste tak' van (wieler)wedstrijd"""             
# import van datetime om deze te kunnen gebruiken voor string format
# van datum en tijd
import datetime

class Wedstrijd(object):
    
    def __init__(self, plaats, datum, vertrekpunt, vertrektijd, deelnemers = None):
        # om te voorkomen dat er slechts eenmaal een lege lijst gemaakt 
        # kan worden, stellen we deelnemers standaard in op None
        if deelnemers is None:
            deelnemers = []
        self.plaats = plaats
        # gebruik van datetime strptime om iso-standaard te 'forceren'
        gebruikte_datum = datetime.datetime.strptime(datum, '%Y-%m-%d')
        self.datum = gebruikte_datum.date()
        self.vertrekpunt = vertrekpunt
        gebruikte_tijd = datetime.datetime.strptime(vertrektijd, '%H:%M')
        self.vertrektijd = gebruikte_tijd.time()
        self.deelnemers = deelnemers
    # method om deelnemers toe te voegen aan de lege lijst
    def inschrijving(self, deelnemers):
        self.deelnemers.append(deelnemers)
    # method om de uitslag te verwerken
    def uitslag(self, eerste, tweede, derde):
        self.eerste = eerste
        self.tweede = tweede
        self.derde = derde
        self.winnaars = (self.eerste, self.tweede, self.derde)
        # we kijken met een for-loop of een winnaar wel mee heeft gedaan
        # zo niet dan schrijven we 'm weg in een lijst 'test'
        test = []
        for renner in self.winnaars:
            if renner not in self.deelnemers:
                test.append(renner)
        if len(test) > 0:
            for renner in test:
                print ("Niet in de deelnemerslijst: " + renner + "\n")
        else:
            return self.winnaars

    def toon(self):
        for key, value in self.__dict__.items():
            print (key, value)
            
              
            
        

# ...
# Andere klassen (Weg, ..., Baan, ...) bewust weggelaten
# ...

class Cross(Wedstrijd):
    # of: CrossWedstrijd(Wedstrijd)
    pass

class Veldrijden(Cross):
    pass

class ATB(Cross):
    # All-Terrain Bike  / MTB (Mountain bike) 
     pass	


if __name__ == '__main__':
    wedstrijd = ATB('Ardennen', '2019-10-10', 'Spa', '10:15')
    deelnemers_wedstrijd =['Jan Janssen', 'Theo Thijssen', 'Willem Wever',\
                 'Flip Flipjens', 'Marky Mark', 'Bea Bij']
    for deelnemer in deelnemers_wedstrijd:
        wedstrijd.inschrijving(deelnemer)
    wedstrijd.uitslag('Bea Bij', 'Flip Flipjens', 'Theo Thijssen')
    wedstrijd.toon()




                 
