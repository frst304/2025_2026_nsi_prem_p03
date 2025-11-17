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

Au début, lors du premier cours, nous avons commencé à travailler tous ensemble sur nos ordinateurs sur le menu principal du programme. Très vite, nous avons constaté que cette méthode n’était pas efficace : à la fin du cours, nous devions supprimer beaucoup de contenu à cause de conflits entre nos codes respectifs.

Nous avons alors changé de stratégie : chacun s’est réparti les fonctions à développer de son côté, puis nous avons intégré nos travaux une fois terminés. Cette méthode nous a permis de progresser semaine après semaine.

Cependant, certaines parties ont dû être refaites, car certaines fonctions s’appelaient entre elles, provoquant des dysfonctionnements. Après avoir corrigé ces problèmes, nous avons pu avancer vers la finalisation du projet.

Tâches restantes

Il nous restait trois tâches importantes à accomplir :

1 -Faire en sorte que les opérations de retrait et de dépôt modifient réellement le programme.

2 -Commenter le code pour le rendre plus compréhensible.

3 -Rédiger le fichier README.

Nous nous sommes réparti ces tâches :

Victor : ajout de fonctionnalités supplémentaires, comme l’échange d’argent entre utilisateurs.

Haron : amélioration de l’interface graphique.

Timothée : correction et optimisation des subtilités du code.

Ainsi s’est déroulé notre projet en Python, dont l’objectif était de coder une banque pour trois utilisateurs.