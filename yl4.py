'''
Marten Laane
11.10.22
Ül 4
'''

#vabiribal
a,b =10,20


#jalgpal

sugu = input("pane siia enda sugu n/M:")
if sugu == "mees":
    vanus2 = int(input(" pane siia oma vanus bsm ;; "))
    lubatud = 16,17,18
    if vanus2 in lubatud:
        print(" tubli sa oled sise lubatud")
    else:
        print(" ei saa omonoid")
else:
    print("mine mine kuri naine ei meeldi kooki raisk")
    

#MÜK
hind = int(input("pane siia oma hind bms;"))
if hind <= 10:
           discount = 0.9
elif hind <= 20:
           discount = 0.8
            
           
print (f"lõpphind on {hind*discount}")

#juubel
sp = "5.6.2002"
d,m,y = sp.split(".")
vanus = 2022-int(y)
print(vanus)

if vanus%5 == 0:
    print("JUUBEPEL JUHUU")
else:
    print(" ei ole L RATION")


#matem
tehe = input("Vali tehe (+ - * /): ")
if tehe=="+":
    vastus = a+b
elif tehe =="-":
    vastus = a-BaseException
# ei viitsi rohkem panna lmao
else:
    vastus = "n/a"
print(f"{a}{tehe}{b}={vastus}")

#ruut
if a==b:
    print(f"{a} ja {b} teevad ruudutu")
else:
    print(f"{a} ja {b} ei tee ruutu L")
    