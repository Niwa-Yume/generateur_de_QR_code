# pyqr - Générateur de QR Code en Python

Ce projet est un générateur de QR code simple et efficace écrit en Python. Il permet de créer facilement des QR codes à partir de données textuelles.

## Fonctionnalités

- Génération de QR codes à partir de texte
- Personnalisation de la taille du QR code
- Sauvegarde du QR code en format PNG
- Interface en ligne de commande facile à utiliser

## Installation

Pour installer pyqr, assurez-vous d'avoir Python 3.6 ou supérieur installé, puis exécutez :

```bash
pip install pyqr
```
## Utilisation

Voici un exemple simple d'utilisation :

```python
from pyqr import generate_qr

# Générer un QR code
generate_qr("https://websim.ai", "mon_qr_code.png")

# Pour l'interface en ligne de commande :

python -m pyqr "Votre texte ici" -o qr_output.png
```
Pour plus d'informations, consultez la documentation complète ou rejoignez notre serveur Discord.

## Options

- `-s`, `--size` : Définir la taille du QR code (par défaut : 10)
- `-o`, `--output` : Spécifier le nom du fichier de sortie (par défaut : qr_code.png)

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Pour plus d'informations, consultez la documentation complète ou rejoignez notre serveur Discord.

