f=open("odev.txt","r")
veri=dict()
d=f.readlines()

for i in d:
    sube=i.split("=>")[0]
    if not veri.has_key(sube):
        veri[sube]=dict()
        
    yeni=i.split("=>")[1].replace("\n","").strip()

    for k in yeni.split(" "):
        urun,miktar=[k.split(":")[0], k.split(":")[1]]
        if veri[sube].has_key(urun):
            veri[sube][urun]+=int(miktar)
        else:
            veri[sube][str(urun)]=int(miktar)

print veri
#####
kasa=dict()

for  urunler in veri.values():
    for urun,miktar in urunler.items():
        if kasa.has_key(urun):
            kasa[urun] += int(miktar)
        else: 
            kasa[urun] = int(miktar)


print "toplam =>",kasa
