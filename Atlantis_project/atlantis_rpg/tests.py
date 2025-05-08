from django.test import TestCase
from .models import Player

class PlayerModelTest(TestCase):
    def test_player_creation(self):
        player = Player.objects.create(
            name="Test Adventurer",
            health=100,
            location="Atlantis Gate",
            inventory=[]
        )
        self.assertEqual(player.name, "Test Adventurer")
        self.assertEqual(player.health, 100)
        self.assertEqual(player.location, "Atlantis Gate")
        self.assertEqual(player.inventory, [])
