leeftijd = int(input('LEEFTIJD: '))
paspoord = input('INBEZIT VAN PASPOORT (ja/nee): ')
if leeftijd >= 18 and paspoord == 'ja':
    print('JE MAG STEMMEN!')
else:
    print('JE MAG NIET STEMMEN')