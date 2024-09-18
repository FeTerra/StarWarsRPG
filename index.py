import random
import time

# Classe dos personagens
class Character:
    def __init__(self, name, health, attack_power, force_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.force_power = force_power

    def attack(self, opponent):
        damage = random.randint(5, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} atacou {opponent.name}, causando {damage} de dano.")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} foi derrotado!")

    def use_force(self, opponent):
        force_damage = random.randint(10, self.force_power)
        self.health += 5  # O uso da força regenera um pouco de vida
        opponent.health -= force_damage
        print(f"{self.name} usou a Força contra {opponent.name}, causando {force_damage} de dano.")
        print(f"{self.name} regenerou 5 pontos de vida.")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} foi derrotado!")

    def special_ability(self, opponent):
        pass  # Cada personagem terá uma habilidade especial única

    def is_alive(self):
        return self.health > 0

# Criando personagens com habilidades especiais
class LukeSkywalker(Character):
    def special_ability(self, opponent):
        print(f"{self.name} usa 'Golpe de Sabre Avançado'!")
        damage = 30
        opponent.health -= damage
        print(f"{self.name} causou {damage} de dano em {opponent.name} com sua habilidade especial.")

class DarthVader(Character):
    def special_ability(self, opponent):
        print(f"{self.name} usa 'Estrangulamento com a Força'!")
        damage = 35
        opponent.health -= damage
        print(f"{self.name} causou {damage} de dano em {opponent.name} com sua habilidade especial.")
        self.health += 10
        print(f"{self.name} regenerou 10 pontos de vida.")

class Yoda(Character):
    def special_ability(self, opponent):
        print(f"{self.name} usa 'Sabedoria da Força'!")
        self.health += 40
        print(f"{self.name} regenerou 40 pontos de vida com sua habilidade especial.")

class KyloRen(Character):
    def special_ability(self, opponent):
        print(f"{self.name} usa 'Raiva Descontrolada'!")
        damage = random.randint(30, 50)
        opponent.health -= damage
        print(f"{self.name} causou {damage} de dano em {opponent.name} com sua habilidade especial.")

class ObiWanKenobi(Character):
    def special_ability(self, opponent):
        print(f"{self.name} usa 'Ataque Defensivo'!")
        damage = 25
        opponent.health -= damage
        self.health += 15
        print(f"{self.name} causou {damage} de dano em {opponent.name} e regenerou 15 pontos de vida.")

class EmperorPalpatine(Character):
    def special_ability(self, opponent):
        print(f"{self.name} usa 'Relâmpagos da Força'!")
        damage = 40
        opponent.health -= damage
        print(f"{self.name} causou {damage} de dano em {opponent.name} com sua habilidade especial.")

# Classe para arenas
class Arena:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def apply_effect(self, player1, player2):
        # Aplica o efeito da arena na batalha
        self.effect(player1, player2)

# Função para criar personagens
def create_characters():
    return [
        LukeSkywalker("Luke Skywalker", 100, 20, 30),
        DarthVader("Darth Vader", 120, 25, 40),
        Yoda("Yoda", 90, 15, 50),
        KyloRen("Kylo Ren", 110, 30, 35),
        ObiWanKenobi("Obi-Wan Kenobi", 100, 18, 28),
        EmperorPalpatine("Imperador Palpatine", 95, 22, 45)
    ]

# Função para escolher personagens
def choose_character():
    characters = create_characters()
    print("Escolha seu personagem:")
    for index, character in enumerate(characters):
        print(f"{index + 1}. {character.name} (Vida: {character.health}, Ataque: {character.attack_power}, Força: {character.force_power})")

    choice = int(input("Digite o número do personagem: ")) - 1
    return characters[choice]

# Função para criar arenas
def create_arenas():
    return [
        Arena("Tatooine", "Deserto árido. Todos os ataques causam 10% mais dano.",
              lambda p1, p2: apply_attack_bonus(p1, p2, 1.10)),
        Arena("Endor", "Floresta densa. Todos os personagens regeneram 5 de vida a cada turno.",
              lambda p1, p2: regenerate_health(p1, p2, 5)),
        Arena("Mustafar", "Planeta vulcânico. Todos os personagens perdem 5 de vida a cada turno.",
              lambda p1, p2: lose_health(p1, p2, 5)),
        Arena("Estrela da Morte", "Estação espacial. Vilões recebem 20% de bônus de ataque.",
              lambda p1, p2: boost_villain_attack(p1, p2, 1.20)),
        Arena("Dagobah", "Local remoto com forte conexão à Força. Habilidades da Força são 20% mais poderosas.",
              lambda p1, p2: boost_force_power(p1, p2, 1.20))
    ]

# Efeitos das arenas
def apply_attack_bonus(player1, player2, bonus):
    player1.attack_power = int(player1.attack_power * bonus)
    player2.attack_power = int(player2.attack_power * bonus)
    print(f"Todos os ataques causam {int((bonus - 1) * 100)}% mais dano nesta arena!")

def regenerate_health(player1, player2, health_points):
    player1.health += health_points
    player2.health += health_points
    print(f"Todos os personagens regeneram {health_points} pontos de vida.")

def lose_health(player1, player2, health_points):
    player1.health -= health_points
    player2.health -= health_points
    print(f"Todos os personagens perdem {health_points} pontos de vida devido ao calor intenso!")

def boost_villain_attack(player1, player2, bonus):
    villains = ["Darth Vader", "Kylo Ren", "Imperador Palpatine"]
    if player1.name in villains:
        player1.attack_power = int(player1.attack_power * bonus)
        print(f"{player1.name} recebeu um bônus de {int((bonus - 1) * 100)}% de ataque!")
    if player2.name in villains:
        player2.attack_power = int(player2.attack_power * bonus)
        print(f"{player2.name} recebeu um bônus de {int((bonus - 1) * 100)}% de ataque!")

def boost_force_power(player1, player2, bonus):
    player1.force_power = int(player1.force_power * bonus)
    player2.force_power = int(player2.force_power * bonus)
    print(f"Habilidades da Força são {int((bonus - 1) * 100)}% mais poderosas nesta arena!")

# Função para escolher arena
def choose_arena():
    arenas = create_arenas()
    print("\nEscolha a arena de batalha:")
    for index, arena in enumerate(arenas):
        print(f"{index + 1}. {arena.name} - {arena.description}")
    choice = int(input("Digite o número da arena: ")) - 1
    return arenas[choice]

# Função principal do jogo
def star_wars_battle():
    # Jogador 1 escolhe o personagem
    print("Jogador 1, escolha seu personagem:")
    player1 = choose_character()

    # Jogador 2 escolhe o personagem
    print("\nJogador 2, escolha seu personagem:")
    player2 = choose_character()

    # Escolha da arena
    arena = choose_arena()
    print(f"\nA batalha será na arena: {arena.name}!\n")

    print(f"Batalha entre {player1.name} e {player2.name} começa na arena {arena.name}!\n")

    # Batalha em turnos
    while player1.is_alive() and player2.is_alive():
        print(f"\n{player1.name}: {player1.health} de vida")
        print(f"{player2.name}: {player2.health} de vida")

        # Aplicar o efeito da arena
        arena.apply_effect(player1, player2)

        # Turno de ataque do Jogador 1
        action = random.choice(["attack", "force", "special"])
        if action == "attack":
            player1.attack(player2)
        elif action == "force":
            player1.use_force(player2)
        else:
            player1.special_ability(player2)

        time.sleep(1)  # Pausa para dar um efeito de turno

        # Verifica se o Jogador 2 ainda está vivo
        if not player2.is_alive():
            print(f"\n{player1.name} venceu a batalha!")
            break

        # Aplicar o efeito da arena no início do turno do Jogador 2
        arena.apply_effect(player1, player2)

        # Turno de ataque do Jogador 2
        action = random.choice(["attack", "force", "special"])
        if action == "attack":
            player2.attack(player1)
        elif action == "force":
            player2.use_force(player1)
        else:
            player2.special_ability(player1)

        time.sleep(1)  # Pausa para dar um efeito de turno

        # Verifica se o Jogador 1 ainda está vivo
        if not player1.is_alive():
            print(f"\n{player2.name} venceu a batalha!")
            break

# Executando o jogo
star_wars_battle()
