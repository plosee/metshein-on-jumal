'''
Marten Laane
11.10.22
Ül 2
'''
import math

#ümbermõõt
a = 1
b = 2
c = 3
P = a+b+c
print(P)

#toode
toode = 36.75
soodus = toode*0.6
print(soodus*3, "€")

#pitsa
pitsa = 12.9
joot = pitsa*1.1
print(joot/3, "€")

#rulluisk
kiirus = 29.9
aeg = round(kiirus/1.5)
print(aeg)

#hüpotenuus
d=16
f=9
c2=round(math.sqrt(pow(d,2)+pow(f,2)),2)
print(c2)

#ajateisendus
ajaja=int(input("siia laheb aeg minutites: "))
ajamees = ajaja//60
ajanaine=ajaja%60
print("sinu vastus on:", ajamees,":" ,ajanaine)

#arvusüsteemid
arv = int(input("aseta see arv siia:"))
print(hex(arv), bin(arv))

#kütusekulu
liiter = int(input("aseta enda liitri arv siia; "))
km = int(input("aseta siia siis enda kilometraaz vms: "))
kokku=liiter/(100/km)
print=(kokku)
           
