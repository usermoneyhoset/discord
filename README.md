# Selfbot Discord — RPC "Mon shop"

Selfbot Discord complet avec RPC personnalisée et bouton d'accès au shop.

## 📋 Installation rapide

### 1. Prérequis
- Python 3.10+
- pip installé

### 2. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 3. Configuration
Ouvrez `config.json` et remplissez vos paramètres:
```json
{
  "token": "VOTRE_TOKEN_DISCORD_ICI",
  "shop_image_url": "https://votre-image.com/shop.png",
  "shop_link": "https://darknorth.fr"
}
```

**Où obtenir votre token Discord?**
1. Ouvrez Discord (client desktop)
2. Appuyez sur `Ctrl+Shift+I` (DevTools)
3. Allez dans l'onglet Console
4. Collez: `window.localStorage.token.replace(/"/g,'')`
5. Copiez le résultat dans `config.json`

> ⚠️ **Garde ton token secret — ne le partage jamais!**

### 4. Lancement
```bash
python selfbot_rpc.py
```

La RPC se mettra à jour automatiquement toutes les minutes.

---

## 🎮 Commandes disponibles

| Commande | Effet |
|----------|-------|
| `!rpc` | Affiche le shop avec bouton cliquable |
| `!rpc-status` | Change le statut personnalisé |
| `!rpc-stop` | Arrête la RPC |

Tapez ces commandes dans n'importe quel serveur ou DM — seul le selfbot les verra.

---

## 📝 Configuration personnalisée

### Changer l'image
Remplacez `shop_image_url` dans `config.json` par une URL valide:
- Service gratuit: https://imgur.com (upload → copier le lien)
- Hébergement personnel: votre propre serveur

### Changer le lien du shop
Modifiez `shop_link` — n'importe quel URL valide fonctionne.

### Changer le texte de la RPC
Éditez la ligne dans `selfbot_rpc.py`:
```python
name="Mon shop",  # Texte principal
state="🛍️ Découvrez nos produits",  # Texte secondaire
```

---

## 🔧 Dépannage

**"Token invalide"**
→ Vérifiez que votre token dans `config.json` est correct (sans guillemets)

**"config.json non trouvé"**
→ Assurez-vous que `config.json` est dans le même dossier que `selfbot_rpc.py`

**Les commandes ne marchent pas**
→ Tapez-les en tant que l'utilisateur auquel appartient le token. Les selfbots ne répondent qu'à leurs propres messages.

---

## ⚠️ Notes de sécurité

- Garde ton token secret — quiconque le possède contrôle ton compte
- Ne pushe jamais `config.json` sur GitHub (les tokens y sont en clair)
- Les selfbots contreviennent aux conditions d'utilisation Discord — utilise à tes risques

---

## 📦 Contenu du zip

```
selfbot_rpc/
├── selfbot_rpc.py       # Code principal
├── config.json          # Configuration (à remplir)
├── requirements.txt     # Dépendances
├── README.md            # Ce fichier
└── .gitignore           # Ignore config.json sur Git
```

---

Bon surf! 🛍️
