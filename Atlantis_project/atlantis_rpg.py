import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atlantis_project.settings')
import django
django.setup()
from atlantis_rpg.game import AtlantisGame

if __name__ == "__main__":
    player_name = input("Enter your adventurer's name: ")
    game = AtlantisGame(player_name)
    game.play()
