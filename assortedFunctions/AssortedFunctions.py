# 1.1
def teken_boom(teken='', grootte=0):
    'functie die een "boom" tekent van ingegeven teken met ingegeven grootte'
    try:
        tekening = ''
        eind = len(teken)
        # loop om de boom van 1 naar ingegeven grootte te printen
        for deel in range(1, grootte+1):
            tekening += teken
            print(tekening)

        # vervolg loop om de boom van ingegeven grootte terug naar 1 te printen
        for deel in range(grootte,1,-1):
            #de lengte van teken wordt verwijderd, ook een boom
            # van meerdere tekens is mogelijk hierdoor
            tekening = tekening[:-eind] 
            print(tekening)
    except:
        print('het teken moet een string zijn, en de grootte een nummer')

# 1.2
def raden_maar(top=10):
    'functie met een raad-spelletje van getallen tussen 1 en ingegeven getal'
    # import van random
    import random
    try:
        # we genereren een random getal
        getal = random.randint(1, top)
        # loop die checkt of het getal geraden is
        while True:
            try: # check of er een getal wordt ingegeven
                raden = int(input('kies een getal tussen 1 en {keuze}\n'\
                              .format(keuze=top)))
                if (raden > top or raden < 1): # check op juiste parameters
                    continue 
                elif (raden < getal):
                    print('Hoger!')
                elif (raden > getal):
                    print('Lager!')
                elif (raden==getal):
                    print('Goed!')
                    break # we stoppen met raden als het juiste getal geraden is.
            except:
                print('je moet wel een getal ingeven!')
    except:
        print('ook de functie moet aangeroepen worden met een nummer')

# 1.3a
def verwijder_dubbel_1(a_list):
    '''functie verwijdert dubbele getallen door er een set van te maken
    die terug wordt gezet in een gesorteerde lijst'''
    try:
        nw_list = sorted(list(set(a_list)))       
        print(nw_list)
    except:
        print('heb je de functie aangeroepen met een lijst van nummers?')

# 1.3b
def verwijder_dubbel_2(any_list):
    '''functie verwijdert dubbelen door door de lijst te loopen en
    elk 'eerste' item aan een nieuwe lijst toe te voegen'''
    try:
        nw_list = []
        for item in any_list:
            if item not in nw_list:
                nw_list.append(item)       
        print(nw_list)
    except:
        print('heb je de functie aangeroepen met een lijst?')

#1.4
def flatten_list(a_nested_list):
    '''functie om een geneste lijst uitgepakt in een nw lijst te zetten
    en printen'''
    if type(a_nested_list) is not list:
        print('heb je de functie wel met een lijst aangeroepen?')
    else:
        def lijst_uitpakker(a_nested_list):
            '''een generator functie die de geneste lijst uitpakt in losse 
            elementen en deze elementen yield naar de bovenliggende functie'''
            # loop door de elementen in de ingegeven lijst
            for item in a_nested_list:
                if (type(item) is list):
                    # als het element een lijst is dan loopen we er net
                    # zolang door tot het geen lijst meer is
                    yield from lijst_uitpakker(item)
                else:
                    yield item
        # bovenliggende functie eromheen geschreven om platte lijst te maken
        nw_list = list(lijst_uitpakker(a_nested_list))
        # en deze te printen    
        print(nw_list)

#1.5
def flatten_iterable(iterable):
    '''functie om een geneste iterable uitgepakt in eenzelfde iterable te
    zetten en printen'''
    if type(iterable) not in [list,set, tuple]:
        print('heb je de functie wel aangeroepen met een lijst, tuple of set?')
    else:
        def uitpakker(iterable):
            '''een generator functie die de geneste iterable uitpakt in losse
            elementen en deze elementen yield naar de bovenliggende functie'''
            #loop door de elementen in de ingegeven iterable
            for item in iterable:
                if (type(item) in [list, set, tuple]):
                    #als het element een iterable is dan 'loopen' we er doorheen
                    # tot het geen iterable meer is
                    yield from uitpakker(item)
                else:
                    yield item
        if (type(iterable) is list):
            #als de ingegeven iterable een lijst is maken we een lijst
            nw_iterable = list(uitpakker(iterable))
        elif (type(iterable) is tuple):
            # idem voor als de iterable een tuple is
            nw_iterable = tuple(uitpakker(iterable))
        else:
            # idem voor als de iterable een set is
            nw_iterable = set(uitpakker(iterable))
        # en tot slot printen we de platgeslagen iterable
        print(nw_iterable)



