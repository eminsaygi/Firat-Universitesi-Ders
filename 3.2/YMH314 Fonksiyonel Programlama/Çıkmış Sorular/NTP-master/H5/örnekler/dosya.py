#!/usr/bin/env python
#-*- coding: iso-8859-9
dosya = open("şiir.txt", "w")
dosya.write("Bütün güneşler batmadan,\nBi türkü daha söyleyeyim bu yerde\n\t\t\t\t --Orhan Veli--")
dosya.close()

with open("şiir.txt", "r") as dosya:
 a=dosya.read()
 print a

 #dosyayı basa sarma
 dosya.seek(0)
 b=dosya.read()
 print b
 
#dosyanın basına verı ekleme
with open("şiir.txt", "r+") as f:
    veri = f.read()
    f.seek(0)
    f.write("Selin Özden\t: 0212 222 22 22\n"+veri)

 
#ortaya veya herhangı bır yere ekleme
with open("şiir.txt", "r+") as f:
     veri = f.readlines()
     veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
     f.seek(0)
     f.writelines(veri)


