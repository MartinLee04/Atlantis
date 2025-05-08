from .models import Player, Narrative
import random
import time

class AtlantisGame:
    def __init__(self, player_name):
        self.player = self.initialize_player(player_name)
        self.narratives = self.load_narratives()

    def initialize_player(self, player_name):
        player, created = Player.objects.get_or_create(
            name=player_name,
            defaults={'health': 100, 'location': 'Atlantis Gate', 'inventory': []}
        )
        return player

    def load_narratives(self):
        narratives = [
            {
                'location': 'Atlantis Gate',
                'description': 'You stand before the shimmering Atlantis Gate, a portal to the lost city. The air hums with ancient energy.',
                'choices': {
                    'Enter the gate': 'Crystal Cavern',
                    'Search the surroundings': 'Atlantis Gate',
                    'Rest': 'Atlantis Gate'
                }
            },
            {
                'location': 'Crystal Cavern',
                'description': 'The cavern glows with bioluminescent crystals. A shadowy figure lurks in the distance.',
                'choices': {
                    'Approach the figure': 'Throne Room',
                    'Collect crystals': 'Crystal Cavern',
                    'Return to gate': 'Atlantis Gate'
                }
            },
            {
                'location': 'Throne Room',
                'description': 'You enter a grand throne room. An ancient king offers you a choice: power or wisdom.',
                'choices': {
                    'Choose power': 'End Power',
                    'Choose wisdom': 'End Wisdom',
                    'Flee': 'Crystal Cavern'
                }
            },
            {
                'location': 'End Power',
                'description': 'You gain immense power but are cursed to guard Atlantis forever. Game Over.',
                'choices': {}
            },
            {
                'location': 'End Wisdom',
                'description': 'You gain wisdom and unlock the secrets of Atlantis. You return home a hero. Game Over.',
                'choices': {}
            }
        ]
        for narrative in narratives:
            Narrative.objects.get_or_create(
                location=narrative['location'],
                defaults={
                    'description': narrative['description'],
                    'choices': narrative['choices']
                }
            )
        return Narrative.objects.all()

    def display_status(self):
        print(f"\nPlayer: {self.player.name}")
        print(f"Health: {self.player.health}")
        print(f"Location: {self.player.location}")
        print(f"Inventory: {self.player.inventory}\n")

    def apply_choice_effects(self, choice):
        if choice == 'Search the surroundings' and self.player.location == 'Atlantis Gate':
            if random.random() < 0.5:
                print("You found a Healing Crystal!")
                self.player.inventory.append('Healing Crystal')
                self.player.health = min(100, self.player.health + 20)
            else:
                print("You found nothing but seaweed.")
        elif choice == 'Collect crystals' and self.player.location == 'Crystal Cavern':
            print("You collected a Glowing Crystal!")
            self.player.inventory.append('Glowing Crystal')
        elif choice == 'Approach the figure' and self.player.location == 'Crystal Cavern':
            print("The figure attacks! You lose 20 health.")
            self.player.health -= 20
        elif choice == 'Rest' and self.player.location == 'Atlantis Gate':
            print("You rest and regain 10 health.")
            self.player.health = min(100, self.player.health + 10)
        self.player.save()

    def play(self):
        while self.player.health > 0:
            self.display_status()
            narrative = Narrative.objects.get(location=self.player.location)
            print(narrative.description)
            if not narrative.choices:
                print("The End.")
                break

            print("\nChoices:")
            for i, choice in enumerate(narrative.choices.keys(), 1):
                print(f"{i}. {choice}")
            choice_idx = input("\nEnter your choice (number): ")
            try:
                choice_idx = int(choice_idx) - 1
                choices = list(narrative.choices.keys())
                if 0 <= choice_idx < len(choices):
                    choice = choices[choice_idx]
                    self.apply_choice_effects(choice)
                    next_location = narrative.choices[choice]
                    self.player.location = next_location
                    self.player.save()
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")
            time.sleep(1)
        if self.player.health <= 0:
            print("You have perished in Atlantis. Game Over.")
