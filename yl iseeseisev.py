'''
aidakemind
ma olen keldris kinni
ma ei suuda
'''
'''
#banner
kroda = int(input("mitu korda sa reklaami tahad: "))
reklam = input("mida sa reklaamiks tahad?: ")

for i in range(kroda): 
            print(reklam.upper()) 
'''
'''
#õunamahl
ounaarv = int(input("mitu ouna sul om bbg: "))
mahla_arv = ounaarv*0.4/3
print(mahla_arv)
'''
'''
#peoarve
kutsutud = int(input("mitu inimest kutsuti?: "))
tuleb = int(input("mitu inimest tegelt tulewb?: "))
eelarve = kutsutud*10+55
mineelarve = tuleb*10+55
print(f"{mineelarve} on minimaalne eelarve")
print(f"{eelarve} on maksimaalne eelarve")

'''
#tevirtused
'''
tervitus = int(input("mitu tervitus? "))


def terv2(x):
    for i in range(x):
        print(f"Võõrustaja: 'Tere!' \n Täna {i+1}. kord tervitada, mõtiskleb võõrustaja \n  Külaline: 'Tere, suur tänu kutse eest!'")
        
terv2(tervitus)
'''
#mündid
'''
listii=input("sisesta failinimi: ")
fail = open(listii)
list2 = []
for i in fail:
    list2.append(int(i))
print(list2)


def listi(x):
    summa = 0
    for i in x:
        if i  <= 5:
            summa += i
    print(summa)
listi(list2)
'''
#kuupäev'
'''
def kuu_nimi(o):
    kuud = ["", "jan", "veb", "marts", "april", "mai", "juuni", "juuli", "aug", "sept", "okt", "nov", "dets"]
    return kuud[o]

def kuupaev(p,l,a):
    print(f"{p}. {l}. {a}. a")

lilput = input("pane siia kuupaev asi DD.MM.YYYY: ")
p,k,a = lilput.split(".")

kuupaev(p,kuu_nimi(int(k)),a)
'''


    

    
    

    

            
        





    



