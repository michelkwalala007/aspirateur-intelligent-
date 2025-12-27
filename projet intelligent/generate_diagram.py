"""
Script pour générer le diagramme du fonctionnement de l'agent.
Génère un fichier diagramme.png avec un organigramme simple.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Création de la figure
fig, ax = plt.subplots(1, 1, figsize=(10, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Couleurs
box_color = '#e3f2fd'
decision_color = '#fff9c4'
action_color = '#c8e6c9'

# Fonction pour créer une boîte
def create_box(x, y, width, height, text, color=box_color, shape='rect'):
    if shape == 'rect':
        box = mpatches.Rectangle((x, y), width, height, 
                                 facecolor=color, edgecolor='black', linewidth=1.5)
    elif shape == 'diamond':
        box = mpatches.RegularPolygon((x + width/2, y + height/2), 4, 
                                     radius=width/2, orientation=0.785,
                                     facecolor=color, edgecolor='black', linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, ha='center', va='center', 
            fontsize=9, weight='bold', wrap=True)

# Fonction pour créer une flèche
def create_arrow(x1, y1, x2, y2, label=''):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x, mid_y, label, ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8),
                fontsize=8)

# Titre
ax.text(5, 11.5, "Organigramme du Fonctionnement de l'Agent Aspirateur", 
        ha='center', va='center', fontsize=14, weight='bold')

# Début
create_box(4, 10, 2, 0.6, "DÉBUT", action_color)
create_arrow(5, 10, 5, 9.5)

# Observation
create_box(3.5, 9, 3, 0.6, "OBSERVATION\nÉtat des chambres A et B", box_color)
create_arrow(5, 9, 5, 8.5)

# Décision : Les deux chambres sont sales ?
create_box(3.5, 7.5, 3, 1.2, "Les deux\nchambres\nsont sales ?", decision_color, 'diamond')
create_arrow(5, 7.5, 5, 7)

# Oui : Nettoyer chambre actuelle
create_box(1, 5.5, 2.5, 0.8, "Nettoyer chambre\noù se trouve\nl'agent", action_color)
create_arrow(4.25, 7.5, 2.25, 6.3, "Oui")

# Déplacer vers l'autre chambre
create_box(1, 4.5, 2.5, 0.8, "Déplacer vers\nl'autre chambre", action_color)
create_arrow(2.25, 4.5, 2.25, 4)

# Non : Décision suivante
create_box(6.5, 7.5, 2.5, 0.8, "Une seule\nchambre\nest sale ?", decision_color, 'diamond')
create_arrow(5.75, 7.5, 6.75, 7.5, "Non")

# Oui : Se déplacer vers la chambre sale
create_box(6.5, 5.5, 2.5, 0.8, "Se déplacer vers\nla chambre sale", action_color)
create_arrow(7.75, 7.5, 7.75, 6.3, "Oui")

# Nettoyer la chambre sale
create_box(6.5, 4.5, 2.5, 0.8, "Nettoyer la\nchambre sale", action_color)
create_arrow(7.75, 4.5, 7.75, 4)

# Non : Les deux sont propres
create_box(6.5, 3, 2.5, 0.8, "Les deux\nchambres\nsont propres", action_color)
create_arrow(7.75, 7.5, 7.75, 3.8, "Non")

# Attendre
create_box(3.5, 2, 3, 0.6, "ATTENDRE", action_color)
create_arrow(5, 3, 5, 2.6)
create_arrow(2.25, 4, 3.5, 2.3)
create_arrow(7.75, 4, 6.5, 2.3)

# Fin
create_box(4, 1, 2, 0.6, "FIN", action_color)
create_arrow(5, 2, 5, 1.6)

# Légende
legend_elements = [
    mpatches.Patch(facecolor=box_color, edgecolor='black', label='Observation'),
    mpatches.Patch(facecolor=decision_color, edgecolor='black', label='Décision'),
    mpatches.Patch(facecolor=action_color, edgecolor='black', label='Action')
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=9)

# Sauvegarde
plt.tight_layout()
plt.savefig('diagramme.png', dpi=150, bbox_inches='tight')
print("Diagramme généré : diagramme.png")

