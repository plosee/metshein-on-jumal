import random

it22 = open("it22.txt.txt", encoding = "UTF-8")
failisisu = it22.readlines()

def emailid(l):      
    for i in l:
        i = i.lower()
        i = i.replace("ö", "")
        i = i.replace("ä", "")
        i = i.replace("õ", "")
        i = i.replace("ü", "")
        i= i.replace ("\n", "")
        em = i.split(" ")
        print(f"{i[0]}{em[1]}@gmail.com")
emailid(failisisu)

def emailid2(l):
    for i in l:
        i = i.lower()
        i = i.replace("ö", "o")
        i = i.replace("ä", "a")
        i = i.replace("õ", "o")
        i = i.replace("ü", "u")
        i= i.replace ("\n", "")
        em = i.split(" ")
        print(f"{em[0]}.{em[1]}@gmail.com")
emailid2(failisisu)

def paroolmunad(l):      
    for i in l:
        i = i.lower()
        i = i.replace ("\n", "")
        print(f"{i[0]}{random.randint(10,999)}")
paroolmunad(failisisu)
        
    


        
        
    

