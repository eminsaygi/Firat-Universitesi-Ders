#!/usr/bin/python

# Function definition is here
def changelist( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# call changelist function
mylist = [10,20,30];
changelist( mylist );