class gamer:
    game = "callofduty"
    mood = "multiplayer"
    rank = "legend"
    level = 300
class car :
    def __init__(self,company,model,speed):
        self.company = company
        self.model = model
        self.speed = speed  
alex = gamer()
print(alex.game)
print(alex.mood)
print(alex.rank)
print(alex.level)
car1 = car("ford","mostang",320)
print(car1.company)
print(car1.model)
print(car1.speed)
