


from enum import Enum
from enum import StrEnum

class Couleur(Enum):
    Pique = 1
    COEUR = 2
    CARREAU = 3
    TREFLE = 4

Couleur = StrEnum('Couleur', [('PIQUE', '♠'), ('COEUR', '♥'), ('CARREAU', '♦'), ('TREFLE', '♣')])
print(Couleur.CARREAU)


def test_couleurs():
    assert len(Couleur) == 4
    assert Couleur.PIQUE == '♠'
    assert Couleur.COEUR == '♥'
    assert Couleur.PIQUE != Couleur.COEUR

print(test_couleurs())