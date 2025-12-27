"""
Module environment.py
Gère l'état de l'environnement (les deux chambres A et B).
"""


class Environment:
    """
    Représente l'environnement avec deux chambres A et B.
    Chaque chambre peut être "sale" (True) ou "propre" (False).
    """
    
    def __init__(self, room_a_dirty=True, room_b_dirty=True):
        """
        Initialise l'environnement.
        
        Args:
            room_a_dirty (bool): État initial de la chambre A (True = sale, False = propre)
            room_b_dirty (bool): État initial de la chambre B (True = sale, False = propre)
        """
        self.room_a_dirty = room_a_dirty
        self.room_b_dirty = room_b_dirty
    
    def is_room_a_dirty(self):
        """Retourne True si la chambre A est sale."""
        return self.room_a_dirty
    
    def is_room_b_dirty(self):
        """Retourne True si la chambre B est sale."""
        return self.room_b_dirty
    
    def clean_room_a(self):
        """Nettoie la chambre A (la rend propre)."""
        self.room_a_dirty = False
    
    def clean_room_b(self):
        """Nettoie la chambre B (la rend propre)."""
        self.room_b_dirty = False
    
    def make_room_a_dirty(self):
        """Salit la chambre A (la rend sale)."""
        self.room_a_dirty = True
    
    def make_room_b_dirty(self):
        """Salit la chambre B (la rend sale)."""
        self.room_b_dirty = True
    
    def get_state(self):
        """
        Retourne l'état actuel de l'environnement.
        
        Returns:
            dict: Dictionnaire avec l'état des deux chambres
        """
        return {
            'A': 'sale' if self.room_a_dirty else 'propre',
            'B': 'sale' if self.room_b_dirty else 'propre'
        }
    
    def __str__(self):
        """Représentation textuelle de l'environnement."""
        state = self.get_state()
        return f"Chambre A: {state['A']}, Chambre B: {state['B']}"

