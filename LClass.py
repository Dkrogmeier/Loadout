import random

class Loadout:

    def __init__(self, gun):
        self.gun = gun
        self.barrel = []
        self.perks = []
        self.optic = []
        self.muzzle = []
        self.laser =[]
        self.grip =[]
        self.ammo = []
        self.underbarrel = []

    def printOut(self):
            return "{} {} {} {} {} {} {} {} {}".format(self.gun, self.barrel, self.perks, self.optic, self.muzzle, self.laser,self.grip,self.ammo,self.underbarrel) 

guns = ['M91', 'M4', 'M13', 'AK-47','Origen 12']
pistols = ['Magnum', 'Desert Eagle', 'Renetti', 'RPG', 'Strela']
optics = ['VLK', 'Monocle Reflex', 'Viper Reflex']
grip = ['Stippled Grip', 'Literally Sandpaper']
ammo = ['30 Rounds','50 Rounds', '200 Rounds']
laser = ['Tac Laser', '1mW Laser', '5mW Laser']
muzzle = ['Compensator', 'Suppressor']
perks = ['Fully Loaded', 'FMJ']
barrel = ['Extended Barrel', 'No barrel']
stocks = ['Short stock', 'No Stock']
perks1 = ['Scavenger', 'Cold Blooded', 'Kill Chain', 'Quick Fix']
perks2 = ['Restock', 'Overkill', 'High Alert', 'Ghost']
perks3 = ['Tune up', 'Amped', 'Shrapnel', 'Battle Hardened']

def getLoadout():
    p = random.choice(perks2)
    lists = [optics, grip, ammo, laser, muzzle, perks, barrel, stocks]
    i = 1
    count = 5#int(input("Enter # of attachments 0-5: "))
    while count > 5 or count < 0:
        count = int(input("Try again using 0-5: "))
    x = Loadout(random.choice(guns))
    print(x.gun)
    while i <= count:
        a = random.choice(lists)
        a1 = random.choice(a)
        lists.remove(a)
        i += 1
        print(a1)
    if p == 'Overkill':
        overKill()
    else:
        notoverKill()
    print(random.choice(perks1))
    print(p)
    print(random.choice(perks3))

def notoverKill():
    lists = [optics, grip, ammo, laser, muzzle, perks, barrel, stocks]
    x = random.choice(pistols)
    if x == 'RPG' or 'Strela':
        print('\n{}\n'.format(x))
        #return
    i = 1
    count = 5
    print('\n{}'.format(x))
    while i <= count:
        a = random.choice(lists)
        a1 = random.choice(a)
        lists.remove(a)
        i += 1
        print(a1)
    return

def overKill():
    lists = [optics, grip, ammo, laser, muzzle, perks, barrel, stocks]
    x = random.choice(guns)
    print('\n{}'.format(x))
    i = 1
    count = 5
    while i <= count:
        a = random.choice(lists)
        a1 = random.choice(a)
        lists.remove(a)
        i += 1
        print(a1)
    return


y = Loadout(random.choice(guns))
getLoadout()
y.printOut()

    
