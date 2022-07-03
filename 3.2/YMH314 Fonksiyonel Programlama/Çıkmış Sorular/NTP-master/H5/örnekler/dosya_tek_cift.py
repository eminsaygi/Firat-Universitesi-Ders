a = open("cift.txt","w")
b = open("tek.txt","w")
for i in range(1,100):
     if i % 2 == 0 :
        a.write(str(i))
        a.write(",")

     else :
        b.write(str(i))
        b.write(",")

a.close()
b.close()
