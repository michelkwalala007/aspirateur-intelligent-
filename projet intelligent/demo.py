"""
Module demo.py
Démonstration visuelle de l'agent aspirateur avec Tkinter.
"""

import tkinter as tk
from tkinter import ttk
import time
import threading
from environment import Environment
from agent import VacuumAgent


class VacuumDemo:
    """
    Interface graphique pour la démonstration de l'agent aspirateur.
    """
    
    def __init__(self, root):
        """
        Initialise l'interface graphique.
        
        Args:
            root: Fenêtre principale Tkinter
        """
        self.root = root
        self.root.title("Agent Aspirateur Intelligent - Démonstration")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Initialisation de l'environnement et de l'agent
        self.environment = Environment(room_a_dirty=True, room_b_dirty=True)
        self.agent = VacuumAgent(initial_position='A')
        
        # Variables de contrôle
        self.is_running = False
        self.cycle_count = 0
        
        # Création de l'interface
        self.create_widgets()
        
        # Mise à jour initiale de l'affichage
        self.update_display()
    
    def create_widgets(self):
        """Crée les widgets de l'interface graphique."""
        
        # Titre
        title_label = tk.Label(
            self.root,
            text="Agent Aspirateur à Réflexe Simple",
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0'
        )
        title_label.pack(pady=10)
        
        # Frame pour les chambres
        rooms_frame = tk.Frame(self.root, bg='#f0f0f0')
        rooms_frame.pack(pady=20)
        
        # Chambre A
        self.room_a_frame = tk.Frame(
            rooms_frame,
            width=200,
            height=200,
            relief=tk.RAISED,
            borderwidth=3
        )
        self.room_a_frame.pack(side=tk.LEFT, padx=20)
        self.room_a_frame.pack_propagate(False)
        
        self.room_a_label = tk.Label(
            self.room_a_frame,
            text="CHAMBRE A",
            font=('Arial', 14, 'bold')
        )
        self.room_a_label.pack(pady=10)
        
        self.room_a_status = tk.Label(
            self.room_a_frame,
            text="",
            font=('Arial', 12)
        )
        self.room_a_status.pack(pady=5)
        
        self.room_a_agent = tk.Label(
            self.room_a_frame,
            text="",
            font=('Arial', 20)
        )
        self.room_a_agent.pack(pady=20)
        
        # Chambre B
        self.room_b_frame = tk.Frame(
            rooms_frame,
            width=200,
            height=200,
            relief=tk.RAISED,
            borderwidth=3
        )
        self.room_b_frame.pack(side=tk.LEFT, padx=20)
        self.room_b_frame.pack_propagate(False)
        
        self.room_b_label = tk.Label(
            self.room_b_frame,
            text="CHAMBRE B",
            font=('Arial', 14, 'bold')
        )
        self.room_b_label.pack(pady=10)
        
        self.room_b_status = tk.Label(
            self.room_b_frame,
            text="",
            font=('Arial', 12)
        )
        self.room_b_status.pack(pady=5)
        
        self.room_b_agent = tk.Label(
            self.room_b_frame,
            text="",
            font=('Arial', 20)
        )
        self.room_b_agent.pack(pady=20)
        
        # Frame pour les informations
        info_frame = tk.Frame(self.root, bg='#f0f0f0')
        info_frame.pack(pady=10)
        
        self.info_label = tk.Label(
            info_frame,
            text="",
            font=('Arial', 10),
            bg='#f0f0f0',
            wraplength=550,
            justify=tk.LEFT
        )
        self.info_label.pack()
        
        self.cycle_label = tk.Label(
            info_frame,
            text="Cycle : 0",
            font=('Arial', 10),
            bg='#f0f0f0'
        )
        self.cycle_label.pack(pady=5)
        
        # Frame pour les boutons
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        self.start_button = tk.Button(
            button_frame,
            text="Démarrer la simulation",
            command=self.start_simulation,
            font=('Arial', 12),
            bg='#4CAF50',
            fg='white',
            padx=20,
            pady=10
        )
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(
            button_frame,
            text="Arrêter",
            command=self.stop_simulation,
            font=('Arial', 12),
            bg='#f44336',
            fg='white',
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(
            button_frame,
            text="Réinitialiser",
            command=self.reset_simulation,
            font=('Arial', 12),
            bg='#2196F3',
            fg='white',
            padx=20,
            pady=10
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        self.step_button = tk.Button(
            button_frame,
            text="Cycle unique",
            command=self.single_cycle,
            font=('Arial', 12),
            bg='#FF9800',
            fg='white',
            padx=20,
            pady=10
        )
        self.step_button.pack(side=tk.LEFT, padx=10)
    
    def update_display(self):
        """Met à jour l'affichage graphique selon l'état actuel."""
        
        # Mise à jour de la chambre A
        if self.environment.is_room_a_dirty():
            self.room_a_frame.configure(bg='#ffcccc')  # Rouge clair
            self.room_a_status.configure(text="SALE", bg='#ffcccc', fg='#cc0000')
        else:
            self.room_a_frame.configure(bg='#ccffcc')  # Vert clair
            self.room_a_status.configure(text="PROPRE", bg='#ccffcc', fg='#006600')
        
        # Mise à jour de la chambre B
        if self.environment.is_room_b_dirty():
            self.room_b_frame.configure(bg='#ffcccc')  # Rouge clair
            self.room_b_status.configure(text="SALE", bg='#ffcccc', fg='#cc0000')
        else:
            self.room_b_frame.configure(bg='#ccffcc')  # Vert clair
            self.room_b_status.configure(text="PROPRE", bg='#ccffcc', fg='#006600')
        
        # Affichage de la position de l'agent
        if self.agent.get_position() == 'A':
            self.room_a_agent.configure(text="🤖", bg=self.room_a_frame.cget('bg'))
            self.room_b_agent.configure(text="", bg=self.room_b_frame.cget('bg'))
        else:
            self.room_a_agent.configure(text="", bg=self.room_a_frame.cget('bg'))
            self.room_b_agent.configure(text="🤖", bg=self.room_b_frame.cget('bg'))
        
        # Mise à jour des informations
        state = self.environment.get_state()
        info_text = f"Position: Chambre {self.agent.get_position()} | "
        info_text += f"État A: {state['A']} | État B: {state['B']}"
        self.info_label.configure(text=info_text)
        
        self.cycle_label.configure(text=f"Cycle : {self.cycle_count}")
    
    def single_cycle(self):
        """Exécute un seul cycle de simulation."""
        if not self.is_running:
            self.execute_cycle()
    
    def execute_cycle(self):
        """Exécute un cycle d'observation et d'action."""
        self.cycle_count += 1
        
        # L'agent observe et agit
        action = self.agent.act(self.environment)
        
        # Après l'action de l'agent, l'autre chambre peut se salir
        # Si l'agent vient de nettoyer A, B peut se salir pendant ce temps (ou vice versa)
        if "Nettoyage de la chambre A" in action:
            # L'agent a nettoyé A, B peut se salir pendant ce temps
            if not self.environment.is_room_b_dirty():
                self.environment.make_room_b_dirty()
        elif "Nettoyage de la chambre B" in action:
            # L'agent a nettoyé B, A peut se salir pendant ce temps
            if not self.environment.is_room_a_dirty():
                self.environment.make_room_a_dirty()
        
        # Mise à jour de l'affichage
        self.update_display()
        
        # Affichage de l'action dans la console (optionnel)
        print(f"Cycle {self.cycle_count}: {action}")
    
    def start_simulation(self):
        """Démarre la simulation automatique."""
        self.is_running = True
        self.start_button.configure(state=tk.DISABLED)
        self.stop_button.configure(state=tk.NORMAL)
        self.step_button.configure(state=tk.DISABLED)
        
        # Lancer la simulation dans un thread séparé pour ne pas bloquer l'interface
        threading.Thread(target=self.simulation_loop, daemon=True).start()
    
    def stop_simulation(self):
        """Arrête la simulation automatique."""
        self.is_running = False
        self.start_button.configure(state=tk.NORMAL)
        self.stop_button.configure(state=tk.DISABLED)
        self.step_button.configure(state=tk.NORMAL)
    
    def simulation_loop(self):
        """Boucle de simulation automatique."""
        while self.is_running:
            self.execute_cycle()
            # Attente de 2 secondes (simulation accélérée : 2 secondes = 2 minutes)
            time.sleep(2)
    
    def reset_simulation(self):
        """Réinitialise la simulation."""
        self.stop_simulation()
        self.cycle_count = 0
        self.environment = Environment(room_a_dirty=True, room_b_dirty=True)
        self.agent = VacuumAgent(initial_position='A')
        self.update_display()


def main():
    """Fonction principale pour lancer la démonstration."""
    root = tk.Tk()
    app = VacuumDemo(root)
    root.mainloop()


if __name__ == "__main__":
    main()

