#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:45:08 2026

@author: tristanbourgeois
"""

from carte.py import Carte
from enum import StrEnum
import random

Couleur = StrEnum('Couleur', [('PIQUE', '♠'), ('COEUR', '♥'), ('CARREAU', '♦'), ('TREFLE', '♣')])


class Jeu:
    Cartes = [Carte(i,Couleur.PIQUE,True)for i in range(8)] + [Carte(i,Couleur.COEUR,True)for i in range(8)] + [Carte(i,Couleur.TREFLE,True)for i in range(8)] + [Carte(i,Couleur.CARREAU,True)for i in range(8)]
    Cartes = random.shuffle(Cartes)
    
    def __str__(self):
        if self.cache:
            return'**'
        else:
            return([str(self.ordre) + str(self.cache)])
        return()
    def __pop__(Cartes):
        if len(Cartes) == 0:
            return None
        else:
            Cartes = Cartes.pop()
            return Cartes
        