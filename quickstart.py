from Dynamo_Deck import Deck_Builder, card

deck_52 = {
    "attributes":{
        "value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "suit" : ["H","S","C","D"],
        "name" : "deck52_card"
    },
    "cards":{
        "deck_of_52":{
        	"repeat":2,
            "front_face":{
                "name":"name",
                "product":{
                    "iters":["value","suit"]
                }
            }
        }
    }
}


d = Deck_Builder()
d.load_instruction(deck_52)
deck1 = d.make_deck()


for card in deck1:
    card.flip()
    print card
    raw_input()