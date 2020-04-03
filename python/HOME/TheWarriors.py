class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = 1
    
    def disp(self):
        print(self.health, self.is_alive)

    def hit(self):
        self.attack = 5
        return self.attack
        
    def alive(self):
        if self.health <= 0: 
            print("Warrior is Dead")
            self.is_alive = 0
        else:
            print("Warrior is Alive")

class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7
        self.is_alive = 1

    def disp(self):
        print(self.health, self.is_alive)
    
    def hit(self):
        self.attack = 7
        return 

    def alive(self):
        if self.health <= 0: 
            print("Knight is Dead")
            self.is_alive = 0
        else:
            print("Knight is Alive")

def fight(unit_1, unit_2):
    print('=================')
    unit_1.disp()
    unit_2.disp()
    print('=================')
    
    round = 0
    while unit_1.health > 0 and unit_2.health > 0:
        round += 1
        print('-----------------')
        print('Round=', round)
        if round % 2 == 1:
            #unit_2.health -= unit_1.hit()
            unit_2.health -= unit_1.attack
        else:
            #unit_1.health -= unit_2.hit()
            unit_1.health -= unit_2.attack
        print('1st=', unit_1.health, '2nd=', unit_2.health)

    unit_1.alive()
    unit_2.alive()
    print(unit_1.is_alive)
    return unit_1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
