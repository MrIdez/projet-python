import random
import time
from FonctionBataille import JeuBataille, AideBataille
from FonctionPresident import PremierePartiePresident as Pa1

def AideJeDeCarte(nbjeu:int) :
	if nbjeu == 1 :
		AideBataille()
	else :
		help(Pa1)

def MonPrint(txt:str) :
	for elem in txt :
		time.sleep(0.02)
		print(elem,end='',flush=True)

def test(nbfois) :
	vainqueurA=0
	vainqueurB=0
	totalcoup=0
	Mcoup=0
	for i in range(nbfois) :
		x,y=JeuBataille('1','2')
		if x==1 :
			vainqueurA+=1
		else :
			vainqueurB+=1
		totalcoup+=y
	Mcoup=totalcoup/nbfois
	return vainqueurA,vainqueurB,Mcoup

def Bataille() :
	"""
	Cette Fonction permet de rendre accesible à l'utilisateur le jeu de la Bataille , elle fait appel a la Fonction JeuBataille pour toutes les opérations alogorithmiques
	"""
	print('Qui est tu , joueur 1 ?\nRépond ou je te répond')
	P1 = input('>')
	print('')
	print('Qui est tu , joueur 2 ?\nRépond ou je te répond')
	P2 = input('>')
	time.sleep(1)
	MonPrint('LA BATAILLE PEUT COMENCER !!\n')
	time.sleep(1)
	v,nbcoup = JeuBataille(P1, P2,1)
	
	if nbcoup == 69 :
		print('Nice, 69 coups !')
	
	if random.randint(1, 6)==4 :
		if v == 1 :
			print('32 - 0 !!! \nC\'est la piquette',P2,'Tu sais pas jouer',P2,'\nT\'ES MAUVAIS !!!!')
		else :
			print('32 - 0 !!! \nC\'est la piquette',P1,'Tu sais pas jouer',P1,'\nT\'ES MAUVAIS !!!!')
	else :
		if v == 1 :
			print('Bravo ,',P1,'tu es le champion de cet bataille !\n Tu as gagné en',nbcoup,'Coups \n N\'hésite pas à jouer a la roulette russe,',P2, 'n\'aurais pas pu prendre sa revanche..')
		else :
			print('Bravo ,',P1,'tu es le champion de cet bataille !\n Tu as gagné en',nbcoup,'Coups \n N\'hésite pas à jouer a la roulette russe,',P2, 'n\'aurais pas pu prendre sa revanche..')

def BatailleV2(P1:str,P2:str) :
	time.sleep(1)
	MonPrint('LA BATAILLE PEUT COMENCER !!\n')
	time.sleep(1)
	v,nbcoup = JeuBataille(P1, P2,1)
	
	if nbcoup == 69 :
		print('Nice, 69 coups !')
	
	if random.randint(1, 6)==4 :
		if v == 1 :
			print('32 - 0 !!! \nC\'est la piquette',P2,'Tu sais pas jouer',P2,'\nT\'ES MAUVAIS !!!!')
		else :
			print('32 - 0 !!! \nC\'est la piquette',P1,'Tu sais pas jouer',P1,'\nT\'ES MAUVAIS !!!!')
	else :
		if v == 1 :
			print('Bravo ,',P1,'tu es le champion de cet bataille !\n Tu as gagné en',nbcoup,'Coups \n N\'hésite pas à jouer a la roulette russe,',P2, 'n\'aurais pas pu prendre sa revanche..')
		else :
			print('Bravo ,',P1,'tu es le champion de cet bataille !\n Tu as gagné en',nbcoup,'Coups \n N\'hésite pas à jouer a la roulette russe,',P2, 'n\'aurais pas pu prendre sa revanche..')

def President(p1,p2,p3,p4) :
	print('-------------------------------------------------------------------')
	print('Beta - Seulement la premiere partie est disponible')
	print('-------------------------------------------------------------------')
	president,Vice_President,Vice_TDC,TDC=Pa1(p1,p2,p3,p4)