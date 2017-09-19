lijst = [4, 5, 3, -89]
def kwadraten_som(grondgetallen):
    for i in grondgetallen:
        if i < 0:
            grondgetallen.remove(i)
    grondgetallen = [i *2 for i in grondgetallen]
    return sum(grondgetallen)
print(kwadraten_som(lijst))