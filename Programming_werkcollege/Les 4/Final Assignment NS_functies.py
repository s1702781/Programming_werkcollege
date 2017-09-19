def standaardtarief(afstandKM):
    if int(afstandKM) <  0:
        return 0.0
    elif int(afstandKM) < 50:
        return afstandKM * 0.80
    else:
        return (afstandKM * 60) + 15
def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd > 65:
        return standaardtarief(afstandKM) * 0.70
    elif leeftijd < 12 or leeftijd > 65 and weekendrit == True:
        return standaardtarief(afstandKM) * 0.65
    else:
        if weekendrit == True:
            return standaardtarief(afstandKM) * 0.60
        else:
            return standaardtarief(afstandKM)
print(ritprijs(8,True, 2))
print(ritprijs(11,True, 2))
print(ritprijs(12,True, 2))
print(ritprijs(68,True, 2))
print(ritprijs(8,False, 2))
print(ritprijs(11,False, 2))
print(ritprijs(12,False, 2))
print(ritprijs(68,False, 2))
print(ritprijs(8,True, 15))
print(ritprijs(11,True, 15))
print(ritprijs(12,True, 15))
print(ritprijs(68,True, 15))
print(ritprijs(8,False, 15))
print(ritprijs(11,False, 15))
print(ritprijs(12,False, 15))
print(ritprijs(68,False, 15))