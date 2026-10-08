#!/usr/bin/env python3
# language: Python 3.10+, file: selfbot_rpc.py
# discord.py==2.0+

import discord
from discord.ext import tasks
from discord import Embed, ui, Interaction
import json
import os
from pathlib import Path

# ===== CONFIG LOADER =====
def load_config():
    config_path = Path(__file__).parent / "config.json"
    if not config_path.exists():
        print(f"❌ config.json non trouvé. Crée-le avec vos paramètres.")
        return None
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

CONFIG = load_config()
if not CONFIG:
    exit(1)

TOKEN = CONFIG.get("token")
SHOP_IMAGE_URL = CONFIG.get("shop_image_url", "https://via.placeholder.com/500")
SHOP_LINK = CONFIG.get("shop_link", "https://darknorth.fr")

if not TOKEN:
    print("❌ Token Discord manquant dans config.json")
    exit(1)

# ===== SHOP BUTTON =====
class ShopButton(ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @ui.button(label="Ouvrir le shop", style=discord.ButtonStyle.blurple, emoji="🛍️")
    async def shop_button(self, interaction: Interaction, button: ui.Button):
        embed = Embed(
            title="Redirection",
            description=f"[Cliquez ici pour accéder au shop]({SHOP_LINK})",
            color=discord.Color.blue()
        )
        embed.set_image(url=SHOP_IMAGE_URL)
        await interaction.response.send_message(embed=embed, ephemeral=True)

# ===== SELFBOT =====
class SelfbotRPC(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        print(f"✓ Connecté en tant que {self.user}")
        if not self.synced:
            self.update_rpc.start()
            self.synced = True

    @tasks.loop(minutes=1)
    async def update_rpc(self):
        """Met à jour la RPC toutes les minutes"""
        if not self.is_ready():
            return
        try:
            activity = discord.Activity(
                type=discord.ActivityType.custom,
                name="🛍️ Mon shop",
                state="Découvrez nos produits"
            )
            await self.change_presence(activity=activity)
        except Exception as e:
            print(f"⚠️ Erreur RPC: {e}")

    async def on_message(self, message):
        """Écoute les commandes utilisateur"""
        if message.author.id != self.user.id:
            return

        if message.content == "!rpc":
            embed = Embed(
                title="Mon shop",
                description="Bienvenue dans notre boutique!",
                color=discord.Color.purple()
            )
            embed.set_image(url=SHOP_IMAGE_URL)
            embed.set_footer(text="Cliquez le bouton pour accéder au shop")
            
            view = ShopButton()
            await message.channel.send(embed=embed, view=view)
            await message.delete()

        if message.content == "!rpc-status":
            await self.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.custom,
                    name="✨ À l'écoute",
                    state="Consultez mon shop"
                )
            )
            await message.add_reaction("✓")

        if message.content == "!rpc-stop":
            await self.change_presence(activity=None)
            await message.add_reaction("⏹️")

# ===== LANCEMENT =====
if __name__ == "__main__":
    client = SelfbotRPC()
    try:
        print("🚀 Démarrage du selfbot...")
        client.run(TOKEN)
    except discord.errors.LoginFailure:
        print("❌ Token invalide. Vérifiez config.json")
    except Exception as e:
        print(f"❌ Erreur: {e}")
