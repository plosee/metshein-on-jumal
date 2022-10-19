'''
Marten Laane
11.10.22
Ül 4 while
'''
import random
#while
'''
#tärnid
j=5

for i in range(5):
    print("*"*j)
    j-=1
    
for i in range(5):
    print("*"*j)
    j+=1

for i in range(5):
    print("* "* 5)

#loto
    
for i in range(0,5):
    print(random.randint(1, 10) ,end="")

#paaris ja paaritu
    
for i in range (0,10):
    if i%2==0:
        print(f"{i} paaris")
    else:
        print(f"{i} paaritu")
        
#korrutustabel

for i in range(11):
    print(5*i)

#arvasmismang
loop=1
while loop==1:
    arv=random.randint(1,3)
    for i in range(3):
        pakkumine=int(input("arva arv tighkahiib:"))
        if pakkumine == arv:
            print("tubli too")
            break
        else:
            print("ei ole")
    loop=int(input("jatka y/n: "))


#pank

konto=10000
intress=0.05

for i in range(5):
    print(konto, konto*intress+konto)
    konto=round(konto+konto*intress)
  '''  
#ruutude rabel

print("arv ruut kuup")
for i in range(1,10):
    print(f"{i}     {i**2}     {i**3}") 

