#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:26:27 2026

@author: tristanbourgeois
"""
# from test_couleurs import couleur
from enum import StrEnum

Couleur = StrEnum('Couleur', [('PIQUE', '♠'), ('COEUR', '♥'), ('CARREAU', '♦'), ('TREFLE', '♣')])


class Carte:
    def __init__(self,couleur,ordre,cache):
        self.couleur = couleur
        self.ordre = ordre
        self.cache = False
    
    @property
    def couleur(self):
        return(self.couleur)
    @property
    def ordre(self):
        return(self.ordre)
    @property
    def cache(self):
        return(self.cache)
    
    def devoiler(self):
        self.cache = False
    def cacher(self):
        self.cache = True
        
    def __str__(self):
        if self.cache == True:
            return ['██']
        else:
            if self.ordre < 11:
                return [str(self.ordre) + str(Couleur.self.couleur)]
            elif self.ordre == 11:
                return ['J' + str(Couleur.self.couleur)]
            elif self.ordre == 12:
                return ['Q' + str(Couleur.self.couleur)]
            elif self.ordre == 13:
                return ['K' + str(Couleur.self.couleur)]
            elif self.ordre == 13:
                return ['A' + str(Couleur.self.couleur)]
            
    def __eq__(self,other):
        return self.couleur == other.couleur and self.ordre == other.ordre
        