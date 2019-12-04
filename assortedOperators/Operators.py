#2.1
def schakel(bool1, bool2):
    '''functie die een boolean teruggeeft op vergelijking 2 booleans'''
    if bool1 and bool2 or not bool1 and not bool2:
        return True
    else:
        return False

#2.2
def mediaan(num_list):
    'functie sorteert ingegeven numerieke lijst, en print de mediaan'
    try:
        # we sorteren de lijst
        num_list.sort()
        # we bekijken de lengte van de lijst
        lengte = len(num_list)
        # als er bij delen door 2 geen rest is dan nemen we het
        # gemiddelde van de middelste 2 getallen
        if lengte%2 == 0:
            mediaan = (num_list[int((lengte/2)-1)]+num_list[int(lengte/2)])/2
            print(mediaan)
        
        else: # als er wel een rest is kunnen we het middelste getal nemen
            mediaan = num_list[int(lengte/2)]
            print(mediaan)
    except:
        print('Heb je wel een lijst met nummers ingegeven?')
        
#2.3
def puzzel(koppen=0, poten=0):
    try:
        # als er een oneven aantal poten is, dan is er geen oplossing
        if poten%2 != 0:
            print('geen oplossing')
        else:
            # er zijn ten minste (koppen*2) kalkoenen(poten), uit het restant
            # halen we de konijnen
            restant = poten-(koppen*2)
            konijnen = int(restant/2)
            kalkoenen = koppen -konijnen
            dieren = {'konijnen': konijnen, 'kalkoenen': kalkoenen}
            print(dieren)
    except:
        print('heb je het aantal koppen en poten wel in nummers ingegeven?')
        
#2.4
def palindroom(text):
    '''functie checkt of een tekst een palindroom is door te strippen en
    om te draaien'''
    # Variabele met alle speciale tekens (+ spatie)
    tekens = '''!@#$%€^&*();:'"\,.<>/?_-[]{}~` '''
    try:
        # Hoofdletters worden omgezet in kleine letters
        text2 = text.lower()
        # Als alternatief gedacht aan (import)re.sub 
        # maar voor oplossing zonder import gekozen.
        # Als er een speciaal teken voorkomt dan halen we deze weg
        for teken in text2:
            if teken in tekens:
                text2 = text2.replace(teken,'')
        # als de omgedraaide tekst gelijk is, dan is het een palindroom
        if text2 == text2[::-1]:
            print('Het is een palindroom!')
        else:
            print('Jammer, helaas geen palindroom')
    except:
        print('je kunt alleen een tekst als string ingeven hier')
    
#2.5
def binary_search(ascending_integer_list, search_for):
    '''functie checkt of een getal in een lijst voorkomt, door de lijst
    in 2-en te splitsen en telkens het middelste getal te controleren'''
    try:
        lijst = ascending_integer_list
        if search_for not in lijst:
            # als het getal niet in de lijst voorkomt dan gaan we niet verder
            return False
        else:
            while True:
                lengte = len(lijst)
                middelste = lijst[int(lengte/2)]
                if middelste > search_for:
                    # als het getal in de bovenste helft zit, gebruiken we de
                    # de bovenste helft van de lijst als nieuwe lijst
                    lijst = lijst[:int(lengte/2)]
                elif middelste < search_for:
                    # idem maar dan met de onderste helft
                    lijst = lijst[int(lengte/2):]
                elif middelste == search_for:
                    # gevonden en dus gaan we uit de loop
                    return ascending_integer_list.index(search_for)
                    break
    except:
        print('heb je een lijst met getallen, en een getal ingegeven?')

# heb de test van 2.5 laten staan achter ##
##from random import randint
##rlist= sorted ([randint(0,999999) for i in range(999999)])
##print(binary_search(rlist, 15))



    
