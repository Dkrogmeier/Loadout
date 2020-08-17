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
optics = ['VLK', 'Monocle Reflex', 'Viper Reflex']
grip = ['Stippled Grip', 'Literally Sandpaper']
ammo = ['30 Rounds','50 Rounds', '200 Rounds']
laser = ['Tac Laser', '30 mm laser']
muzzle = ['Compensator', 'Suppressor']
perks = ['Fully Loaded', 'FMJ']
barrel = ['Extended Barrel', 'No barrel']
stocks = ['Short stock', 'No Stock']
perks1 = ['Scavenger', 'Cold Blooded', 'Kill Chain', 'Quick Fix']
perks2 = ['Restock', 'Overkill', 'High Alert', 'Ghost']
perks3 = ['Tune up', 'Amped', 'Shrapnel', 'Battle Hardened']

def getLoudout():
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
    print(random.choice(perks1))
    print(random.choice(perks2))
    print(random.choice(perks3))
    
y = Loadout(random.choice(guns))
getLoudout()
y.printOut()

    
