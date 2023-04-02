import random


def AideClass():
	help(File)
	help(CarteBridge)
	help(CartePresident)
	help(JeuDeCarteBridge)
	help(JeuDeCartePresident)
	help(PaquetDeCarte)
	help(Joueur)
	help(JoueurPresident)
	help(JoueurPoker)


class File:
	"""Une Classe de file"""

	def __init__(self):
		""" créer un file vide """
		self.taille = 0
		self.contenu = []

	def EstVide(self):
		""" Renvoie si la file est vide"""
		return self.taille == 0

	def Enfiler(self, elem):
		""" Enfile un element dans la file """
		self.taille += 1
		self.contenu.append(elem)

	def Defiler(self):
		""" Defile la file"""
		assert not self.EstVide(), 'La File est vide'
		p = self.contenu.pop(0)
		self.taille -= 1
		return p

	def Tete(self):
		"""Renvoie la tete de la file sans la supprimer """
		assert not self.EstVide(), 'La File est vide'
		p = self.contenu
		return p[0]

	def Queue(self):
		""" Renvoie la Queue de la file sans la supprimer """
		assert not self.EstVide(), 'La File est vide'
		p = self.contenu
		return p[len(p) - 1]

	def GetTaille(self):
		""" Renvoie la Taille de la file """
		return self.taille

	def GetContenu(self):
		""" Renvoie le contenu de la file """
		return self.contenu

	def Affiche(self):
		""" Affiche le contenu de la file """
		print(self.contenu)

	def __str__(self):
		"""Renvoie le contenu de la file sous forme de chaine de caractére """
		return str(self.contenu)


class CarteBridge:
	"""
    Classe définissant une carte caratérisée par :
        sa valeur
        sa couleur
        sa figure
    """

	def __init__(self, val, coul):
		LFig = [None, 'Un', 'Deux', 'Trois', 'Quatre', 'Cinq', 'Six', 'Sept', 'Huit', 'Neuf', 'Dix', 'Valet', 'Dame',
				'Roi', 'As']
		self.__valeur = val
		self.__couleur = coul
		self.__figure = LFig[val]

	# getters
	def GetValeur(self):
		"""Renvoie la valeur de la carte"""
		return self.__valeur

	def GetCouleur(self):
		"""Renvoie la couleur de la carte"""
		return self.__couleur

	def GetFigure(self):
		"""Renvoie la figure de la carte"""
		return self.__figure

	# setters
	def __SetFigure(self, fig):
		self.__figure = fig

	def _SetValeur(self, val):
		self.__valeur = val

	def _SetCouleur(self, coul):
		self.__couleur = coul

	# Fonction d'affichage
	def Affiche(self):
		""" Affiche la Carte """
		print(self.GetFigure(), 'de', self.GetCouleur())


class CartePresident:
	"""
    Classe définissant une carte caratérisée par :
        sa valeur
        sa couleur
        sa figure
    """

	def __init__(self, val, coul):
		LFig = [None, None, 'Trois', 'Quatre', 'Cinq', 'Six', 'Sept', 'Huit', 'Neuf', 'Dix', 'Valet', 'Dame', 'Roi',
				'As', 'Deux']
		self.__valeur = val
		self.__couleur = coul
		self.__figure = LFig[val]

	# getters
	def GetValeur(self):
		"""Renvoie la valeur de la carte"""
		return self.__valeur

	def GetCouleur(self):
		"""Renvoie la couleur de la carte"""
		return self.__couleur

	def GetFigure(self):
		"""Renvoie la valeur de la carte"""
		return self.__figure

	# setters
	def __SetFigure(self, fig):
		self.__figure = fig

	def _SetValeur(self, val):
		self.__valeur = val

	def _SetCouleur(self, coul):
		self.__couleur = coul

	# Fonction d'affichage
	def Affiche(self):
		""" Affiche la Carte """
		print(self.GetFigure(), 'de', self.GetCouleur())


class CarteUno:
	"""
    Classe définissant une carte caratérisée par :
        sa valeur
        sa couleur
        sa figure
    """

	def __init__(self, val, coul):
		LFig = ['Zéro', 'Un', 'Deux', 'Trois', 'Quatre', 'Cinq', 'Six', 'Sept', 'Huit', 'Neuf', '+2',
				'Inversement de sens', 'Passe ton tour', 'Joker', '+4']
		self.__valeur = val
		self.__couleur = coul
		self.__figure = LFig[val]

	# getters
	def GetValeur(self):
		"""Renvoie la valeur de la carte"""
		return self.__valeur

	def GetCouleur(self):
		"""Renvoie la couleur de la carte"""
		return self.__couleur

	def GetFigure(self):
		"""Renvoie la valeur de la carte"""
		return self.__figure

	# setters
	def __SetFigure(self, fig):
		self.__figure = fig

	def _SetValeur(self, val):
		self.__valeur = val

	def _SetCouleur(self, coul):
		self.__couleur = coul

	# Fonction d'affichage
	def Affiche(self):
		""" Affiche la Carte """
		if self.GetValeur() > 12:
			print(self.GetFigure())
		else:
			print(self.GetFigure(), self.GetCouleur())


class JeuDeCarteBridge:

	def CreerJeu(self, nb):
		"""Crée un paquet de 32 ou 54 Carte"""
		Jeu = []
		if nb == 32:
			mini = 7
		else:
			mini = 2
		for coul in ['Tréfle', 'Pique', 'Carreaux', 'Coeur']:
			for k in range(mini, 15):
				une_carte = CarteBridge(k, coul)
				Jeu.append(une_carte)
		return Jeu

	def __init__(self, nb):
		""" initialise le Paquet """
		self.nombre = nb
		self.Jeu = self.CreerJeu(nb)

	# getters

	def GetJeu(self):
		"""renvoie le Jeu"""
		return self.Jeu

	def GetNbCarte(self):
		"""Renvoie le nombre de Carte """
		return self.nombre

	def Melanger(self):
		""" Mélange le Jeu"""
		return random.shuffle(self.Jeu)


class JeuDeCartePresident:

	def CreerJeu(self):
		""" crée le jeu """
		Jeu = []
		for coul in ['Tréfle', 'Pique', 'Carreaux', 'Coeur']:
			for k in range(2, 15):
				une_carte = CartePresident(k, coul)
				Jeu.append(une_carte)
		return Jeu

	def __init__(self):
		""" initialise le Paquet de President"""
		self.Jeu = self.CreerJeu()

	# getters

	def GetJeu(self):
		"""renvoie le Jeu"""
		return self.Jeu

	def Melanger(self):
		""" Mélange le Jeu"""
		return random.shuffle(self.Jeu)


class JeuDeCarteUno:

	def CreerJeu(self):
		""" crée le jeu """
		Jeu = []
		for i in range(2):
			for coul in ['Vert', 'Rouge', 'Bleu', 'Jaune']:
				for k in range(0, 12):
					une_carte = CarteUno(k, coul)
					Jeu.append(une_carte)
		for j in range(4):
			c = CarteUno(13, 'Carte Spéciale')
			c2 = CarteUno(14, 'Carte Spéciale')
			Jeu.append(c)
			Jeu.append(c2)
		return Jeu

	def __init__(self):
		""" initialise le Paquet de President"""
		self.Jeu = self.CreerJeu()

	# getters

	def GetJeu(self):
		"""renvoie le Jeu"""
		return self.Jeu

	def Melanger(self):
		""" Mélange le Jeu"""
		return random.shuffle(self.Jeu)


class PaquetDeCarte:
	"""
    Creer un paquet de carte
    avec pour attribue le contenu et le nb de carte
    """

	def __init__(self, p: list):
		""" init le paquet de Carte , les cartes doivent être de la class Carte"""
		self.nbcarte = len(p)
		self.paquet = File()
		for elem in p:
			self.paquet.Enfiler(elem)

	def TirerCarte(self):
		""" Tire la premiere carte de ce paquet """
		return self.paquet.Defiler()

	def Distribuer(self, nbCarte):
		""" Distribue un nb de carte de ce paquet , elle n'y sont plus aprés """
		Main = []
		for i in range(nbCarte):
			Main.append(self.TirerCarte())
		return Main

	def RamasserC(self, p):
		"""Ramasse un paquet de Carte """
		if random.randint(1, 2) == 1:
			p.reverse()
		for elem in p:
			self.AjouterCarte(elem)

	def AjouterCarte(self, c):
		"""Ajoute un carte dans la pioche """
		self.paquet.Enfiler(c)
		self.nb_carte += 1

	def AffichePaquet(self):
		""" Affiche le paquet de Carte """
		for c in self.paquet.GetContenu():
			c.Affiche()

	def GetTaille(self):
		""" Renvoie la taille du Paquet """
		return self.paquet.GetTaille()


class Joueur:
	def __init__(self, nomJoueur):
		self.nom_joueur = nomJoueur
		self.__pioche = File()
		self.nb_carte = 0

	def AjouterCarte(self, c):
		"""Ajoute un carte dans la pioche """
		self.__pioche.Enfiler(c)
		self.nb_carte += 1

	def Ramasser(self, p):
		"""Ramasse un paquet de Carte """
		if random.randint(1, 2) == 1:
			p.reverse()
		for elem in p:
			self.AjouterCarte(elem)

	def TirerCarte(self):
		"""Tire une carte de la pioche du joueur"""
		c = self.__pioche.Defiler()
		self.nb_carte -= 1
		return c

	def TirerCarteNum(self, x):
		"""Tire la carte x de la pioche du joueur"""
		x = int(x)
		c = self.__pioche[x]
		self.nb_carte -= 1
		return c

	def GetNbCarteJ(self):
		"""Renvoie le nombre de carte du joueur"""
		return self.nb_carte

	def GetNom(self):
		"""Renvoie le nom du joueur"""
		return self.nom_joueur

	def __GetPioche(self):
		"""Renvoie la pioche du joueur"""
		p = self.__pioche
		return p

	def AffichePioche(self):
		"""Affiche la pioche du joueur"""
		for i in range(self.__pioche.GetTaille()):
			x = self.__pioche.Defiler()
			print(i + 1, '.', end=' ', sep='')
			x.Affiche()
			self.__pioche.Enfiler(x)


class JoueurPresident:
	def __init__(self, nomJoueur):
		"""Initialise le joueur sans pioche et neutre """
		self.nom_joueur = nomJoueur
		self.__pioche = []
		self.nb_carte = 0
		self.statut = 'Neutre'

	def AjouterCarte(self, c):
		"""Ajoute une carte par odre croissant dans la pioche """
		self.__pioche.append(None)
		m = c
		i = len(self.__pioche) - 1
		while i > 0 and m.GetValeur() < self.__pioche[i - 1].GetValeur():
			self.__pioche[i] = self.__pioche[i - 1]
			i -= 1
		self.__pioche[i] = m
		self.nb_carte += 1

	def Ramasser(self, p):
		"""Ramasse un paquet de Carte """
		if random.randint(1, 2) == 1:
			p.reverse()
		for elem in p:
			self.AjouterCarte(elem)

	def TirerCarte(self, x):
		"""Tire la carte x de la pioche du joueur"""
		x = int(x)
		c = self.__pioche.pop(x - 1)
		self.nb_carte -= 1
		return c

	def DefSatut(self, statut: str):
		""" Defini le statut du joueur (Président, vice- President , neutre ...)"""
		self.statu = statut

	def GetNbCarteJ(self):
		"""Renvoie le nombre de carte du joueur"""
		return self.nb_carte

	def GetNom(self):
		"""Renvoie le nom du joueur"""
		return self.nom_joueur

	def __GetPioche(self):
		"""Renvoie la pioche du joueur"""
		p = self.__pioche
		return p

	def GetStatue(self):
		return self.statu

	def AffichePioche(self):
		"""Affiche la pioche du joueur"""
		for i in range(len(self.__pioche) - 1):
			print(i + 1, '.', end=' ', sep='')
			c = self.__pioche[i]
			c.Affiche()


class JoueurPoker:
	def __init__(self, nomJoueur, argent):
		self.nom_joueur = nomJoueur
		self.__pioche = File()
		self.__nb_carte = 0
		self.__argent = argent
		self.mise = 0
		self.couché = False

	def AjouterCarte(self, c):
		"""Ajoute un carte dans la pioche """
		self.__pioche.Enfiler(c)
		self.__nb_carte += 1

	def Ramasser(self, p):
		"""Ramasse un paquet de Carte """
		if random.randint(1, 2) == 1:
			p.reverse()
		for elem in p:
			self.AjouterCarte(elem)

	def TirerCarte(self):
		"""Tire une carte de la pioche du joueur"""
		c = self.__pioche.Defiler()
		self.__nb_carte -= 1
		return c

	def Debiter(self, somme):
		"""Debite au joueur une somme """
		self.__argent -= somme

	def Créditer(self, somme):
		"""Crédite le joueur d'une certaine somme"""
		self.__argent += somme

	def Miser(self, somme):
		self.mise += somme

	def GetNbCarteJ(self):
		"""Renvoie le nombre de carte du joueur"""
		return self.__nb_carte

	def Coucher(self):
		"Couche le joueur"
		self.couché = True

	def __Debout(self):
		self.couché = False

	def GetNom(self):
		"""Renvoie le nom du joueur"""
		return self.nom_joueur

	def __GetPioche(self):
		"""Renvoie la pioche du joueur"""
		p = self.__pioche
		return p

	def GetArgent(self):
		"""Renvoie l'argent du joueur"""
		return self.__argent

	def AffichePioche(self):
		"""Affiche la pioche du joueur"""
		for c in self.__pioche.GetContenu():
			c.Affiche()
