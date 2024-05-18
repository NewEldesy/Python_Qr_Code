# Générateur de QR Code

Ce programme permet de générer et de lire des codes QR à partir de texte.

## Installation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Installez les dépendances nécessaires en exécutant la commande suivante :
    ```
    pip install opencv-python-headless qrcode PyQt5
    ```

## Utilisation

1. Exécutez le programme en exécutant la commande suivante dans votre terminal :
    ```
    python qr_code_generator.py
    ```
2. L'interface utilisateur s'ouvrira, vous permettant de charger, générer et lire des codes QR.

## Fonctionnalités

- **Chargement d'une image**: Permet de charger une image existante pour la lecture d'un code QR.
- **Sauvegarde d'une image**: Permet de sauvegarder un code QR généré dans un fichier PNG.
- **Génération de code QR**: Génère un code QR à partir du texte saisi dans l'éditeur de texte.
- **Lecture de code QR**: Lit un code QR à partir de l'image actuellement chargée.
- **Actualisation des champs**: Efface le texte saisi et l'image affichée.
- **Quitter**: Ferme l'application.

## Auteur

Ce code a été écrit par [Ramel MAKOSSO].