"""
marten laane
13.11.22
iseseisev töö 15.11.22
"""
import math
import random

#defineerime kasutaja ja arvuti täringu nimekirjad, kasutaja raha, mitu korda korrata, ning loop funktsiooni algus
kasutajatäringud = []
arvutitäringud = []
kasutajaraha = 0
täringarv = 2
jrk = 1
loop = 1
attempt = 1

#loopib kuni kasutaja otsustab mitte edasi mängida
while loop == 1:
    #jooksutab allolevat koodi nii mitu korda kui mitu täringut on, praegu 2
    for i in range (täringarv):
        #ranmdom.randint veeretab täringud
        number = random.randint(1,6)
        #allolev rida lisab kasutaja täringu väärtuse nimekirja
        kasutajatäringud.append(number)
        #sama asi mis eelnevalt aga arvuti listi
        anumber = random.randint(1,6)
        arvutitäringud.append(anumber)

    #näitab kasutaja raha koguse
    print(f"Balance: {kasutajaraha}")
    bet = int(input("Paljuga te soovite kihla vedada: "))

    #testib kas kasutaja veeretas kokku suurema väärtusega täringuid
    if sum(kasutajatäringud) > sum(arvutitäringud):
        print("Olete võitnud!")
        #prindib kasutaja ja arvuti täringute summad
        print(f"Kasutaja täringute summa: {sum(kasutajatäringud)}, Arvuti täringute summa: {sum(arvutitäringud)}")
        #lisab kihlveost võidetud raha kasutaja raha summale
        kasutajaraha = (kasutajaraha + bet)
        print(f"Balance: {kasutajaraha}")
        #kasutaja kaotab kihlveo
    elif sum(kasutajatäringud) < sum(arvutitäringud):
        print("Kaotasite!")
        print(f"Kasutaja täringute summa: {sum(kasutajatäringud)}, Arvuti täringute summa: {sum(arvutitäringud)}")
        kasutajaraha = (kasutajaraha - bet)
        print(f"Balance: {kasutajaraha}")
    else:
        #kasutaja jääb viiki 
        print("Viik!")
        print(f"Kasutaja täringute summa: {sum(kasutajatäringud)}, Arvuti täringute summa: {sum(arvutitäringud)}")
        print(f"Balance: {kasutajaraha}")

    #clearib listid et täringute output ei suureneks
    arvutitäringud.clear()
    kasutajatäringud.clear()

    #küsib kasutajalt kas ta soovib jätkata
    cont = input("Soovite jätkata? (jah/ei): ")
    if cont.lower() == "jah":
        loop = 1
        print("Jätkame")
        #lisab +1  roundi numbrile, järgmine rida prindib line breakiga roundi ja selle numbri
        attempt +=1
        print(f"\nRound {attempt}")
    else:
        #katkestab loopi kui kasutaja ei kirjuta jah
        loop = 0
