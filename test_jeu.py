
from carte import Carte
from couleurs import Couleur
from jeu import Jeu


def test_jeu_creation_taille():
    """Vérifie qu'un nouveau jeu contient exactement 32 cartes."""
    jeu = Jeu()
    assert len(jeu.cartes) == 32

def test_jeu_composition():
    """Vérifie que le jeu contient bien toutes les 32 cartes attendues (du 7 à l'as pour chaque couleur)."""
    jeu = Jeu()
    valeurs_attendues = [1] + list(range(7, 14))
    
    # On vérifie que chaque combinaison (couleur, ordre) est présente exactement une fois
    for couleur in Couleur:
        for ordre in valeurs_attendues:
            carte_ref = Carte(couleur, ordre)
            assert carte_ref in jeu.cartes

def test_jeu_pop():
    """Teste la méthode pop qui retire et retourne la dernière carte."""
    jeu = Jeu()
    taille_initiale = len(jeu.cartes)
    
    carte_retiree = jeu.pop()
    assert isinstance(carte_retiree, Carte)
    assert len(jeu.cartes) == taille_initiale - 1

    # Test du vidage complet du jeu
    for _ in range(31):
        jeu.pop()
    
    assert len(jeu.cartes) == 0
    assert jeu.pop() is None  # Doit retourner None si le jeu est vide

def test_jeu_str():
    """Vérifie que la méthode __str__ retourne une chaîne de caractères non vide."""
    jeu = Jeu()
    representation = str(jeu)
    assert isinstance(representation, str)
    assert len(representation) > 0