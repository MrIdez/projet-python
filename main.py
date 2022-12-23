from JeuDeCarte import Bataille, BatailleV2, President, AideJeDeCarte
from Class import AideClass
import Fun 
import time as t
import sys
import os



def MonPrint(txt:str) :
	""" un beau print """
	for elem in txt :
		t.sleep(0.047)
		print(elem,end='',flush=True)
		
	print('')

def aide() :
	"""Fonction d'aide """
	print("Sur quel fonction veux-tu de l'aide ?")
	print("1. Bataille")
	print("2. Roullette Russe")
	print("3. President(Beta)")
	print("4. Tes Chances de te faire supprimer")
	print("5. Pile ou Face")
	print("6. Class (Pour les utilisateurs avancée )")
	x=input(">")
	if x=='1' :
		MonPrint('Fonction 1 :')
		help(Bataille)
		print('')
		print("Suivant")
		fin=input()
		if fin != None :
			AideJeDeCarte(1)
	elif x=='2' :
		help(Fun.roulette_russe)
	elif x=='3' :
		help(President)
		AideJeDeCarte(2)
	elif x=='4' :
		help(Fun.ChanceSuppr)
	elif x=='5':
		help(Fun.Pile_ou_Face)
	else :
		AideClass()

def main() :
	if os.name in ('posix','osix','linux') :
		os.system('clear')
	if os.name in ('nt', 'dos'):
		os.system('cls')
		t.sleep(2)
	print('Salut !')
	print("Si tu es ici c'est surement pour jouer a de nombreux Jeux (Bon, il en n'a que deux pour l'instant mais bon... )",flush=True)
	print('\n')
	print("À quelle jeux veux tu jouer ? Répond vite et pars le numéro de l'action que tu veux")
	print('')
	t.sleep(1)
	MonPrint("1. Bataille")
	MonPrint("2. Roullette Russe")
	MonPrint("3. President(Beta)")
	MonPrint("4. Tes Chances de te faire supprimer")
	MonPrint("5. Pile ou Face")
	print('')
	print("Entrée. Quitter le programme")
	print("?. Aide")
	x=input('> ')
	if x=='1' :
		print('Qui est tu , joueur 1 ?\nRépond ou je te répond')
		P1 = input('>')
		print('')
		print('Qui est tu , joueur 2 ?\nRépond ou je te répond')
		P2 = input('>')
		BatailleV2(P1,P2)
		t.sleep(1)
		print('')
		print("Alors c'étais bien ? En vérité tu ne peux répondre et je m'en fiche mais bon ça fait plus stylé")
		t.sleep(1)
		MonPrint('On remet ça ??')
		print("1.Oui,avec les même noms 2.Oui, mais je veux changé de noms 3.Non")
		z=input('> ')
		if z == '1' :
			BatailleV2(P1,P2)
		elif z== '2' :
			Bataille()
		else :
			sys.exit()
	elif x=='2' :
		print('Qui est tu , joueur 1 ?\nRépond ou je te répond')
		nom1 = input('>')
		print('')
		print('Qui est tu , joueur 2 ?\nRépond ou je te répond')
		nom2 = input('>')
		return Fun.roulette_russe(nom1,nom2)
	elif x=='3' :
		print('Qui est tu , joueur 1 ?\nRépond ou je te répond')
		P1 = input('>')
		print('')
		print('Qui est tu , joueur 2 ?\nRépond ou je te répond')
		P2 = input('>')
		print('')
		print('Qui est tu , joueur 3 ?\nRépond ou je te répond')
		P3 = input('>')
		print('')
		print('Qui est tu , joueur 4 ?\nRépond ou je te répond')
		P4 = input('>')
		return President(P1,P2,P3,P4) 
	elif x=='4' :
		print('Qui est tu ?')
		iu = input('>')
		oo=Fun.ChanceSuppr()
		print(iu.upper(),'tu a',oo,'chance de te faire supprimer')
	elif x=='5' :
		print(Fun.Pile_ou_Face())
	elif x=='' :
		sys.exit('Fais attention, tu pourrais par un hasard très malheureux te faire radier sans préavis du club des vivants dans les 24 prochaines heures')
	elif x=='?' :
		aide()
	else : 
		print("Tu as mal répondu, c'était pourtant simple.... ")
		print("Néanmoins je te laisse une autre chance de bien répondre")
		t.sleep(1)
		return main()
	t.sleep(1)
	print('')
	MonPrint("Alors c'étais bien , Non ?")
	print("De toute façon le jeu et fini , oui je sais c'est dur ")
	print("Neanmoins tu peux continuer de jouer car le programme se relançera dés que tu appuiras sur 'Entrée'.")
	fin=input()
	if fin != None :
		MonPrint('3\n')
		t.sleep(1)
		MonPrint('2\n')
		t.sleep(1)
		MonPrint('1')
		t.sleep(1)
		return main()
main()


