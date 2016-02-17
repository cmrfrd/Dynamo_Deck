from Dynamo_Deck import Deck_Builder, card
from random import choice

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

print "Gin-Rummy hand from standard_deck_52:"
print standard_deck_52
for rando in range(10):
    print choice(standard_deck_52).flip()

print "\n\nCanasta hand from canasta_deck:"
for rando in range(11):
    print canasta_deck.pop().flip()

print "\n\nAll cards in template deck:"
for card in template_deck:
    print card.flip()