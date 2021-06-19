class Player:
    def __init__(self, name="Player", gold=0, color="none"):
        self.name = name
        self.gold = gold
        self.color = color

    def __str__(self):
        return f'Player name is {self.name}. He/she has {self.gold} gold. His/her color is {self.color}'


    def win(self):
        return f'Player {self.name} is win'




players = []
players.append(Player('Gleb', 300, 'black'))
players.append(Player('Dima', 200, 'white'))
players.append(Player())



