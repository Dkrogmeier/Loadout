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
pistols = ['X16', '1911', '.357', 'M19', '.50 GS', 'Renetti']
BoomKnives = ['RPG', 'Strela-P', 'JOKR', 'PILA', 'Combat Knife', 'Kali Sticks', 'Dual Kodachis']
Secondary = [pistols, BoomKnives]

optics = ['VLK', 'Monocle Reflex', 'Viper Reflex', 'Operator Reflex Sight', 'Corp Combat Halo Sight', 'Aim-Op Reflex Sight', 'G.I. Mini Reflex', 'Scout Combat Optic',
'APX5 Holographic Sight', 'Cronen LP945 Mini Reflex', '4.0x Flip Hybrid', 'VLK 3.0x Optic', 'Integral Hybrid', 'Variable Zoom Scope', 'Canted Hybrid',
'Solozero Optics Mini Reflex', 'Thermal Hybrid', 'PBX Holo 7 Sight', 'Merc Thermal Optic', 'Sniper Scope', 'Monocle Reflex Sight', 'Solozero NVG Enhanced',
'Cronen C480 Pro Optic']
grip = ['Stippled Grip', 'Granulated Grip Tape', 'Rubberized Grip Tape']
ammo = ['50 Rounds','60 Rounds', '100 Rounds']
laser = ['Tac Laser', '1mW Laser', '5mW Laser']
muzzle = ['Compensator', 'Tactical Suppresor', 'Muzzle Brake', 'Lightweight Suppresor', 'Monolithic Suppresor', 'Flash Guard', 'Breacher Device']
perks = ['Fully Loaded', 'FMJ', 'Presence of Mind', 'Frangible - Disabling', 'Burst', 'Fast Melee', 'Sleight of Hand', 'Mo Money', 'Frangible - Wounding', 'Recon', 'Heavy Hitter']
barrel = ['Extended Barrel', 'No barrel']
underbarrel = ['Commando Foregrip', 'Bipod', 'Ranger Foregrip', 'Operator Foregrip', 'M203 40mm Incendiary', 'Tactical Foregrip', 'M203 40mm Flash', 'M203 40mm High-Explosive', 'M203 40mm Recon', '12-Gauge Deputy', 'M203 40mm Smokescreen']
stocks = ['FORGE TAC Ultralight', 'No Stock', 'Singuard Arms Sniper Prowler', 'FSS Close Quarters Stock']

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
    print("\n{}".format(random.choice(perks1)))
    print(p)
    print("{}\n".format(random.choice(perks3)))

def notoverKill():
    lists = [optics, grip, ammo, laser, muzzle, perks, barrel, underbarrel, stocks]
    x = random.choice(Secondary)
    x1 = random.choice(x)
    if x1 in BoomKnives:
        print('\n{}'.format(x1))
        return
    else:
        i = 1
        count = 5
        print('\n{}'.format(x1))
        while i <= count:
            a = random.choice(lists)
            a1 = random.choice(a)
            lists.remove(a)
            i += 1
            print(a1)
        return

def overKill():
    lists = [optics, grip, ammo, laser, muzzle, perks, barrel, underbarrel, stocks]
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


getLoadout()
getLoadout()
getLoadout()
