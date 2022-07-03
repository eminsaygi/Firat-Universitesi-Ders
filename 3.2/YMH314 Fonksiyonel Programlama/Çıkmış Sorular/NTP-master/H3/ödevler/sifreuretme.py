# -*- coding: utf-8 -*-
"""
100 adet 8 karakterden oluşan en az bir küçük, büyük harf, rakam ve belirlenen özel karakterleri
içeren string şifre üretir
"""

import random

#Küçük/Büyük harfler, rakam ve özel karakter dizileri
s_lowers="abcdefghijklmnopqrstuvwxyz"
s_uppers="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s_digits="0123456789"
s_specials="%?*#!"

liste=[]
for i in range(100):
    x=""
    x+=random.choice(s_lowers)
    x+=random.choice(s_uppers)
    x+=random.choice(s_digits)
    x+=random.choice(s_specials)
    #Birer adet büyük harf,küçük harf, rakam ve özel karakter birer tane ürettik
    #Geriye kalan 4 tanesini rastgele seçecek
    for a in range(4):
        x+=random.choice(s_lowers+s_uppers+s_digits+s_specials)
    #Oluşturulan 8 karakterli şifreyi tekrar karıştırdık ve listeye ekledik
    x=''.join(random.sample(x,8))
    liste.append(x)

print liste

