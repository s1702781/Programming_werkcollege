cijferICOR = 6
cijferPROG = 7
cijferCSN = 6.5
gemiddelde = (cijferCSN + cijferICOR + cijferPROG) / 3
beloning = (cijferCSN * 30) + (cijferICOR * 30) + (cijferPROG * 30)
overzicht = 'Mijn gemiddelde cijfer is een ' + str(gemiddelde) + ' en mijn beloning is ' + str(beloning) + ' euro'
print(overzicht)