import random

class Player:
    def __init__(self, name):
        self.name = name      
        self.score = 0        

    def choice(self):
        pass  

class Human(Player):
    def choice(self):
        return input("1-камень,2-ножницы,3-бумага: ")

class Computer(Player):
    def choice(self):
        return str(random.randint(1, 3))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1   
        self.p2 = p2   

    def play(self):
        c1 = self.p1.choice()
        c2 = self.p2.choice()
        print(self.p1.name, "выбрал", c1)
        print(self.p2.name, "выбрал", c2)
        
        if c1 == c2:
            print("ничья")
        elif (c1 == "1" and c2 == "2") or (c1 == "2" and c2 == "3") or (c1 == "3" and c2 == "1"):
            print(self.p1.name, "победил")
            self.p1.score += 1
        else:
            print(self.p2.name, "победил")
            self.p2.score += 1
        print("счёт:", self.p1.name, self.p1.score, "-", self.p2.name, self.p2.score)

name = input("твоё имя: ")
human = Human(name)
bot = Computer("компьютер")
game = Game(human, bot)

for _ in range(3):
    game.play()





