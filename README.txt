##################################
These files are designed to simulate a deck of cards for any game.

unique and sequential cards can be created via JSON input

Card
|____Attributes
|   |_face_in_view:bool
|   |_Attributes:dict
|   |_
|   
|
|____Methods
    |_flip_card():bool
    |_read():dict
    
Deck
|____Attributes
|   |_number_of_cards:int
|   |_probobility_distibution:list
|   |_
|   
|
|____Methods
    |_raise_likelyhood():list
    |_remove_card():bool
    |_shuffle():bool
    |_show_all():dict
    |_

deck object has
    card object

deck builder has
    static_card_builder



example: Standard deck of 52

{
    "sequential_cards":{
        "deck_52":{
            "front_face":{
                "attribute_variables":{
                     "ranges":{
                         "value":{
                             "begin":1,
                             "end":13,
                             "step":1
                         }
                     },
                     "lists":{
                         "suit":["H","S","C","D"]
                     },
                     "organization":"product"
                }
            }
        }
    }
}