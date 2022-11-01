'''
Marten Laane
01.11.22
Ül 9
'''
import datetime
import locale



tana = datetime.date.today()
print(tana.strftime("%d. %B %Y"))
locale.setlocale(locale.LC_ALL, "et_EE")
print(tana.strftime("%d. %B %Y"))

ik="50605306516"
sp=datetime.date(int("20"+ik[1:3]),int(ik[3:5]),int(ik[5:7]))
print(sp)

age=tana.year - int("20"+ik[1:3])
print(age)

