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

{
    "unique_cards":{
        "card_1": {
            "front_face":{
                 "name":"card 1",
                 "description":"",
                 "attributes":{}
            },
            "back_face":{}
        }
    },
    "sequential_cards":{
        "seq1":{
            "repeat":1,
            "front_face":{
                 "attributes_constant":{
                     "name":"sequential_card"
                 },
                 "attributes_variable":{
                     "arrays":{
                         "array_1":["a","b","c","d"]
                     },
                     "organization":"sequential"
                 }
            },
            "back_face":{}
        }
    }
}

example: Standard deck of 52

{
    "sequential_cards":{
        "deck_52":{
            "front_face":{
                "attribute_variables":{
                    "arrays":{
                        "suit":["H","S","C","D"],
                        "value":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                    },
                    "product":{
                        "iters":["suit",""],
                        "repeat":
                    }
                }
            }
        }
    }
}


{
    "attributes":{
        "attr1":5,
        "attr2":[1,2,3,4,5],
        "attr3":"Name_Example",
        "attr4":['a','b','c','d'],
        "attr5":null
        ...                           <-----as many as you like
    }
    "cards":{

        "a_static_card":{
            "repeat":2,
            "front_face":{
                "title":"potatoes",   <------not listed in "attributes"
                "name":"attr3"        <------listed in "attributes"
            }
        },
        ...                           <------as many as you like

        "sequential_cards_1":{
            
            "repeat":1,               <-----optional (default is one)

            "front_face":{            <-----optional (dflt is blank)
            
                "name":"attr3",       <-----referring to "attributes"
                
                "chain":["attr3"],

                "izip_longest":{
                    "iters":["attr2","attr4"],
                    "value_fill":""   <-----optional (dflt to none)
                },

                "product":{
                    "iters":["attr2","attr4"],
                    "repeat":1        <-----optional (dflt to 1)
                },

                "permutations":{
                    "iter":"attr4",
                    "r":2             <-----optional (dflt to length of iter)
                },

                "combinations":{
                    "iter":"attr2",
                    "r":2             <-----must have
                },

                "combinations_with_replacement":{
                    "iter":"attr2",
                    "r":2             <-----must have
                }

                ^----only the first one of these is used,
                    be sure naming convention is not any of these

            },
            "back_face":{}            <------optional(dflt is blank)
        },
        ...                           <------as many as you like
    }
}



deck_52
{
    "attributes":{
        "value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "suit" : ["H","S","C","D"],
        "name" : "deck52_card"
    },
    "cards":{
        "deck_of_52":{
            "front_face":{
                "name":"name",
                "product":{
                    "iters":["value","suit"]
                }
            }
        }
    }
}