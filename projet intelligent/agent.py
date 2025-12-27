"""
Module agent.py
Implémente un agent aspirateur à réflexe simple.
L'agent observe l'environnement et agit selon des règles simples.
"""


class VacuumAgent:
    """
    Agent aspirateur à réflexe simple.
    L'agent n'a pas de mémoire : il réagit uniquement à l'état actuel de l'environnement.
    """
    
    def __init__(self, initial_position='A'):
        """
        Initialise l'agent.
        
        Args:
            initial_position (str): Position initiale de l'agent ('A' ou 'B')
        """
        self.position = initial_position  # Position actuelle : 'A' ou 'B'
    
    def get_position(self):
        """Retourne la position actuelle de l'agent."""
        return self.position
    
    def move_to(self, room):
        """
        Déplace l'agent vers une chambre.
        
        Args:
            room (str): 'A' ou 'B'
        """
        if room in ['A', 'B']:
            self.position = room
    
    def observe(self, environment):
        """
        Observe l'état de l'environnement.
        
        Args:
            environment: Objet Environment à observer
            
        Returns:
            dict: État observé (chambres sales ou propres)
        """
        return {
            'A': environment.is_room_a_dirty(),
            'B': environment.is_room_b_dirty()
        }
    
    def act(self, environment):
        """
        L'agent observe l'environnement et agit selon des règles simples.
        C'est un agent à réflexe simple : pas de mémoire, réaction immédiate.
        
        Règles :
        1. Si les deux chambres sont sales → nettoie celle où il se trouve, puis se déplace vers l'autre
        2. Si une seule chambre est sale → se déplace vers celle-ci et la nettoie
        3. Si les deux chambres sont propres → ne fait rien (attend)
        
        Args:
            environment: Objet Environment à nettoyer
            
        Returns:
            str: Description de l'action effectuée
        """
        # Observation de l'environnement
        state = self.observe(environment)
        room_a_dirty = state['A']
        room_b_dirty = state['B']
        
        # Règle 1 : Les deux chambres sont sales
        if room_a_dirty and room_b_dirty:
            # Nettoie la chambre où il se trouve actuellement
            if self.position == 'A':
                environment.clean_room_a()
                self.move_to('B')  # Se déplace vers B pour la nettoyer au prochain cycle
                return "Nettoyage de la chambre A, déplacement vers B"
            else:  # position == 'B'
                environment.clean_room_b()
                self.move_to('A')  # Se déplace vers A pour la nettoyer au prochain cycle
                return "Nettoyage de la chambre B, déplacement vers A"
        
        # Règle 2 : Seule la chambre A est sale
        elif room_a_dirty and not room_b_dirty:
            if self.position != 'A':
                self.move_to('A')
                return "Déplacement vers la chambre A"
            else:
                environment.clean_room_a()
                return "Nettoyage de la chambre A"
        
        # Règle 3 : Seule la chambre B est sale
        elif not room_a_dirty and room_b_dirty:
            if self.position != 'B':
                self.move_to('B')
                return "Déplacement vers la chambre B"
            else:
                environment.clean_room_b()
                return "Nettoyage de la chambre B"
        
        # Règle 4 : Les deux chambres sont propres
        else:  # not room_a_dirty and not room_b_dirty
            return "Les deux chambres sont propres, l'agent attend"

