'''
Marten Laane
01.11.22
Ül 7
'''
'''
def tevita(a="tundamtu", keel="ge"):
    if keel=="et":
        print(f"tere {a}")
    elif keel=="ge":
        print(f"Guten tag {a}")
    
tevita()

'''
import math

def kuup(a):
    print(f"kuubi ruumala on {a**3}")
def kera(r):
    print(f"kuubi ruumala on {round(4*math.pi*((r/2)**2))}")
def koonus(u, i):
    print(f"kuubi ruumala on {round(0.3*math.pi*(u**2)*i)}")
def silinder(b, s):
    print(f"kuubi ruumala on {a**3}")

loop = 1
while loop == 1:
        print("---------------leiam ruumala---------------")
        valik=int(input("1. kuup/2. kera/3. koonus/4. silinder/5. valjam ine"))
        if valik == 1:
            a=int(input("vali yks kuubi kylg2"))
            kuup(a)
        elif valik == 2:
            r=int(input("vali kera diameeter"))
            kera(r)
        elif valik == 3:
            u=int(input("ytle koonuse raadius "))
            i=int(input("ytle koonuse kõrgus "))
            koonus(u, i)
        elif valik == 4:
            silinder()
        elif valik==5:
            loop = 0
        else:
            print("sellist valikut pole")
        
 