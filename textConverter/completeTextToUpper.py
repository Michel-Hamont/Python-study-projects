def convert_to_upper(filename_in, filename_out):
    '''een functie om tekstbestanden om te zetten naar allemaal hoofdletters'''
    # met 'open' halen we per 'stukje' de tekst op en schrijven deze per
    # 'beetje' weg naar de variabele 'tekst'
    with open(filename_in, 'rt') as fin:
        tekst = ''
        stukje = 1000
        while True:
            beetje = fin.read(stukje)
            if not beetje:
                break
            tekst += beetje
    # de ingelezen tekst wordt geconverteerd:
    capitalized = tekst.upper()
    # en weer weggeschreven
    with open(filename_out, 'wt') as fout:
        fout.write(capitalized)

# aanroep van de functie om het HOOFDLETTERS bestand te maken
convert_to_upper('loremipsum.txt', 'HOOFDLETTERS.TXT')

        
