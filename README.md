# 🚀 Équipe NSI Prem P03 - 2025/2026

Voici la team avec nos pseudos GitHub :

| Prénom  | Pseudo GitHub    |
|---------|------------------|
| Timothee | `timothee.chps`  |
| Haron    | `HaronElmz`      |
| Victor   | `frst_304`       |


🏦 Manuel Utilisateur – Simulateur de Distributeur Automatique de Billets (DAB)
📘 Description

Ce programme simule le fonctionnement d’un distributeur automatique de billets (DAB).
Il permet à un utilisateur de :

Créer un compte en entrant son nom et sa date de naissance (un code PIN lui sera attribué) ;

S’authentifier avec un code PIN déjà existant ;

Consulter le solde de son compte ;

Retirer et déposer de l’argent ;

Quitter le programme proprement.

Tout se fait dans le terminal (aucune interface graphique).

⚙️ Prérequis

Python 3.x installé sur votre ordinateur.

Le fichier du programme dab.py (fourni par le développeur).

🚀 Lancement du programme

Ouvrez un terminal ou une invite de commandes.

Placez-vous dans le dossier contenant le fichier dab.py.

Exécutez le programme avec :

python dab.py

👤 Étape 1 – Connexion ou Création de compte

Au démarrage, le programme vous propose deux choix :

=== Distributeur Automatique de Billets ===
1. Se connecter avec un code PIN existant
2. Créer un nouveau compte
Choix :

🆕 Si vous choisissez 2 – Créer un nouveau compte

Le programme vous demandera :

Entrez votre nom : 
Entrez votre date de naissance (JJ/MM/AAAA) :


Ensuite, il génère automatiquement un code PIN personnel (affiché à l’écran), par exemple :

Votre compte a été créé avec succès !
Votre code PIN est : 4729
Gardez-le précieusement pour vos prochaines connexions.


Le compte démarre avec un solde initial de 0 €.

🔐 Si vous choisissez 1 – Se connecter

Le programme demande :

Entrez votre code PIN :


Si le code est correct, vous accédez au menu principal.

En cas d’erreur, le programme affiche un message d’erreur et redemande le code.

📋 Étape 2 – Menu Principal

Une fois connecté, le menu suivant s’affiche :

=== MENU PRINCIPAL ===
1. Consulter le solde
2. Retirer de l’argent
3. Déposer de l’argent
4. Quitter


👉 Tapez le numéro correspondant à l’action que vous souhaitez effectuer.

💰 Fonctionnalités
1️⃣ Consulter le solde

Affiche le solde actuel du compte :

Votre solde actuel est de : 850 €

2️⃣ Retirer de l’argent

Saisissez le montant souhaité :

Entrez le montant à retirer : 


Le programme vérifie que le montant :

est disponible sur le compte ;

est un multiple de 5 ;

peut être décomposé en billets (50€, 20€, 10€, 5€).

Exemple :

Retrait de 85 € effectué avec succès.
Billets distribués : 1x50€, 1x20€, 1x10€, 1x5€
Nouveau solde : 765 €

3️⃣ Déposer de l’argent

Entrez le montant à déposer :

Entrez le montant à déposer :


Le solde est mis à jour :

Dépôt de 200 € effectué.
Nouveau solde : 965 €

4️⃣ Quitter

Tapez 4 pour quitter :

Merci d’avoir utilisé notre DAB. À bientôt !


Le programme se ferme proprement.



