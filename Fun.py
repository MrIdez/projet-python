import random
import time

def roulette_russe(nom1,nom2) :
	"""Fonction de roulette russe sauf que on peut perdre plusieurs fois (Ou pas ......) """
	if random.randint(1, 6)==1 :
		print(nom1,'a été supprimé par le parrain, il est donc le grand perdant de cette roulette russe' )
	else :
		print('Félicitation',nom1,'Tu a survécu ! \n C\'est maintenant au tour de ',nom2,'Bonne Chance à lui !')
		time.sleep(2)
		return roulette_russe(nom2,nom1)


def ChanceSuppr() :
	'''Renvoie les chances de te faire supprimer par le parrain '''
	return random.uniform(100000.5465465464898,1000000000.6216544)


def Pile_ou_Face() :
	'''Pile ou Face ? '''
	if random.randint(1,2) == 1 :
		return 'Pile'
	else :
		return 'Face'
	
def get_rep(mot:str) :
	while True :
		rep = input('Réponse :')
		rep=rep.lower()
		if len(rep)!=1 :
			if rep == mot :
				return rep
			else :
				print(mot)
				print("Le mot que tu a proposé est incorect, je te conseil de tenter un caractére")
		else :
			return rep

def nouv_mt(mot,tr,rep) :
	for i in range(len(mot)):
		if mot[i] == rep:
			tr = tr[:i] + rep + tr[i + 1:]
	return tr

def Trouve_Le_mot(Lmot:list,Joueur:str='') :
	mot=random.choice(Lmot)
	mot=mot.lower()
	print(mot)
	vies = 10
	mt= "-" * len(mot)
	while vies > 0 and mt != mot :
		print('Ton mot :',mt)
		print(str(vies) + " vies restante")
		rep = get_rep(mot)
		if rep == mot :
			print("GG tu a gagné , le mot étais bien :  " + mot)
			return Joueur
		mt = nouv_mt(mot,mt,rep)
		if rep in mot:
			print("La lettre est dans le mot")
		else:
			print("Mince , ta lettre n'est pas dans le mot")
			vies = vies - 1
	if vies == 0:
		 print("Perdu !! le mot étais : " + mot)
		 return Joueur
	else:
		print("GG tu a gagné , le mot étais bien :  " + mot)
		return Joueur
			
	
	
			
