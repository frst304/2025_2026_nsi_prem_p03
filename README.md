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

🧾 Créer un compte en entrant son nom et son âge et en choisissant un mot de passe ;

🔐 S’authentifier avec un code PIN existant ;

💰 Consulter le solde de son compte ;

💸 Retirer ou déposer de l’argent ;

🚪 Quitter le programme proprement.

🖥️ Tout se fait directement dans le terminal (aucune interface graphique).

👤 Étape 1 – Connexion ou Création de compte

Au démarrage, le programme affiche :

=== Bienvenue ===
[1] Ancien utilisateur  
[2] Nouvel utilisateur  
[q] Quitter le programme
Choix :

🆕 Nouvel utilisateur 

Si vous choisissez l’option 2, le programme vous demandera :

Entrez votre nom complet:
Entrez votre âge  :
Choisissez un mot de passe :

Ensuite, un identifiant est généré automatiquement avec votre nom:

Compte créé avec succès. Votre identifiant est : a.ardaguller



💶 Le compte démarre avec un solde initial de 0 €.

🔐 Ancien utilisateur

Si vous choisissez 1 – Ancien utilisateur, le programme demande :

Entrez votre identifiant :
Puis votre mot de passe :


✅ En cas de code correct → accès au menu principal.

❌ En cas d’erreur → message d’erreur et nouvelle demande.

📋 Étape 2 – Menu Principal

Une fois connecté, le menu suivant apparaît :

=== Bienvenue haron elmounzil ===
[1] Voir son solde  
[2] Retirer de l'argent 
 [3] Ajouter de l'argent 
 [q] Quitter le programme

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

4)Quitter
Tapez q pour quitter.


💬 Message de sortie :

Merci d’avoir utilisé notre DAB. À bientôt !


Le programme se ferme proprement ✅

🧠 Astuces

Conservez votre code PIN en lieu sûr 🔒

Vérifiez toujours votre solde avant un retrait 💼

Les montants doivent être multiples de 5 pour le retrait 💶