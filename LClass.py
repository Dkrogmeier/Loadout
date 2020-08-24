import random

guns = ['Kilo 141', 'Oden', 'M4A1', 'M13', 'FAL', 'SCAR-17', 'FR 5.56', 'AK-47', 'RAM-7', 'GRAU 5.56',
'CR-56 AMAX', 'AN-94', 'SA87', 'PKM', 'MG34', 'M91', 'Holger-26', 'Bruen MK9', "Fennec", 'MP5', 'MP7', 'AUG',
        'UZI', 'Bizon', 'P90', 'ISO','Dragunov', 'HDR', 'AX-50','Rytec AMR', 'MK2 Carbine', 'M14 EBR', 'Kar-98k', 'SKS', 'Crossbow', 'Striker 45', 'Model 680 Shotgun', '725 Shotgun', 'R9-0 Shotgun', 'Origin 12', 'VLK Rogue']
#primary = [kilo141, oden, m4, m13, fal, scar, fr, ak, ram, grau, amax, an, sa87, pkm, mg, m91, holger,
#bruen, fennec, mp5, mp7, aug, uzi, bizon, p90, iso, drag, hdr, ax, rytec, carbine, ebr, kar, sks, bow, striker, model, seventwo, r9, origin, rogue]
pistols = ['X16', '1911', '.357', 'M19', '.50 GS', 'Renetti']
#secondary = [x16, nineteen, magnum, m19, gs, renetti]
BoomKnives = ['RPG', 'Strela-P', 'JOKR', 'PILA', 'Combat Knife', 'Kali Sticks', 'Dual Kodachis']
#thepunch = [rpg, strela, jokr, pila, knife, kali, kodachi]
Secondary = [pistols, BoomKnives]
lethal = ['Claymore', 'Frag Grenade', 'Molotov Cocktail', 'C4', 'Semtex', 'Throwing Knife', 'Proximity', 'Thermite', 'Flaming Throwing Knife']
tactical = ['Flash Grenade', 'Stun Grenade', 'Smoke Grenade', 'Snapshot Grenade', 'Heartbeat Sensor', 'Gas Grenade', 'Stim', 'Decoy Grenade']



optics = ['Monocle Reflex', 'Viper Reflex Sight', 'Operator Reflex Sight', 'Corp Combat Halo Sight', 'Aim-Op Reflex Sight', 'G.I. Mini Reflex', 'Scout Combat Optic',
            'APX5 Holographic Sight', 'Cronen LP945 Mini Reflex', '4.0x Flip Hybrid', 'VLK 3.0x Optic', 'Integral Hybrid', 'Variable Zoom Scope', 'Canted Hybrid',
            'Solozero Optics Mini Reflex', 'Thermal Hybrid', 'PBX Holo 7 Sight', 'Merc Thermal Optic', 'Sniper Scope', 'Monocle Reflex Sight', 'Solozero NVG Enhanced',
            'Cronen C480 Pro Optic']
opticslite = ['Monocle Reflex', 'Viper Reflex Sight', 'Operator Reflex Sight', 'Corp Combat Halo Sight', 'Aim-Op Reflex Sight', 'G.I. Mini Reflex', 'Scout Combat Optic',
            'APX5 Holographic Sight', 'Cronen LP945 Mini Reflex', 'VLK 3.0x Optic', 'Integral Hybrid', 'Canted Hybrid',
            'Solozero Optics Mini Reflex', 'Thermal Hybrid', 'PBX Holo 7 Sight', 'Merc Thermal Optic', 'Monocle Reflex Sight', 'Solozero NVG Enhanced',
            'Cronen C480 Pro Optic']
grip = ['Stippled Grip', 'Granulated Grip Tape', 'Rubberized Grip Tape']
laser = ['Tac Laser', '1mW Laser', '5mW Laser']
muzzle = ['Compensator', 'Tactical Suppresor', 'Muzzle Brake', 'Lightweight Suppresor', 'Monolithic Suppresor', 'Flash Guard', 'Breacher Device']
perks = ['Fully Loaded', 'FMJ', 'Presence of Mind', 'Frangible - Disabling', 'Burst', 'Fast Melee', 'Sleight of Hand', 'Mo Money', 'Frangible - Wounding', 'Recon', 'Heavy Hitter']
perkslite = ['Fully Loaded', 'FMJ', 'Frangible - Disabling', 'Fast Melee', 'Sleight of Hand', 'Mo Money', 'Frangible - Wounding', 'Recon', 'Heavy Hitter']
underbarrel = ['Commando Foregrip', 'Bipod', 'Ranger Foregrip', 'Operator Foregrip', '40mm Incendiary', 'Tactical Foregrip', '40mm Flash', '40mm High-Explosive',
                '40mm Recon', '12-Gauge Deputy', '40mm Smokescreen']

perks1 = ['Scavenger', 'Cold Blooded', 'Kill Chain', 'Quick Fix', 'Double Time', 'E.O.D']
perks2 = ['Restock', 'Overkill', 'High Alert', 'Ghost', 'Hardline', 'Pointman']
perks3 = ['Tune up', 'Amped', 'Shrapnel', 'Battle Hardened', 'Spotter', 'Tracker']


#-----------------------------------------Assault Rifles-------------------------------------------------------------------
kiloBarrel = ['Singuard Arms 16.6 SOCOM', 'Singuard Arms 19.8 Prowler', 'Singuard Arms Whisper']
kiloStock = ['FORGE TAC Ultralight', 'No Stock', 'Singuard Arms Sniper Pro', 'FSS Close Quarters Stock']
kiloAmmo = ['50 Rounds','60 Rounds', '100 Rounds']
kilo141 = [optics, grip, laser, muzzle, perks, underbarrel, kiloAmmo, kiloBarrel, kiloStock]

odenMuzzle = ['Flash Guard', 'Tactical Suppressor', 'CQB Breacher Device', 'Colossus Suppressor', 'Compensator', 'Muzzle Brake', 'Monolithic Suppressor']
odenBarrel = ['Oden Factory 810mm', 'Oden Factory 730mm', 'Oden Factory 420mm']
odenStock = ['FORGE TAC Ballast Pack', 'Oden Ultralight Hollow', 'FTAC XL Elite Comb']
odenUnder = ['Commando Foregrip', 'Bipod', 'Ranger Foregrip', 'Operator Foregrip', '40mm Incendiary', 'Tactical Foregrip', '40mm Flash', '40mm High-Explosive',
                '40mm Recon', '12-Gauge Deputy', '40mm Smokescreen','M203 40m Concussive']
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
falMuzzle = ['Muzzle Brake','Flash Guard','Tactical Suppressor','Lightweight Suppressor','Compensator','Monolithic Suppressor']
fal = [optics, grip, laser, falMuzzle, perks, underbarrel, falAmmo, falBarrel, falStock]

scarBarrel = ['Forge TAC 17.2 LB', 'Forge TAC 20 LB', 'Forge TAC CQC Pro']
scarStock = ['FTAC Hunter', 'FTAC Collapsible Stock', 'FSS Close Quarters Stock', 'XRK Obelisk Pro']
scarAmmo = ['25 Round Mags', '30 Round Mags']
scar = [optics, grip, laser, muzzle, perkslite, underbarrel, scarAmmo, scarBarrel, scarStock]

frBarrel = ['15.9 Commando', 'FR 24.4 Sniper', 'TAC Forge Ultralight']
frStock = ['FR Ultralight Hollow', 'Forge TAC Ballast Pack', 'FSS Tac-Wrap']
frAmmo = ['50 Round Mags', '60 Round Mags']
fr = [optics, grip, laser, muzzle, perks, underbarrel, frAmmo, frBarrel, frStock]

akMuzzle = ['Flash Guard','Muzzle Brake','Tactical Suppressor','Compensator','Lightweight Suppressor','Bayonet','Monolithic Suppressor']
akBarrel = ['Spetsnaz Elite', '23.0 RPK Barrel', '8.1 Compact Barrel', '23.0 Romanian']
akStock = ['Field LMG Stock', 'Skeleton Stock', 'No Stock', 'FFS Close Quarters Stock', 'Forge TAC Ultralight']
akAmmo = ['40 Round Mags', '5.45x39mm 30-Round Mags', '75 Round Drum Mags']
ak = [optics, grip, laser, akMuzzle, perkslite, underbarrel, akAmmo, akBarrel, akStock]

ramBarrel = ['FTAC 13.5 Compact', 'Forge TAC Eclipse', 'XRK Ranger']
ramStock = ['FTAC Equilibrium', 'XRK Ultralight Hollow', 'XRK Close Quarters Stock']
ramAmmo = ['50 Round Mags']
ram = [optics, grip, laser, muzzle, perks, underbarrel, ramAmmo, ramBarrel, ramStock]

grauBarrel = ['ZLR Drifter A-08', 'Tempus 26.4 Archangel', 'XRK CZEN mk2', 'FFS 20.8 Nexus', 'FSS 11.8 Squall']
grauAmmo = frAmmo
grauGrip = ['XRK Void II', 'Cronen Sniper Elite', 'FTAC R-89 Rubber']
grauStock = ['FSS Blackjack', 'XRK StrikeLite III', 'No Stock']
grau = [optics, grauGrip, laser, muzzle, perks, underbarrel, frAmmo, grauBarrel, grauStock]

amaxBarrel = ['FSS 8.3 Intruder', 'XRK Zodiac S440', 'FSS 11.8']
amaxStock = ['FSS Close Quarters Stock', 'FTAC Hunter', 'No Stock', 'FTAC Spartan', 'XRK Gatekeeper', 'CR-56 Exo']
amaxAmmo = ['45 Round Mags', 'M67 10-R Mags']
amax = [optics, grip, laser, muzzle, perkslite, underbarrel, amaxAmmo, amaxBarrel, amaxStock]

anMuzzle = ['AN-94 Sonic Brake','Flash Guard','Tactical Suppressor','Lightweight Suppressor','Compensator',
'Monolithic Suppressor']
anBarrel = ['AN-94 Factory 330mm', 'AN-94 Factory X-438mm', 'VLK AN-94 Sila']
anStock = ['AN-94 Factory Heavy', 'Forge TAC Ultralight', 'Folded Stock', 'FSS Close Quarters Stock', 'VLK PX-9']
anAmmo = ['45 Round Mags', '60 Round Casket Mags']
an = [optics, grip, laser, anMuzzle, perks, underbarrel, anAmmo, anBarrel, anStock]


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


#----------------------------------SMGS------------------------------------------------------------------------------
fenMuzzle = ['Flash Guard', 'Muzzle Brake', 'CQB Breacher Device', 'Tactical Suppresor', 'Monolithic Suppresor', 'ZLR Sabre', 'Compensator']
fenBarrel = ['ZLR 16 Apex', 'ZLR 18 Deadfall']
fenStock = ['FTAC C6 Carbine PRO', 'FORGE TAC CQS', 'ZLR Blade', 'No Stock']
fenAmmo = ['40 Round Drum Mags', '45 Hollow Point 12-R Mags']
fenUnder = ['Merc Foregrip','Commando Foregrip','Operator Foregrip','Tactical Foregrip', 'Ranger Foregrip']
fennec = [laser, grip, perkslite, optics, fenMuzzle, fenBarrel, fenStock, fenAmmo, fenUnder]

mp5Barrel = ['FSS Light','Monolithic Integral Suppressor','FSS Mini','Subsonic Integral Suppressor']
mp5Stock = ['FORGE TAC Ultralight','Classic Straight-line Stock','FSS Close Quarters Stock','FTAC Collapsible']
mp5Ammo = ['45 Rounds', '10mm 30 Round Mags']
mp5Under = ['Commando Foregrip','Merc Foregrip','Ranger Foregrip','Tactical Foregrip','Operator Foregrip']
mp5 = [laser, grip, muzzle, opticslite, perkslite, mp5Stock, mp5Ammo, mp5Under, mp5Barrel]

mp7Barrel = ['FSS Strike', 'FSS Recon', 'FSS Swat']
mp7Stock = ['FORGE TAC Ultralight','FORGE TAC Stalker','FSS Close Quarters Stock','No Stock']
mp7 = [laser, grip, opticslite, perkslite, frAmmo, mp5Under, muzzle, mp7Barrel, mp7Stock]

augBarrel = ['407mm Extended Barrel','407mm Lightweight','622mm Long Barrel']
augStock = ['FTAC Ultralight Hollow','FORGE TAC CQB Comb','FSS Heavy Stock Pro']
augAmmo = ['32 Round Mags','5.56 NATO 30-Round Mags','5.56 NATO 60-Round Drums']
aug = [laser, grip, muzzle, opticslite, mp5Under, perkslite, augBarrel, augStock, augAmmo]

uziAmmo = ['40 Round Mags','50 Round Mags','.41 AE 32-Round Mags']
uziStock = ['FORGE TAC Ultralight','Standard-Issue Wood Stock','No Stock','FSS Close Quarters Stock']
uziBarrel = ['13.1" First Responder','8.5" Factory Mini','16.5" Factory Carbine','FSS Carbine Pro']
uzi = [muzzle, laser, grip, opticslite, uziBarrel, mp5Under, uziAmmo, uziStock]

bizonBarrel = ['8.7" Steel','8.7" Polygonal','8.7" Aluminum']
bizonAmmo = ['84 Round Helical Mags']
bizonStock = ['Factory Aluminum Stock','No Stock','Corvus Skeleton Stock','FSS Close Quarters Stock']
bizon = [laser, grip, muzzle, opticslite, perkslite, bizonAmmo, bizonStock, bizonBarrel, mp5Under]


p90Barrel = ['FORGE TAC Retribution','FSS 10.6" Pro']
p90Stock = ['FORGE TAC CQB Comb','Fly Strap','FSS Heavy Stock Pro']
p90 = [laser, grip, muzzle, opticslite, perkslite, grip, p90Barrel, p90Stock]

strStock = ['FSS Guardian','FTAC Precision Fixed Stock','XRK Gen III Survivalist Series']
strAmmo = ['.45 Hollow Point 12-R Mags','45 Round Mags']
strBarrel = ['300mm Poly Barrel','400mm Stainless Steel','150mm Stainless Steel']
strGrip = ['FTAC 60 Series Polymer','FTAC G-5 EXO','FTAC 60 Series Rubber']
strUnder = ['Commando Foregrip','Merc Foregrip','Tactical Foregrip','Ranger Foregrip','Operator Foregrip']
striker = [laser, grip, muzzle, strBarrel, strAmmo, strStock, strUnder]

isoBarrel = ['FTAC 225mm Dominator','FSS Revolution','ISO 140mm CQB','FSS Nightshade']
isoStock = ['FORGE TAC Ultralight','FORGE TAC Stalker','FTAC Vagrant','ISO Collapsible']
isoGrip = ['FSS Vice ISO Grip','FTAC Elite ISO Grip','ISO Tac-Form']
isoAmmo = ['30 Round Mags','50 Round Drums']
iso = [laser, grip, perkslite, mp5Under, opticslite, isoBarrel, isoStock, isoGrip, isoAmmo]




#-------------------------------Sniper Rifles-----------------------------
dragBarrel= ['510mm Compact Barrel', '660mm Extended Barrel']
dragLaser = ['Tac Laser']
dragOptic = ['Scout Combat Optic', 'VLK 3.0x Optic', 'Merc Thermal Optic', 'Thermal Dual Power Scope', 'Variable Zoom Scope', 'Thermal Sniper Scope',
            'Cronen C480 Pro Optic']
dragStock = ['FTAC Hunter-Scout','Skeleton Stock', 'VLK Lightweight Stock', 'FTAC Stalker-Scout']
dragAmmo = ['15 Round Mags', '20 Round Mags']
dragUnder = ['Bipod']
drag = [dragLaser, muzzle, perkslite, dragBarrel,dragOptic, dragStock, dragAmmo, dragUnder]

hdrStock = ['FTAC Stalker-Scout','FTAC Hunter-Scout','FSS Nomad Stock','FTAC Champion']
hdrAmmo = ['7 Round Mags', '9 Round Mags']
hdrBarrel = ['26.9" HDR Pro','26.0" Bull Barrel','17.2" Bull Barrel']
hdr = [dragLaser, muzzle, perkslite, dragOptic, dragUnder, hdrAmmo, hdrBarrel, hdrStock]

axStock = ['Singuard Arms Marksman','Singuard Arms Evader', 'Singuard Arms Assassin']
axBarrel = ['Singuard Arms Pro','17.0" Factory Barrel','32.0" Factory Barrel' ]
ax = [dragLaser, muzzle, perkslite,dragOptic,dragUnder,hdrAmmo, grip, axStock, axBarrel]

ryMuzzle = ['XRK Tank Brake','Rytec AMR Suppressor']
ryBarrel = ['FTAC Seven Straight','FTAC 448mm Dictator','XRK Harbinger']
ryStock = ['XRK Mastadon','FTAC Trekker','STOVL Tac-Wrap']
ryAmmo = ['25×59mm Explosive 5-R mag','25×59mm Thermite 5-R mag']
rytec = [laser, perkslite,dragOptic,dragLaser,grip,ryStock, ryMuzzle, ryBarrel, ryAmmo]


#------------------------------Marksman Rifles----------------------------
carBarrel = ['FSS 18.0" Factory','FSS 20.0" Factory','FSS 24.0" Factory']
carStock = ['Cartridge Sleeve','FSS MK2 Sport Comb','FSS MK2 Precision Comb','MK2 Ultralight Hollow']
carbine = [muzzle, optics, grip, perkslite, dragLaser, carBarrel, carStock]

ebrBarrel = ['FORGE TAC Precision 20.0"','FORGE TAC Elite','FORGE TAC Precision 22.0"']
ebrStock = ['FTAC Precision Comb','FSS Raider Chassis Pro','FTAC Lightweight Stock','FSS Raider Chassis Elite']
ebrAmmo = ['15 Round Mags','20 Round Mags']
ebrUnder = ['Commando Foregrip','Tactical Foregrip','Bipod','Merc Foregrip','Ranger Foregrip','Operator Foregrip']
ebr = [muzzle, optics, perkslite, dragLaser, ebrBarrel, ebrStock, ebrAmmo, ebrUnder]

karBarrel = ['Singuard Custom 25.1"','Singuard Custom 21.2"','Singuard Custom 27.6"']
karStock =['STVOL Precision Comb','Hollow Stock Mod','FTAC Sport Comb']
kar = [muzzle, optics, grip, perkslite, dragLaser, karBarrel, karStock, dragUnder]

sksBarrel = ['FTAC Landmark','16" FSS Para','22" FSS M59/66']
sksStock = ['SKS Rifle Stock','FTAC Hunter-Scout','Sawed-off Stock']
sksAmmo = ['30 Round Mags','10 Round Mags']
sks = [muzzle, optics, grip, perkslite, dragLaser, sksBarrel, sksStock, sksAmmo]

bowStock = ['FORGE TAC Apex','FORGE TAC Dart CB','FORGE TAC SpeedTrak']
bowBolt = ['FTAC Fury 20" Bolts','FTAC Venom 20" Bolts','FTAC Backburn 20" Bolts']
bowUnder = ['FTAC Speed Grip','XRK Precision Grip','XRK Talon']
bowCable = ['16-Strand Cable','28-Strand Cable']
bowArms = ['XRK Thunder 200 Lb','XRK Quill 100 Lb','XRK Carbon Elite']
bow = [optics, perkslite, dragLaser, bowStock, bowBolt, bowUnder, bowCable, bowArms]
#-----------------------------Shotguns------------------------------------


oriMuzzle = ['Breacher Device','Flash Guard','Tactical Suppressor','Muzzle Brake','Compensator','Choke','Lightweight Suppressor','Monolithic Suppressor']
oriOptics = ['Monocle Reflex', 'Viper Reflex Sight', 'Operator Reflex Sight', 'Corp Combat Halo Sight', 'Aim-Op Reflex Sight', 'G.I. Mini Reflex', 'Scout Combat Optic',
            'APX5 Holographic Sight', 'Cronen LP945 Mini Reflex', 'VLK 3.0x Optic',
            'Solozero Optics Mini Reflex', 'PBX Holo 7 Sight', 'Monocle Reflex Sight', 'Solozero NVG Enhanced','Cronen C480 Pro Optic']
modelBarrel = ['XRK 18.0 Liberator', 'XRK 14.0 SWAT', 'XRK 30.0 Sport']
modelStock = ['FTAC Hunter','FORGE TAC Ultralight','No Stock','Lockwood Precision Series', 'FTAC Stalker-12']
modelUnder = ['Commando Foregrip','Merc Foregrip','Tactical Foregrip','Ranger Foregrip','Operator Foregrip', 'Lockwood Precision Series', 'XRK Truegrip Tactical']
modelAmmo = ['Tube Extensions','Slug Rounds', '12 Gauge 6-R Mags', 'Slug 6-R Mags', 'Dragons Breath Rounds']
model = [laser, grip, perkslite, oriMuzzle, oriOptics]

sevenBarrel = ['Tempus Smooth Bore','Sawed-off Barrel','Tempus 32" Competition']
sevenStock = ['Cronen Equilibrium','Cronen Pro Light','Sawed-off Stock','Tempus Sport']
sevenGuard = ['Tempus SlimGrip','FORGE TAC Steady Grip','FORGE TAC Commander']
sevenAmmo = ['Slug Rounds']
sevenUnder = ['Commando Foregrip','Merc Foregrip','Tactical Foregrip','Ranger Foregrip','Operator Foregrip']
seventwo = [laser, perkslite, oriMuzzle, oriOptics, sevenBarrel, sevenStock, sevenGuard, sevenAmmo, sevenUnder]

r9Barrel = ['FORGE TAC Sentry','FORGE TAC Gemini']
r9Pumps = ['FSS R9-0 Bulldog','FTAC Ultralight Pump','FTAC Close Quarters Pro']
r9Ammo = ['Tube Extensions','Slug Rounds']
r9Under = ['Merc Foregrip','Ranger Foregrip','Operator Foregrip']
r9 = [laser, grip, perkslite, oriMuzzle, r9Barrel, r9Pumps, r9Ammo, r9Under]

oriBarrel = ['FORGE TAC Precision','FORGE TAC Wideshot','FORGE TAC Impaler']
oriStock = ['FTAC Hunter','FORGE TAC Ultralight','No Stock','FORGE TAC Dart']
oriAmmo = ['12 Round Mags','8 Round Slug Mags','25 Round Drum Mags']
oriUnder = ['Merc Foregrip','Commando Foregrip']
origin = [laser, grip, perkslite, oriOptics, oriUnder, oriAmmo, oriStock, oriMuzzle, oriBarrel]

rogueGrip = ['XRK Race Grip','VLK Prime Pump Grip','XRK ReliaGrip']
rogueAmmo = ['12 Round Mags','8 Round Slug Mags','4 Round Mags',"Dragon's Breath Rounds"]
rogueBarrel = ['VLK Czar','6" Revolt','16" Warlord']
rogueStock = ['FTAC Hunter', 'FORGE TAC Ultralight', 'No Stock', 'FSS Close Quarters Stock']
rogue = [oriMuzzle, laser, grip, perkslite, oriOptics, rogueGrip, rogueAmmo, rogueBarrel, rogueStock]
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
    primary = [kilo141, oden, m4, m13, fal, scar, fr, ak, ram, grau, amax, an, sa87, pkm, mg, m91, holger,
    bruen, fennec, mp5, mp7, aug, uzi, bizon, p90, iso, drag, hdr, ax, rytec, carbine, ebr, kar, sks, bow, striker, model, seventwo, r9, origin, rogue]
    g = random.choice(lethal)
    g2 = random.choice(tactical)
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
    print("Lethal: {}".format(g))
    print("Tactical: {}\n".format(g2))



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
    primary = [kilo141, oden, m4, m13, fal, scar, fr, ak, ram, grau, amax, an, sa87, pkm, mg, m91, holger,
    bruen, fennec, mp5, mp7, aug, uzi, bizon, p90, iso, drag, hdr, ax, rytec, carbine, ebr, kar, sks, bow, striker, model, seventwo, r9, origin, rogue]
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

