from enum import Enum
from enum import StrEnum

class couleur(Enum):
    Pique = 1
    COEUR = 2
    CARREAU = 3
    TREFLE = 4

Couleur = StrEnum('Couleur', [('PIQUE', '♠'), ('COEUR', '♥'), ('CARREAU', '♦'), ('TREFLE', '♣')])
print(Couleur)

# carte.py
from couleurs import Couleur
from carte import Carte
from jeu import Jeu
from pile import Pile

class Solitaire:
    
    NB_PILE = 8
    
    def __init__(self):
        jeu = Jeu()
        self.piles = [Pile(jeu) for _ in range(8)]
    
        
    def est_enlevable(self,i,j):
        if i == j:
            return False
        if len(self.piles(i)) == 0 or len(self.piles(j)) == 0:
            return False
        
        carte_i = self.piles(i)[-1]
        carte_j = self.piles(j)[-1]
        
        return carte_i.ordre == carte_j.ordre
    
    def elever(self,i,j):
        enlev = self.est_enlevable(self,i,j)
        if enlev == False:
            return False
        self.piles(i).pop()
        self.piles(j).pop()
        
        return True
    
    def est_termine(self):
        
        for i in range(len(self.piles)):
            for j in range(len(self.piles)):
                if self.est_enlevable(i,j) == True:
                    return False
        return True
    
    def est_vide(self):
        for pile in self.piles:
            if len(pile) != 0: 
                return False
        return True
        
            
        


