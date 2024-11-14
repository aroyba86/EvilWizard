# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        """Attacks an opponent and applies damage."""
        opponent.take_damage(self.attack_power)

    def heal(self, heal_amount):
        """Heals the character by a certain amount, not exceeding max health."""
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} healed by {heal_amount} points. Current health: {self.health}/{self.max_health}")

    def take_damage(self, damage_amount):
        """Reduces health by the damage amount, ensuring it doesn't drop below 0."""
        self.health = max(self.health - damage_amount, 0)
        print(f"{self.name} took {damage_amount} damage. Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        """Displays the character's stats."""
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def use_special_ability(self, opponent):
        """Placeholder for special ability, to be implemented in subclasses."""
        pass


# Character Subclasses (Warrior, Mage, Archer, Paladin, EvilWizard)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def use_special_ability(self, opponent):
        print(f"{self.name} charges into battle with a powerful attack!")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def use_special_ability(self, opponent):
        print(f"{self.name} casts a devastating fireball!")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=45)

    def use_special_ability(self, opponent):
        print(f"{self.name} fires a powerful arrow!")


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)

    def use_special_ability(self, opponent):
        print(f"{self.name} raises their shield, reducing damage for the next turn!")


class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        """Evil Wizard regenerates health over time."""
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def use_special_ability(self, opponent):
        """The Evil Wizard curses the opponent to reduce their attack power for 1 turn."""
        opponent.attack_power -= 5
        print(f"{self.name} curses {opponent.name}, reducing their attack power!")



def create_character():
    class_choices = {
        '1': Warrior,
        '2': Mage,
        '3': Archer,
        '4': Paladin
    }

    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    
    return class_choices.get(class_choice, Warrior)(name)



def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.use_special_ability(wizard)
        elif choice == '3':
            heal_amount = 55 if isinstance(player, Paladin) else 30
            player.heal(heal_amount)
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")


# Main function
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
