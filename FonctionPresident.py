from Class import JeuDeCartePresident as JDCP
from Class import JoueurPresident as JP
from Class import PaquetDeCarte as PC
import sys

def PremierePartiePresident(J1:str,J2:str,J3:str,J4:str) :
	president = None
	Vice_President = None
	Vice_TDC = None
	TDC=None
	ja = JP(J1)
	jb = JP(J2)
	jc = JP(J3)
	jd = JP(J4)
	Paquet= JDCP()
	Paquet.Melanger()
	Pioche = PC(Paquet.GetJeu())
	ja.Ramasser(Pioche.Distribuer(13))
	jb.Ramasser(Pioche.Distribuer(13))
	jc.Ramasser(Pioche.Distribuer(13))
	jd.Ramasser(Pioche.Distribuer(13))
	while P(ja,jb,jc,jd) == False :
		 ja,jb,jc,jd=TourPresident4j(ja,jb,jc,jd)
	president=QP(ja, jb, jc, jd)
	if president == ja :
		Vice_President,Vice_TDC,TDC = troisj(jb, jc, jd, Vice_President, Vice_TDC, TDC)
	if president == jb :
		Vice_President,Vice_TDC,TDC = troisj(ja, jc, jd, Vice_President, Vice_TDC, TDC)
	if president == jc :
		Vice_President,Vice_TDC,TDC = troisj(ja, jb, jd, Vice_President, Vice_TDC, TDC)
	if president == jd :
		Vice_President,Vice_TDC,TDC = troisj(ja, jb, jc, Vice_President, Vice_TDC, TDC)
	return president,Vice_President,Vice_TDC,TDC
	  
def troisj(j1:JP,j2:JP,j3:JP,VicePresident,ViceTDC,TDC) :
	while VP(j1,j2,j3) == False :
		 j1,j2,j3=TourPresident3j(j1,j2,j3)
	VicePresident=QVP(j1,j2,j3)
	if VicePresident == j1 :
		while VTDC(j2,j3) == False:
			j2,j3 = TourPresident2j(j2, j3)
		ViceTDC,TDC=QVTDC(j2, j3)
	elif VicePresident == j2 :
		 while VTDC(j2,j3) == False:
			 j2,j3 = TourPresident2j(j1, j3)
		 ViceTDC,TDC=QVTDC(j1, j3)
	elif VicePresident == j3 :
		 while VTDC(j1,j2) == False:
			 j2,j3 = TourPresident2j(j1, j2)
		 ViceTDC,TDC=QVTDC(j1, j2)
	return VicePresident,ViceTDC,TDC 	  

def TourPresident4j(J1:JP,J2:JP,J3:JP,J4:JP) :
	Cartes1,m = Poser(J1)
	assert Cartes1 != None ,'Il faut jouer J1'
	nb=Cartes1.GetTaille()
	AfficheCartes(Cartes1, J1)
	Cartes2,m = Poser(J2,m)
	if Cartes2 != None :
		assert Cartes2.GetTaille() == nb , "Fin frérot, tu triche"
	AfficheCartes(Cartes2, J2)
	Cartes3,m = Poser(J3,m)
	if Cartes3 != None :
		assert Cartes3.GetTaille() == nb , "Fin frérot, tu triche"
	AfficheCartes(Cartes3, J3)
	Cartes4,m = Poser(J4,m)
	if Cartes4 != None :
		assert Cartes4.GetTaille() == nb , "Fin frérot, tu triche"
	AfficheCartes(Cartes4, J4)
	if Cartes4 == None :
		if Cartes3 == None :
			if Cartes2 == None :
				return J1,J2,J3,J4
			else :
				return J2,J3,J4,J1
		else :
			return J3,J4,J1,J2
	else :
		return J4,J3,J2,J1

def TourPresident3j(J1:JP,J2:JP,J3:JP) :
	Cartes1,m = Poser(J1)
	nb=Cartes1.GetTaille()
	AfficheCartes(Cartes1, J1)
	Cartes2,m = Poser(J2,m)
	if Cartes2 != None :
		assert Cartes2.GetTaille() == nb , "Fin frérot, tu triche"
	AfficheCartes(Cartes2, J2)
	Cartes3,m = Poser(J3,m)
	if Cartes3 != None :
		assert Cartes3.GetTaille() == nb , "Fin frérot, tu triche"
	AfficheCartes(Cartes3, J3)
	if Cartes3 == None :
		if Cartes2 == None :
			return J1,J2,J3
		else :
			return J2,J3,J1
	else :
		return J3,J2,J1

def TourPresident2j(J1:JP,J2:JP) :
	Cartes1,m = Poser(J1)
	nb=Cartes1.GetTaille()
	AfficheCartes(Cartes1, J1)
	Cartes2,m = Poser(J2,m)
	if Cartes2 != None :
		assert Cartes2.GetTaille() == nb , "Fin frérot, tu triche"
	AfficheCartes(Cartes2, J2)

def AfficheCartes(c,j:JP) :
	if c != None :
		print(' \n')
		print(j.GetNom(),'a joué les cartes suivantes :')
		c.AffichePaquet()
	else :
		print('\n')
		print(j.GetNom(),'a passer son tour, il ne peux jouer')
	
def Poser(J:JP,M=0) :
	print(J.GetNom(),'a toi de jouer !',end='\n\n')
	print('Voici t\'as pioche : ',end='\n\n')
	J.AffichePioche()
	print('')
	print('Que veux tu faire ?')
	print('')
	print('1. Jouer un carré , 2. Jouer un triplé , 3. Jouer un double , 4.Jouer une carte 5.Passer ton tour')
	print('Appuie sur une autre touche pour quitter le programme')
	if M == 15 :
		x='Passe'
	else :
		x = input(">")
	if x == "1" :
		print("Quel est le plus petit l'indice du carré que tu veux jouer ? (ex : tape 8 pour le carré des cartes 8,9,10,11)")
		z= input(">")
		z=int(z)
		assert z<J.GetNbCarteJ()-2 , 'Entrez un nombre Valide (entre 1 et 13)'
		a=J.TirerCarte(z)
		b=J.TirerCarte(z)
		c=J.TirerCarte(z)
		d=J.TirerCarte(z)
		assert a.GetValeur() == b.GetValeur() == c.GetValeur() == d.GetValeur() , 'fin frérot , tu triche'
		assert a.GetValeur() >= M , 'fin frérot , tu ne peux pas faire ça , ce n\'est pas dans les régles '
		M=a.GetValeur()
		return PC([a,b,c,d]),M
	elif x== "2" :
		print("Quel est le plus petit l'indice du triplé que tu veux jouer ? (ex : tape 8 pour le triplé des cartes 8,9,10)")
		z= input(">")
		z=int(z)
		assert z < J.GetNbCarteJ()-1 , 'Entrez un nombre Valide (entre 1 et 13)'
		a=J.TirerCarte(z)
		b=J.TirerCarte(z)
		c=J.TirerCarte(z)
		assert a.GetValeur() == b.GetValeur() == c.GetValeur() , 'fin frérot , tu triche'
		assert a.GetValeur() >= M , 'fin frérot , tu ne peux pas faire ça , ce n\'est pas dans les régles '
		M=a.GetValeur()
		return PC([a,b,c]),M
	elif x=='3' :
		print("Quel est le plus petit l'indice du double que tu veux jouer ? (ex : tape 8 pour le double des cartes 8,9)")
		z= input(">")
		z=int(z)
		assert z < J.GetNbCarteJ() , 'Entrez un nombre Valide (entre 1 et 13)'
		a=J.TirerCarte(z)
		b=J.TirerCarte(z)
		assert a.GetValeur() == b.GetValeur() , 'fin frérot , tu triche'
		assert a.GetValeur() >= M , 'fin frérot , tu ne peux pas faire ça , ce n\'est pas dans les régles '
		M=a.GetValeur()
		return PC([a,b]),M
	elif x=='4' :
		print("Quel est l'indice de la carte tu veux jouer ? ")
		z= input(">")
		z=int(z)
		assert z<=J.GetNbCarteJ() , 'Entrez un nombre Valide (entre 1 et 13)'
		a=J.TirerCarte(z)
		assert a.GetValeur() >= M , 'fin frérot , tu ne peux pas faire ça , ce n\'est pas dans les régles '
		M=a.GetValeur()
		return PC([a]),M
	elif x=='5' :
		return None,M
	else :
		sys.exit('Tu as quitté le programme')
		
def QP(J1:JP,J2:JP,J3:JP,J4:JP) :
	if J1.GetNbCarteJ() == 0 :
		J1.DefSatut('President')
		return J1
	elif J2.GetNbCarteJ() == 0 :
		J2.DefSatut('President')
		return J2
	elif J3.GetNbCarteJ() == 0 :
		J3.DefSatut('President')
		return J3
	elif J4.GetNbCarteJ() == 0 :
		J4.DefSatut('President')
		return J4

def P(J1:JP,J2:JP,J3:JP,J4:JP)-> bool :
	"""
	dit si un président a été désigné
	"""
	if J1.GetNbCarteJ() == 0 :
		return True
	elif J2.GetNbCarteJ() == 0 :
		return True
	elif J3.GetNbCarteJ() == 0 :
		return True
	elif J4.GetNbCarteJ() == 0 :
		return True
	else :
		return False
	
def QVP(J1:JP,J2:JP,J3:JP) :
	if J1.GetNbCarteJ() == 0 :
		J1.DefSatut('Vice-President')
		return J1
	elif J2.GetNbCarteJ() == 0 :
		J2.DefSatut('Vice-President')
		return J2
	elif J3.GetNbCarteJ() == 0 :
		J3.DefSatut('Vice-President')
		return J3

def VP(J1:JP,J2:JP,J3:JP)-> bool :
	"""
	dit si un président a été désigné
	"""
	if J1.GetNbCarteJ() == 0 :
		return True
	elif J2.GetNbCarteJ() == 0 :
		return True
	elif J3.GetNbCarteJ() == 0 :
		return True
	else :
		return False

def QVTDC(J1:JP,J2:JP) :
	if J1.GetNbCarteJ() == 0 :
		J1.DefSatut('ViceTDC')
		return J1,J2
	elif J2.GetNbCarteJ() == 0 :
		J2.DefSatut('ViceTDC')
		return J2,J1

def VTDC(J1:JP,J2:JP,J3:JP,J4:JP)-> bool :
	"""
	dit si un président a été désigné
	"""
	if J1.GetNbCarteJ() == 0 :
		return True
	elif J2.GetNbCarteJ() == 0 :
		return True
	else :
		return False
	










#silver