<img width="887" height="241" alt="ascii-art-text" src="https://github.com/user-attachments/assets/dd232f9d-87b0-4894-86a1-8a08a5b219ce" />

# 🚀 Équipe NSI Prem P03 – 2025/2026

### 👥 Membres de l’équipe

| Prénom   | Pseudo GitHub    |
|-----------|------------------|
| Timothée | `timothee.chps` |
| Haron     | `HaronElmz`     |
| Victor    | `frst_304`      |

---

# 🏦 Manuel Utilisateur – Simulateur de Distributeur Automatique de Billets (DAB)

## 📘 Description

Ce programme simule le fonctionnement d’un **distributeur automatique de billets (DAB)**.  
Il permet à un utilisateur de :

- 🧾 **Créer un compte** (nom, âge, mot de passe)
- 🔐 **S’authentifier** avec un identifiant et un mot de passe
- 💰 **Consulter le solde** de son compte
- 💸 **Retirer ou déposer de l’argent**
- 🚪 **Quitter le programme proprement**

> 🖥️ Tout se fait directement dans le **terminal** (aucune interface graphique).

---

## 👤 Étape 1 – Connexion ou Création de compte

Au démarrage, le programme affiche :

```text
=== Bienvenue ===
[1] Ancien utilisateur  
[2] Nouvel utilisateur  
[q] Quitter le programme
Choix :
```

### 🆕 Nouvel utilisateur

Si vous choisissez l’option **2**, le programme vous demandera :

```text
Entrez votre nom complet :
Entrez votre âge :
Choisissez un mot de passe :
```

Ensuite, un identifiant est généré automatiquement à partir de votre nom :

```text
Compte créé avec succès. Votre identifiant est : a.ardaguller
```

💶 Le compte démarre avec un **solde initial de 0 €**.

---

### 🔐 Ancien utilisateur

Si vous choisissez **1 – Ancien utilisateur**, le programme demande :

```text
Entrez votre identifiant :
Entrez votre mot de passe :
```

✅ En cas de code correct → accès au **menu principal**.  
❌ En cas d’erreur → message d’erreur et nouvelle demande.

---

## 📋 Étape 2 – Menu Principal

Une fois connecté, le menu suivant apparaît :

```text
=== Bienvenue haron elmounzil ===
[1] Voir son solde  
[2] Retirer de l'argent  
[3] Ajouter de l'argent  
[q] Quitter le programme
```

👉 Tapez le numéro correspondant à l’action souhaitée.

---

## 💰 Fonctionnalités détaillées

### 1️⃣ Consulter le solde

Affiche le solde actuel du compte :

```text
Votre solde actuel est de : 850 €
```

### 2️⃣ Retirer de l’argent

Le programme demande :

```text
Entrez le montant à retirer :
```

Le programme vérifie que le montant :

- 💵 est **disponible sur le compte** ;
- 🔢 est un **multiple de 5** ;
- 🧩 peut être **décomposé en billets** (50€, 20€, 10€, 5€).

**Exemple :**

```text
Retrait de 85 € effectué avec succès.
Billets distribués : 1x50€, 1x20€, 1x10€, 1x5€
Nouveau solde : 765 €
```

### 3️⃣ Déposer de l’argent

```text
Entrez le montant à déposer :
```

**Exemple :**

```text
Dépôt de 200 € effectué.
Nouveau solde : 965 €
```

### 4️⃣ Quitter

Tapez `q` pour quitter.

💬 **Message de sortie :**

```text
Merci d’avoir utilisé notre DAB. À bientôt !
```

Le programme se ferme **proprement ✅**

---

## 🧠 Astuces

- 🔒 Conservez votre **code PIN** à l'abris des regards 
- 💼 Vérifiez toujours votre **solde avant un retrait**  
- 💶 Les montants doivent être **multiples de 5** pour le retrait


## Histoire du projet

Lors de notre tout premier cours, nous avons commencé à travailler ensemble sur le menu principal de notre programme. Chacun d’entre nous a ouvert son ordinateur, et nous avons commencé à coder simultanément, partageant nos écrans pour avancer le plus rapidement possible. Cependant, très vite, nous avons constaté que cette approche n’était pas vraiment efficace. En fin de séance, il y avait de nombreux conflits entre nos codes respectifs, ce qui nous obligeait à supprimer une grande partie du contenu que nous avions créé, voire à recommencer certaines parties du programme. C'était frustrant, mais cela nous a permis de prendre du recul et de repenser notre stratégie de travail.

Nous avons donc décidé de changer de méthode. Plutôt que de travailler tous ensemble sur le même fichier en temps réel, nous avons opté pour une répartition des tâches. Chaque membre de l'équipe s'est vu attribuer une fonction spécifique à développer de son côté. Une fois que chacun avait terminé sa partie, nous avons procédé à l'intégration de nos travaux respectifs. Cette nouvelle organisation a bien fonctionné et nous a permis de progresser semaine après semaine, chacun avançant à son propre rythme tout en étant responsable d'une partie bien précise du projet.

Cependant, au bout de quelques semaines, nous avons rencontré un autre obstacle. Certaines de nos fonctions s’appelaient les unes les autres, ce qui a provoqué des dysfonctionnements dans le programme. C'était une situation un peu complexe à résoudre, mais après plusieurs heures de debugging ,de réflexion, et avec l'aide de notre professeur nous avons trouvé des solutions pour corriger ces problèmes. Grâce à cette expérience, nous avons appris l’importance de la planification et de l’organisation du code dès le début du projet. Une fois ces erreurs corrigées, nous avons pu avancer plus sereinement vers la finalisation du projet.

À une semaine de la présentation finale, il nous restait trois tâches importantes à accomplir pour être prêts à présenter notre application de banque :

Faire en sorte que les opérations de retrait et de dépôt modifient réellement le solde des comptes. Cela nous avait posé problème pendant les premières phases de développement, et il était essentiel de s'assurer que ces fonctionnalités soient parfaitement opérationnelles avant la présentation.

Commenter le code pour le rendre plus compréhensible. Dès le début du projet, nous savions qu’il était important de bien commenter le code afin de faciliter sa compréhension, aussi bien pour nous-mêmes que pour les autres qui pourraient être amenés à le lire ou à l'utiliser par la suite. Mais au fur et à mesure des semaines, nous avons souvent oublié de le faire au fur et à mesure de notre avancée. Finalement, nous avons décidé de prendre le temps, lors de la dernière phase du projet, pour ajouter des commentaires détaillés dans chaque fonction. Cela a permis de rendre notre code beaucoup plus clair et de nous assurer que toute l'équipe comprenait les choix techniques effectués.

Rédiger le fichier README. Cette étape était primordiale, car elle permettait de bien expliquer le fonctionnement du programme et d’informer les utilisateurs sur la manière de l’utiliser. Nous avons donc réparti cette tâche entre nous, en ajoutant à la fois des instructions d’utilisation, des explications sur l’architecture du code, et des indications sur les prérequis nécessaires pour faire tourner l’application.

Répartition des tâches :

Victor : Il s'est occupé de l'ajout de fonctionnalités supplémentaires, en particulier la gestion de l’échange d’argent entre utilisateurs. Cette fonctionnalité, qui n’était pas demandée dans le cahier des charges initial, a été ajoutée lors de notre dernier cours. Nous avons trouvé que cela apportait un réel plus à l'application, permettant aux utilisateurs d’envoyer de l'argent à leurs amis. C'était un défi technique intéressant, car il fallait gérer les transactions entre plusieurs comptes tout en respectant les règles de sécurité.

Haron : Sa tâche principale a été l’amélioration de l'interface graphique et la rédaction du readme

Timothée : Timothée s’est concentré sur la correction et l’optimisation du code. En plus de régler certains bugs persistants, il a procédé à des refactorisations pour rendre le code plus performant et éviter les redondances inutiles. Il a également été très impliqué dans la rédaction des commentaires pour chaque fonction, afin que notre programme soit plus lisible et facilement compréhensible.

Dernière ligne droite


Finalement, grâce à une bonne gestion du temps et  une répartition efficace des tâches, nous avons pu livrer notre projet dans les délais et avec une application de banque fonctionnelle et bien structurée. Le fait de commenter en continu le code et de vérifier màinutieusement chaque fonctionnalité avant la présentation nous a permis de terminer le projet dans de bonnes conditions, tout en ayant une bonne maîtrise de notre travail. C’était une expérience enrichissante qui nous a permis de travailler en équipe et d’approfondir nos compétences en programmation.



Ainsi s’est déroulé notre projet en Python, dont l’objectif était de coder une banque pour trois utilisateurs.