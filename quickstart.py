from Dynamo_Deck import Deck_Builder, card
from random import randrange

deck_52_path = "./Samples/deck_52.json"
canasta_path = "./Samples/canasta.json"
template_path = "./Samples/template.json"

d = Deck_Builder()

d.load_instruction(deck_52_path)
standard_deck_52 = d.make_deck()

d.load_instruction(canasta_path)
canasta_deck = d.make_deck()

d.load_instruction(template_path)
template_deck = d.make_deck()


get_rando_card = lambda l: l.remove_card(randrange(len(l)))
#quick lambda for ease of use


print "Gin-Rummy hand from standard_deck_52:"

sd52 = standard_deck_52 #short variables :)

for rando_num in range(10):
    print get_rando_card(sd52).flip()

print "\n\nCanasta hand from canasta_deck:"
for rando in range(11):
    print get_rando_card(canasta_deck).flip()

print "\n\nAll cards in template deck:"
for card in template_deck:
    print card
