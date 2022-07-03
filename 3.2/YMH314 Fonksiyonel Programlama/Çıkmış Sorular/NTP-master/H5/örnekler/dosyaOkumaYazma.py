demoText1 = "Checking writing"
demoText2 = "Functionality of pyhton"
 
a = open("test1.txt","w")
a.write(demoText1)
a.write("\n")
a.write("csscscsc")
a.close() #file handler must be closed manually
print "File created"
 
a = open("test1.txt","r")
oku = a.read()
a.close() #file handler must be closed manually
print "Printing result of file : "
print oku
print "-----------------------------------------"
 
#using with is safer because file handler is closed automatically
with open("test1.txt","r") as a:
    oku = a.read()
print "Printing result of file opened as with : "
print oku
print "-----------------------------------------"
