#!/usr/bin/env python
#-*- coding: iso-8859-9

#metotları lıstele
dosya = open("falanca_dosya.txt", "w")
for metot in dir(dosya):
   if not metot.startswith("_"):
      print(metot)
print dosya.name
dosya.close()


#ikili dosyalar
f = open("123.docx", "wb")
f.write("vöskdmvskmvksm")
f.close()


f = open("123.docx", 'rb')
data = f.read(10)
if data[6:11] in [b"JFIF", b"Exif"]:
     print("Bu dosya JPEG!")
else:
     print("Bu dosya JPEG değil!")
