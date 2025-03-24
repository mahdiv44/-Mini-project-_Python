import random
import string
str_lower = string.ascii_lowercase
str_upper= string.ascii_uppercase
number="0123456789"
symble="~!@#$%^&*+-_ <>?(){[]}"
all= number + symble + str_upper +  str_lower
a=list()

while True: 
  print("\t \t \n             welcome to password generetor           ".upper())

  print (""" 1. Creat Password
  2. Exit \n""" )
  print(" ")
  x=int(input("  enter your choice  : "))
  if x==1 : 

   length= int (input(" enter your length password : "))
  
   password="".join((random.sample(all,length)))
   print("password is : ",password)

  elif x==2: 
   break 
   
  else : 

   print("Wrong !")