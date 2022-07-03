def benzer_cikar(liste):
    output = []
    seen = set()
    for liste in liste:
        if liste not in seen:
            output.append(liste)
            seen.add(liste)
    return output
liste = [2, 78, 98, 34, 5, 2, 560, 78, 43, 5]
sonuc = benzer_cikar(liste)
print(sonuc)