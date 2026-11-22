#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:12:32 2026

@author: tristanbourgeois
"""

class Pile:
    def __init__(self,jeu):
        self._cartes = []
        for carte in range(4):
            carte = jeu.piocher()
            carte.cacher()
            self._carte.append(carte)
        self.carte[-1].devoiler()
    
    def __str__(self):
        return " ".join(str(carte for carte in self.cartes))
    
    def __len__(self):
        return len(self._cartes)
    
    def pop(self):
        if len(self.liste) == 0:
            return None
        carte = self._cartes.pop()
        if len(self._cartes) > 0:
            self.cartes[-1].devoiler()
        return carte
            