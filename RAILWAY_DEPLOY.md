# Déployer sur Railway (GRATUIT)

Railway: $5 crédit gratuit/mois — plus que suffisant pour un selfbot.

## 📋 Étapes

### 1. Créer un repo GitHub
- Va sur https://github.com/new
- Crée un repo `selfbot-rpc` (public ou privé, peu importe)
- Clone-le en local

### 2. Copie les fichiers dedans
```bash
# Dans le dossier du repo git
cp -r ../selfbot_rpc/* .
```

Commit et push:
```bash
git add .
git commit -m "Initial selfbot setup"
git push
```

**IMPORTANT:** `config.json` avec ton token est en local SEULEMENT. Pas sur GitHub.

### 3. Créer le compte Railway
- Va sur https://railway.app
- Sign up avec GitHub (plus facile)
- Autorise Railway à accéder à tes repos

### 4. Déployer le projet
1. Dans Railway, clique "New Project"
2. Sélectionne "Deploy from GitHub"
3. Choisis ton repo `selfbot-rpc`
4. Railway détecte le `requirements.txt` automatiquement

### 5. Ajouter le token en ENV
Railway doit avoir ton token SANS le mettre sur GitHub:

1. Dans le dashboard Railway, va dans "Variables"
2. Ajoute: `DISCORD_TOKEN` = `TON_TOKEN_ICI`
3. Modifie `config.json` pour lire depuis l'env:

**Nouveau config.json:**
```json
{
  "token": "DISCORD_TOKEN",
  "shop_image_url": "https://cdn.discordapp.com/attachments/...",
  "shop_link": "https://darknorth.fr"
}
```

**Nouveau code dans selfbot_rpc.py** (avant load_config):
```python
import os

def load_config():
    # D'abord essayer les env vars, sinon config.json
    token = os.getenv("DISCORD_TOKEN")
    if token:
        return {
            "token": token,
            "shop_image_url": os.getenv("SHOP_IMAGE_URL", "https://..."),
            "shop_link": os.getenv("SHOP_LINK", "https://darknorth.fr")
        }
    
    # Fallback: config.json local
    config_path = Path(__file__).parent / "config.json"
    if not config_path.exists():
        print(f"❌ config.json non trouvé.")
        return None
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)
```

### 6. Déployer
- Railway détecte les changements GitHub automatiquement
- Clique "Deploy"
- Attends ~2 min
- Statut "Active" = c'est live

### 7. Vérifier que ça tourne
Dans Railway, onglet "Logs" — tu dois voir:
```
✓ Connecté en tant que [TonUsername]
```

---

## 🔧 Coûts & Limites

- **Gratuit:** $5 crédit/mois
- **Selfbot léger:** ~$0.50/mois (un selfbot simple)
- **Suffisant pour:** 10 selfbots easy

Si tu dépasses, Railway te facture juste le surplus (très cheap).

---

## 🚨 Troubleshoot

**"Token invalide"**
→ Vérifie la variable `DISCORD_TOKEN` dans Railway

**"Logs vides"**
→ Redéploie manuellement ou pousse une modif GitHub

**Le selfbot pas actif après 30min**
→ Railway ne stop pas les apps, tu es bon

---

## Alternative: PythonAnywhere (zéro crédit)

Si tu veux 100% gratuit sans crédit:

1. https://www.pythonanywhere.com
2. Crée un compte gratuit
3. Crée une "Scheduled task" Python
4. Copie le code du selfbot dedans
5. Schedule: run toutes les heures

C'est moins fluide que Railway mais gratuit illimité.

---

C'est bon, tu as Railway avec le crédit gratuit?
