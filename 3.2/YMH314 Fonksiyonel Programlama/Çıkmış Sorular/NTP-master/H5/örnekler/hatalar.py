liste = ["elma", "armut", "karpuz", "kavun", "erik", "üzüm", "þeftali", "muz"]
while True:
    try:
       s = raw_input("Lütfen bir meyve adý söyleyiniz: ")
       p = liste.index(s) + 1
       print s, "listemizde", p, "no'lu sýrada bulunuyor"
    except ValueError:
       pass
