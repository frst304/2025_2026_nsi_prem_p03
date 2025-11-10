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

🧾 Créer un compte en entrant son nom et sa date de naissance (un code PIN lui sera attribué) ;

🔐 S’authentifier avec un code PIN existant ;

💰 Consulter le solde de son compte ;

💸 Retirer ou déposer de l’argent ;

🚪 Quitter le programme proprement.

🖥️ Tout se fait directement dans le terminal (aucune interface graphique).

👤 Étape 1 – Connexion ou Création de compte

Au démarrage, le programme affiche :

=== Distributeur Automatique de Billets ===
1. Se connecter avec un code PIN existant
2. Créer un nouveau compte
Choix :

🆕 Création d’un nouveau compte

Si vous choisissez l’option 2, le programme vous demandera :

Entrez votre nom :
Entrez votre date de naissance (JJ/MM/AAAA) :


Ensuite, un code PIN personnel est généré automatiquement :

Votre compte a été créé avec succès !
Votre code PIN est : 4729
Gardez-le précieusement pour vos prochaines connexions.


💶 Le compte démarre avec un solde initial de 0 €.

🔐 Connexion à un compte existant

Si vous choisissez 1 – Se connecter, le programme demande :

Entrez votre code PIN :


✅ En cas de code correct → accès au menu principal.

❌ En cas d’erreur → message d’erreur et nouvelle demande.

📋 Étape 2 – Menu Principal

Une fois connecté, le menu suivant apparaît :

=== MENU PRINCIPAL ===
1. Consulter le solde
2. Retirer de l’argent
3. Déposer de l’argent
4. Quitter


👉 Tapez le numéro correspondant à l’action que vous souhaitez effectuer.

💰 Fonctionnalités Détailées
1️⃣ Consulter le solde

Affiche le solde actuel du compte :

Votre solde actuel est de : 850 €

2️⃣ Retirer de l’argent
Entrez le montant à retirer :


Le programme vérifie que le montant :

💵 est disponible sur le compte ;

🔢 est un multiple de 5 ;

🧩 peut être décomposé en billets (50€, 20€, 10€, 5€).

Exemple :

Retrait de 85 € effectué avec succès.
Billets distribués : 1x50€, 1x20€, 1x10€, 1x5€
Nouveau solde : 765 €

3️⃣ Déposer de l’argent
Entrez le montant à déposer :


Exemple :

Dépôt de 200 € effectué.
Nouveau solde : 965 €

4️⃣ Quitter
Tapez 4 pour quitter.


💬 Message de sortie :

Merci d’avoir utilisé notre DAB. À bientôt !


Le programme se ferme proprement ✅

🧠 Astuces

Conservez votre code PIN en lieu sûr 🔒

Vérifiez toujours votre solde avant un retrait 💼

Les montants doivent être multiples de 5 pour le retrait 💶