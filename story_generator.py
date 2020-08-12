# a random spoiler generator based on this comic:
# https://xkcd.com/2243/

import random

# define the various options and choose randomly one
villain = ['Kyle Ren', 'Malloc', 'Darth Sebelius', 'Theranos', 'Lord Juul']
friend = ['Kym Spacemeasurer','Teen Yoda','Dab Tweetdek', 'Yaz Progestin', 'TI-83']
lightsaber = ['beige', 'ochre', 'mauve', 'aquamarine', 'taupe']
superweapon = ['Sun Obliterator', 'Moonsquisher', 'World Eater', 'Planet Zester', 'Superconducting Supercollider']
superpower = ['blowing up a planet with a bunch of beams of energy that combine into one', 'blowing up a bunch of planets with one beam of energy that splits into many', 'cutting a planet in half and smashing the halves together like two cymbals', "increasing the CO2 levels in a planet's atmosphere, causing rapid heating", 'triggering the end credits before the movies is done']
old_enemy = ['Boba Fett', 'Salacious Crumb', 'The Space Slug', 'The Bottom Half of Darth Maul', 'YouTube Commenters']
feat = ['a bow that shoots little lightsaber-headed arrows.', 'X-Wings and TIE Fighters dodging the giant letters of the opening crawl.', 'a Sith educational display that uses force lightning to demonstrate the dielectric breakdown of air.', 'Kylo Ren putting on another helmet over his smaller one.', 'a Sith car wash where the bristles on the brushes are little lightsabers.']
father = ['Luke', 'Leia', 'Han', 'Obi-Wan', 'a random junk-trader']
mother = ['Poe.', 'BB-8.', 'Amilyn Holdo.', 'Laura Dern.', 'a random junk-trader.', 'that one droid from the Jawa Sandcrawler that says "gonk".']

# creates the parts of the story
intro = 'In this Star Wars movie, our heroes return to take on the First Order and new villain '
part_1 = '. With help from their new friend '
part_2 = ', Rey builds a new lightsaber with a '
part_3 = " blade, and they head out to confront the First Order's new weapon, the "
part_4 = ', a space station capable of '
part_5 = '. They unexpectedly join forces with their old enemy, '
part_6 = ', and destroy the superweapon in a battle featuring '
part_7 = "\n\nP.S. Rey's parents are "
part_8 = ' and '

# generates the story
def rsg():
  print(intro + random.choice(villain) + part_1 + random.choice(friend) + part_2 + random.choice(lightsaber) + part_3 + random.choice(superweapon) + part_4 + random.choice(superpower) + part_5 + random.choice(old_enemy) + part_6 + random.choice(feat) + part_7 + random.choice(father) + part_8 + random.choice(mother))


while True:
  rsg()
  while True:
    user_input = input('Would you like to generate a new spoiler? [y,n]\n')
    if user_input not in ('y', 'n'):
      print('Please enter "y" for yes or "n" for no.')
      continue
    if user_input == 'y':
      break
    else:
      print('Alright, ciao!')
      quit()
