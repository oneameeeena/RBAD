# RBAD
Developed a full-stack role-based admin dashboard with secure authentication, protected routes, and user management using React and Laravel.


📘 Cahier des Charges
🖥️ Projet : Role-Based Admin Dashboard

Stack: React + Laravel + MySQL

1️⃣ Contexte du projet

Ce projet consiste à développer une application web avec un système d’authentification et de gestion des rôles permettant de contrôler l’accès aux fonctionnalités selon le type d’utilisateur.

L’objectif est de créer un tableau de bord administratif professionnel similaire aux systèmes utilisés en entreprise.

2️⃣ Objectifs

Implémenter une authentification sécurisée

Mettre en place un système de rôles (Admin / User)

Gérer les utilisateurs

Protéger les routes selon les permissions

Afficher des statistiques dans un dashboard

3️⃣ Périmètre fonctionnel
🔐 3.1 Authentification

Inscription

Connexion

Déconnexion

Hash des mots de passe

Auth via Laravel Sanctum ou JWT

👤 3.2 Gestion des rôles

Deux rôles :

🟢 Admin

Voir tous les utilisateurs

Modifier utilisateur

Supprimer utilisateur

Changer rôle

Bannir utilisateur

Voir statistiques globales

🔵 User

Modifier son profil

Voir son dashboard personnel

Consulter ses informations

📊 3.3 Dashboard
Admin Dashboard :

Nombre total d’utilisateurs

Nombre d’utilisateurs actifs

Nombre d’utilisateurs bannis

Graphique simple (ex: évolution inscriptions)

User Dashboard :

Informations personnelles

Statut du compte

4️⃣ Exigences techniques
Backend (Laravel)

API REST

Middleware pour rôles

Policies ou Gates

Validation des requêtes

Architecture propre (Controllers, Services optionnel)

Base de données
users

id

name

email

password

role (admin / user)

status (active / banned)

timestamps

Frontend (React)

React Router

Axios

Protected routes

Redirection selon rôle

UI propre (Tailwind recommandé)

5️⃣ Exigences non fonctionnelles

Sécurité des routes

Validation côté frontend & backend

Gestion des erreurs

Code structuré et lisible

README professionnel

6️⃣ Architecture générale

Frontend (React)
↓
API REST (Laravel)
↓
Base de données MySQL

7️⃣ Livrables attendus

Code source GitHub

README détaillé

Screenshots du dashboard

Schéma base de données

Description pour CV

8️⃣ Planning estimatif
Tâche	Durée
Setup backend + auth	1 jour
Gestion rôles + middleware	1 jour
Frontend layout	1 jour
Dashboard + stats	1 jour
Testing + README	1 jour

Durée totale estimée : 4–5 jours
