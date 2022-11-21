odavisetekst = open("oda_uus.txt")
fh = odavisetekst.readlines()

def odad(fh):
	listi = []
	nimed = []
	for i in fh:
		i = i.replace("\n", "")
		maks = max(i.split(" ")[-3:])
		listi.append(maks)
		nimed.append(i.split(" ")[:2])
		neer = i.split(" ")
		print(f"{neer[0], neer[1]}. Nende suurim vise: {maks}")	
	maksi = max(listi)
	asd = listi.index(maksi)
	print(f"voitja on {nimed[asd]} ja ta viskas {listi[asd]}")
	
odad(fh)
