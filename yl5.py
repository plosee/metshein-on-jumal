'''
Marten Laane
11.10.22
Ül 5
'''
'''
nimed = []
for i in range(5):
    nimi = input("sisteata nimi hompederast:")
    nimed.append(nimi)

print (nimed[-1])
nimed.sort()
print (nimed)
'''
#opilased
'''
j=0
opilased = ["Juhan","kati","mario","maarja","mati"]
for opilane in opilased:
    print(f"{j}. {opilane}")
    j+=1
    
inn = int(input("keda soovid muuta="))
opilased.pop(inn)
inn2=input("keda sa siis tahad?")
opilased.insert(inn, inn2)
print(opilased)
'''
#opilased 2
'''
j=0
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
for opilane in opilased:
    print(f"{j}. {opilane}")
    j+=1

myopilased=set(opilased)
print(myopilased)
'''
#vanus

import random
import statistics
nummer=[random.randint(1, 99), random.randint(1, 99), random.randint(1, 99), random.randint(1, 99)]
print(nummer)
print(max(nummer))
print(min(nummer))
print(sum(nummer))
print(statistics.mean(nummer))

#tärnid
for nummers in nummer:
    print(f"{nummers*'*'}")

