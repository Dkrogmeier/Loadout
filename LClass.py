import random

guns = ['Kilo 141', 'Oden', 'M4A1', 'M13', 'FAL', 'SCAR-17', 'FR 5.56', 'AK-47', 'RAM-7', 'GRAU 5.56',
'CR-56 AMAX', 'AN-94', 'SA87', 'PKM', 'MG34', 'M91', 'Holger-26', 'Bruen MK9']
#primary = [kilo141, oden, m4, m13, fal, scar, fr, ak, ram, grau, amax, an, sa87, pkm, mg34, m91, holger, bruen]
pistols = ['X16', '1911', '.357', 'M19', '.50 GS', 'Renetti']
#secondary = [x16, nineteen, magnum, m19, gs, renetti]
BoomKnives = ['RPG', 'Strela-P', 'JOKR', 'PILA', 'Combat Knife', 'Kali Sticks', 'Dual Kodachis']
#thepunch = [rpg, strela, jokr, pila, knife, kali, kodachi]
Secondary = [pistols, BoomKnives]

optics = ['Monocle Reflex', 'Viper Reflex Sight', 'Operator Reflex Sight', 'Corp Combat Halo Sight', 'Aim-Op Reflex Sight', 'G.I. Mini Reflex', 'Scout Combat Optic',
            'APX5 Holographic Sight', 'Cronen LP945 Mini Reflex', '4.0x Flip Hybrid', 'VLK 3.0x Optic', 'Integral Hybrid', 'Variable Zoom Scope', 'Canted Hybrid',
            'Solozero Optics Mini Reflex', 'Thermal Hybrid', 'PBX Holo 7 Sight', 'Merc Thermal Optic', 'Sniper Scope', 'Monocle Reflex Sight', 'Solozero NVG Enhanced',
            'Cronen C480 Pro Optic']
grip = ['Stippled Grip', 'Granulated Grip Tape', 'Rubberized Grip Tape']
laser = ['Tac Laser', '1mW Laser', '5mW Laser']
muzzle = ['Compensator', 'Tactical Suppresor', 'Muzzle Brake', 'Lightweight Suppresor', 'Monolithic Suppresor', 'Flash Guard', 'Breacher Device']
perks = ['Fully Loaded', 'FMJ', 'Presence of Mind', 'Frangible - Disabling', 'Burst', 'Fast Melee', 'Sleight of Hand', 'Mo Money', 'Frangible - Wounding', 'Recon', 'Heavy Hitter']
underbarrel = ['Commando Foregrip', 'Bipod', 'Ranger Foregrip', 'Operator Foregrip', '40mm Incendiary', 'Tactical Foregrip', '40mm Flash', '40mm High-Explosive',
                '40mm Recon', '12-Gauge Deputy', '40mm Smokescreen']

perks1 = ['Scavenger', 'Cold Blooded', 'Kill Chain', 'Quick Fix']
perks2 = ['Restock', 'Overkill', 'High Alert', 'Ghost']
perks3 = ['Tune up', 'Amped', 'Shrapnel', 'Battle Hardened']

#-----------------------------------------Assault Rifles-------------------------------------------------------------------
kiloBarrel = ['Singuard Arms 16.6 Socom', 'Singuard Arms 19.8 Prowler', 'Singuard Arms Whisper']
kiloStock = ['FORGE TAC Ultralight', 'No Stock', 'Singuard Arms Sniper Pro', 'FSS Close Quarters Stock']
kiloAmmo = ['50 Rounds','60 Rounds', '100 Rounds']
kilo141 = [optics, grip, laser, muzzle, perks, underbarrel, kiloAmmo, kiloBarrel, kiloStock]

odenMuzzle = ['CQB Breacher Device', 'Collosus Suppresor']
odenBarrel = ['Oden Factory 810mm', 'Oden Factory 730mm', 'Oden Factory 420mm']
odenStock = ['FORGE TAC Ballast Pack', 'Oden Ultralight Hollow', 'FTAC XL Elite Comb']
odenUnder = ['M203 40m Concussive']
odenAmmo = ['25 Round Mags', '30 Round Mags']
oden = [optics, grip, laser, odenMuzzle, perks, odenUnder, odenStock, odenAmmo, odenBarrel]

m4Barrel =['FFS 11.5 Commando', 'Stock M16 Grenadier', 'FFS 14.5 Tac Lite', 'Corvus Custom Marksman', 'FFS 12.4 Predator']
m4Stock = ['M-16 Stock', 'Singuard Arms Invader', 'No Stock', 'Forge Tac CQS']
m4Ammo = ['50 Round Mags', '60 Rounds Mags', '9mm 32-Round Mags', '458 SOCOM 10-Round Mags']
m4 = [optics, grip, laser, muzzle, perks, underbarrel, m4Ammo, m4Barrel, m4Stock]

m13Barrel = ['Tempus Mini', 'Tempus Cyclone', 'Tempus Marksman']
m13Stock = ['Forge TAC Stalker', 'No Stock', 'FSS Close Quarters Stock', 'M13 Skeleton Stock']
m13Ammo = ['50 Round Mags', '300 Blackout 30-Round Mags', '60 Rounds Mags']
m13 = [optics, grip, laser, muzzle, perks, underbarrel, m13Ammo, m13Barrel, m13Stock]

falBarrel = ['18.0 Ultralight', 'XRK Marksman', '13.0 OSW Para']
falStock = ['Factory 18 Aluminum', 'No Stock', 'FSS Close Quarters', 'Forge Tac Stalker']
falAmmo = ['24 Round Mags', '30 Round Mags']
fal = [optics, grip, laser, muzzle, perks, underbarrel, falAmmo, falBarrel, falStock]

scarBarrel = ['Forge TAC 17.2 LB', 'Forge TAC 20 LB', 'Forge TAC CQC Pro']
scarStock = ['FTAC Hunter', 'FTAC Collapsible Stock', 'FSS Close Quarters Stock', 'XRK Obelisk Pro']
scarAmmo = ['25 Round Mags', '30 Round Mags']
scar = [optics, grip, laser, muzzle, perks, underbarrel, scarAmmo, scarBarrel, scarStock]

frBarrel = ['15.9 Commando', 'FR 24.4 Sniper', 'TAC Forge Ultralight']
frStock = ['FR Ultralight Hollow', 'Forge TAC Ballast Pack', 'FSS Tac-Wrap']
frAmmo = ['50 Round Mags', '60 Round Mags']
fr = [optics, grip, laser, muzzle, perks, underbarrel, frAmmo, frBarrel, frStock]

akBarrel = ['Spetsnaz Elite', '23.0 RPK Barrel', '8.1 Compact Barrel', '23.0 Romanian']
akStock = ['Field LMG Stock', 'Skeleton Stock', 'No Stock', 'FFS Close Quarters Stock', 'Forge TAC Ultralight']
akAmmo = ['40 Round Mags', '5.45x39mm 30-Round Mags', '75 Round Drum Mags']
ak = [optics, grip, laser, muzzle, perks, underbarrel, akAmmo, akBarrel, akStock]

ramBarrel = ['FTAC 13.5 Compact', 'Forge TAC Eclipse', 'XRK Ranger']
ramStock = ['FTAC Equilibrium', 'XRK Ultralight Hollow', 'XRK Close Quarters Stock']
ramAmmo = ['50 Round Mags']
ram = [optics, grip, laser, muzzle, perks, underbarrel, ramAmmo, ramBarrel, ramStock]

grauBarrel = ['ZLR Drifter A-08', 'Tempus 26.4 Archangel', 'XRK CZEN mk2', 'FFS 20.8 Nexus']
grauAmmo = frAmmo
grauGrip = ['XRK Void II', 'Cronen Sniper Elite', 'FTAC R-89 Rubber']
grauStock = ['Field LMG Stock', 'Skeleton Stock', 'No Stock', 'FFS Close Quarters Stock', 'Forge TAC Ultralight']
grau = [optics, grauGrip, laser, muzzle, perks, underbarrel, frAmmo, grauBarrel, grauStock]

amaxBarrel = ['FSS 8.3 Intruder', 'XRK Zodiac S440', 'FSS 11.8']
amaxStock = ['FSS Close Quarters Stock', 'FTAC Hunter', 'No Stock', 'FTAC Spartan', 'XRK Gatekeeper', 'CR-56 Exo']
amaxAmmo = ['45 Round Mags', 'M67 10-R Mags']
amax = [optics, grip, laser, muzzle, perks, underbarrel, amaxAmmo, amaxBarrel, amaxStock]

#anMuzzle = ['AN-94 Sonic Brake']
anBarrel = ['AN-94 Factory 330mm', 'AN-94 Factory X-438mm', 'VLK AN-94 Sila']
anStock = ['AN-94 Factory Heavy', 'Forge TAC Ultralight', 'Folded Stock', 'FSS Close Quarters Stock', 'VLK PX-9']
anAmmo = ['45 Round Mags', '60 Round Casket Mags']
an = [optics, grip, laser, muzzle, perks, underbarrel, anAmmo, anBarrel, anStock]

#---------------------------------Pistols---------------------------------
pmuzzle = ['Flash Guard', 'Monolithic Suppresor', 'Muzzle Brake', 'Oil Can Suppresor', 'Compensator','Lightweight Suppresor', 'Tactical Suppresor']
trigger = ['Lightweight Trigger', 'Heavy Duty Trigger', 'Match Grade Trigger']
pgrip = ['Granulated Grip Tape', 'Stippled Grip Tape', 'X16 Stock', 'Rubberized Grip Tape']
pperks = ['Fast Melee', 'Frangible - Wounding', 'Frangible - Disabling', 'FMJ', 'Mo Money', 'Sleight of Hand', 'Recon', 'Heavy Hitter', 'Fully Loaded', 'Akimbo']


x16 = [pmuzzle, laser, pgrip]

nineBarrel = ['45 Compact', '45 Match Grade', '1911 Stalker']
nineOptic = ['Cronen LP945 Mini Reflex', 'Solozero Optics Mini Reflex', 'G.I. Mini Reflex']
nineTA = ['Lightweight Trigger', 'Heavy Duty Trigger', 'Match Grade Trigger']
nineAmmo = ['10 Round Mags', '15 Round Mags']
nineteen = [pmuzzle, laser, grip, pperks, nineOptic, nineTA]

magnum = [laser, pperks, nineTA,]
m19 = [pmuzzle, laser, pperks, nineOptic, nineTA, grip]
gs = [pmuzzle, laser, pperks, nineTA, grip]
renetti = [pmuzzle, laser, pperks]

#----------------------------------SMGS-----------------------------------
fennec = [laser, grip]
mp5 = [laser, grip]
mp7 = [laser, grip]
aug = [laser, grip]
uzi = [laser, grip]
bizon = [laser, grip]
p90 = [laser, grip]
striker = [laser, grip]
iso = [laser, grip]
#-------------------------------Sniper Rifles-----------------------------
drag = [laser, muzzle, perks]
hdr = [laser, muzzle, perks]
ax = [laser, muzzle, perks]
rytec = [laser, muzzle, perks]
#------------------------------Marksman Rifles----------------------------
carbine = [muzzle, optics, grip, perks]
ebr = [muzzle, optics, grip, perks]
kar = [muzzle, optics, grip, perks]
sks = [muzzle, optics, grip, perks]
bow = [muzzle, optics, grip, perks]
#-----------------------------Shotguns------------------------------------
model = [laser, grip, perks]
seventwo = [laser, grip, perks]
r9 = [laser, grip, perks]
origin = [laser, grip, perks]
rogue = [laser, grip, perks]
#----------------------------LMGS----------------------------------------
saBarrel = ['18.2 Factory', '25.4 Factory', '12.4 Factory']
saStock = ['Heavy Stock Pro', 'Ultralight Hollow', 'TAC CQB Comb']
saUnder = ['Commando Foregrip', 'Merc Foregrip', 'Tactical Foregrip', 'Operator Foregrip', 'Bipod', 'Ranger Foregrip']
sa87 = [muzzle, optics, grip, perks, saBarrel, frAmmo, saUnder, saStock, laser]

pkBarrel = ['18.2 Compact Barrel', '26.9 Extended Barrel', '25.9 Heavy Barrel']
pkStock = ['Forge TAC Stalker', 'Forge Tac Ultralight', 'FFS Close Quarters Stock', 'No Stock']
pkGrip = ['Commando Foregrip','Merc Foregrip', 'Tactical Foregrip', 'Bipod', 'Snatch Grip', 'Operator Foregrip']
pkAmmo = ['150 Round Belt', '200 Round Belt']
pkm = [muzzle, optics, grip, perks, laser, pkBarrel, pkStock, pkGrip, pkAmmo]

mgBarrel = ['FSS Brute', 'FSS Stubby', 'FSS Elite']
mgAmmo = ['75 Round Belt', '100 Round Belt']
mg = [muzzle, optics, grip, perks, laser, mgBarrel, pkStock, saUnder, mgAmmo]

m91Barrel = ['M91 Special Forces', 'M91 Infantry', 'M91 Heavy']
m91Stock = ['Forge TAC Stalker', 'Forge Tac Ultralight', 'No Stock', 'XRK Striker']
m91Ammo = ['120 Round Belt', '150 Round Belt']
m91 = [muzzle, optics, grip, perks, laser, saUnder, m91Stock, m91Barrel, m91Ammo]

holBarrel = ['XRK Ultralight', 'FTAC 8.98 Spitfire']
holStock = ['FSS Ranger', 'FSS Infantry', 'No Stock', 'XRK Axis']
holUnder = ['Commando Foregrip', 'Merc Foregrip', 'Tactical Foregrip', 'Operator Foregrip', 'Ranger Foregrip']
holAmmo = ['30 Round Mags']
holger = [muzzle, optics, grip, perks, laser, holBarrel, holStock, holUnder, holAmmo]

bruBarrel = ['XRK Horizon 23.0', 'XRK Summit 26.8', 'Bruen 18,0 Para']
bruStock = ['Forge TAC Stalker', 'Forge Tac Ultralight', 'No Stock', 'Skeleton Stock']
bruAmmo = ['200 Round Belt', '60 Round Mags']
bruen = [muzzle, optics, grip, perks, laser, saUnder, bruBarrel, bruStock, bruAmmo]

#------------------------------------LOADOUT--------------------------------------------------------
def getLoadout():
    p = random.choice(perks2)
    primary = [kilo141, oden, m4, m13, fal, scar, fr, ak, ram, grau, amax, an, sa87, pkm, mg, m91, holger, bruen]
    i = 1
    count = 5#int(input("Enter # of attachments 0-5: "))
    #while count > 5 or count < 0:
    #    count = int(input("Try again using 0-5: "))
    x = random.choice(guns)
    z = guns.index(x)
    print(x)
    hold = []
    while i <= count:
        holdname = []
        a = primary[z]                   #a = gun at index z
        a1 = random.choice(primary[z])   #chooses one of attachments
        while a1 in hold:
            a1 = random.choice(primary[z])
        a2 = random.choice(a1)         #single attachment                   #remove attachments
        hold.append(a1)
        i += 1
        print(a2)
    if p == 'Overkill':
        overKill()
    else:
        notoverKill()

    print("\n{}".format(random.choice(perks1)))
    print(p)
    print("{}\n".format(random.choice(perks3)))



def notoverKill():
    #primary = [kilo141, oden, m4, m13, fal, scar, fr, ak, ram, grau, amax, an]
    secondary = [x16, nineteen, magnum, m19, gs, renetti]
    x = random.choice(Secondary)
    x1 = random.choice(x)
    if x1 in BoomKnives:
        print('\n{}'.format(x1))
        return
    else:
        z = pistols.index(x1)
        i = 1
        count = 2
        print('\n{}'.format(x1))
        while i <= count:
            hold = []
            a = secondary[z]    #guns
            a1 = random.choice(secondary[z])       #attachments
            a2 = random.choice(a1)      #single attachment
            a.remove(a1)            #remove attachments
            i += 1
            print(a2)
        return

def overKill():
    primary = [kilo141, oden, m4, m13, fal, scar, fr, ak, ram, grau, amax, an, sa87, pkm, mg, m91, holger, bruen]
    #guns = ['Kilo 141', 'Oden', 'M4A1', 'M13', 'FAL', 'SCAR-17', 'FR 5.56', 'AK-47', 'RAM-7', 'GRAU 5.56', 'CR-56 AMAX', 'AN-94']
    x = random.choice(guns)
    z = guns.index(x)
    print('\n{}'.format(x))
    i = 1
    count = 5
    while i <= count:
        a = primary[z]                   #a = gun at index z
        a1 = random.choice(primary[z])   #chooses one of attachments
        a2 = random.choice(a1)         #single attachment
        a.remove(a1)                   #remove attachments
        i += 1
        print(a2)
    return


getLoadout()
