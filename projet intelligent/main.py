"""
Module main.py
Simulation en console de l'agent aspirateur.
"""

import time
from environment import Environment
from agent import VacuumAgent


def simulate_cycle(agent, environment, cycle_number):
    """
    Simule un cycle d'observation et d'action de l'agent.
    Les chambres redeviennent sales automatiquement pour créer un cycle continu.
    
    Args:
        agent: Objet VacuumAgent
        environment: Objet Environment
        cycle_number: Numéro du cycle actuel
    """
    print(f"\n{'='*60}")
    print(f"CYCLE {cycle_number}")
    print(f"{'='*60}")
    print(f"État de l'environnement : {environment}")
    print(f"Position de l'agent : Chambre {agent.get_position()}")
    
    # L'agent observe et agit
    action = agent.act(environment)
    print(f"Action de l'agent : {action}")
    
    # Après l'action de l'agent, l'autre chambre peut se salir
    # Si l'agent vient de nettoyer A, B peut se salir (ou vice versa)
    if "Nettoyage de la chambre A" in action:
        # L'agent a nettoyé A, B peut se salir pendant ce temps
        if not environment.is_room_b_dirty():
            environment.make_room_b_dirty()
            print("⚠️  La chambre B est redevenue sale pendant le nettoyage de A")
    elif "Nettoyage de la chambre B" in action:
        # L'agent a nettoyé B, A peut se salir pendant ce temps
        if not environment.is_room_a_dirty():
            environment.make_room_a_dirty()
            print("⚠️  La chambre A est redevenue sale pendant le nettoyage de B")
    
    print(f"Nouvel état : {environment}")
    print(f"Nouvelle position : Chambre {agent.get_position()}")


def main():
    """
    Fonction principale de la simulation.
    """
    print("="*60)
    print("SIMULATION D'UN AGENT ASPIRATEUR À RÉFLEXE SIMPLE")
    print("="*60)
    
    # Initialisation
    # Vous pouvez modifier l'état initial des chambres ici
    environment = Environment(room_a_dirty=True, room_b_dirty=True)
    agent = VacuumAgent(initial_position='A')
    
    print("\nConfiguration initiale :")
    print(f"État : {environment}")
    print(f"Position agent : Chambre {agent.get_position()}")
    
    # Simulation de plusieurs cycles
    num_cycles = 10  # Nombre de cycles à simuler
    
    print(f"\nDémarrage de la simulation ({num_cycles} cycles)...")
    print("(Chaque cycle représente 2 minutes de temps réel)")
    print("\nAppuyez sur Entrée pour démarrer...")
    input()
    
    for cycle in range(1, num_cycles + 1):
        simulate_cycle(agent, environment, cycle)
        
        # Pause de 2 secondes (simulation accélérée : 2 secondes = 2 minutes)
        if cycle < num_cycles:
            print("\nAttente de 2 secondes avant le prochain cycle...")
            time.sleep(2)
    
    print(f"\n{'='*60}")
    print("SIMULATION TERMINÉE")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

