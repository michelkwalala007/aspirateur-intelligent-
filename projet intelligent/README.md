# 🧹 Agent Aspirateur Intelligent  
## Projet d’Intelligence Artificielle

## Présentation du projet

Ce projet a été réalisé dans le cadre du cours d’**Intelligence Artificielle**.  
Il consiste à simuler un **agent aspirateur intelligent à réflexe simple** capable de nettoyer deux chambres (A et B) en fonction de leur état (sale ou propre).

L’objectif est de comprendre comment un agent peut **observer son environnement**, **prendre une décision simple** et **agir automatiquement**, sans apprentissage ni mémoire complexe.

---

## Objectifs du projet

- Implémenter un agent à réflexe simple
- Simuler un environnement avec deux chambres
- Visualiser le comportement de l’agent
- Mettre en pratique les notions vues au cours
- Présenter un projet fonctionnel et compréhensible sur GitHub

---

## Type d’agent

L’agent utilisé est un **agent à réflexe simple**.

Caractéristiques :
- Pas d’apprentissage
- Pas de mémoire avancée
- Décisions basées uniquement sur l’état actuel
- Comportement déterministe basé sur des règles simples

---

## Description de l’environnement

L’environnement est composé de deux chambres :
- **Chambre A**
- **Chambre B**

Chaque chambre peut être :
- *sale*
- *propre*

L’agent peut :
- se déplacer entre les chambres
- nettoyer la chambre où il se trouve
- attendre si aucune action n’est nécessaire

---

## Règles de comportement de l’agent

L’agent applique les règles suivantes :

1. **Si les deux chambres sont sales**  
   → Il nettoie d’abord la chambre où il se trouve, puis se déplace vers l’autre chambre.

2. **Si une seule chambre est sale**  
   → Il se déplace vers cette chambre (si nécessaire) et la nettoie.

3. **Si les deux chambres sont propres**  
   → L’agent attend.

---

## Cycle de fonctionnement

À chaque cycle (toutes les **2 minutes** en temps réel ou **2 secondes** en temps simulé) :

1. L’agent observe l’état des chambres
2. Il décide de l’action à effectuer
3. Il exécute l’action (nettoyage, déplacement ou attente)

---

## Structure du projet

