class Warrior:
    is_alive: bool = True
    health: int = 50
    attack: int = 5
    pass

class Knight(Warrior):
    attack: int = 7
    pass

def fight(frst, scnd):
    while frst.is_alive and scnd.is_alive:
        scnd.health -= frst.attack
        frst.health -= scnd.attack
        if scnd.health <= 0:
            scnd.is_alive = False
            return True
        elif frst.health <= 0:
            frst.is_alive = False
            return False
    return 0

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
