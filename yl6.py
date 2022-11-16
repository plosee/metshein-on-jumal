'''
Marten Laane
11.10.22
Ül 6
'''

facebook = open('C:\pytontexzt1.txt', 'r')

reform=0
kesikuid=0
er=[]

failisisu = facebook.readlines()
for i in failisisu:
    e, p, ee, n = i.split(" ")
    print(e, p, ee, n)
    if ee=="RE":
        reform+=1
    elif ee=="KE":
        kesikuid+=1
    if ee not in er:
        er.append(ee)
    with open("ns.txt", "a") as poliitik:
        poliitik.write(e+" "+p+"\n")
    
        
print(reform)
print(kesikuid)
print(len(er))




    
    



