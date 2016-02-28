#DYNAMO_DECK
####A dynamic card creator

######About
This library is designed to simulate a deck of cards for games or 
anything else really that would want to use cards for.

Using a special JSON instruction template you can create sequences of cards 

######Template Construction
So templates are split into 2 main areas --attributes-- and --cards--. --attributes-- contain 
ant sort of string, list, or custom generator. --cards-- contain different instruction sets
for each group of cards you want to make.

Card instructions are made as follows

'''
"card_instruction_name":{                <------name of the card instruction
    "repeat":5,                          <------times you want the instruction repeated.
                                                This is an optional argument and will 
                                                default to 1 if not provided
    "front_face":{                       <------
    },
    "back_face":{
    }
}
'''

The general template goes as follows..

{
    "attributes":{
        "attr1":5,
        "attr2":[1,2,3,4,5],
        "attr3":"Name_Example",
        "attr4":['a','b','c','d'],
        "attr5":null
        ...                           <-----add as many attributes as you like
                                            Custom Generators can also be added 
    },
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

                "izip":["attr3"],

                "izip_longest":{
                    "name":["stuffystuff", "thingything"]
                    "iters":["attr2","attr4"],
                    "fillvalue":""   <-----optional (dflt to none)
                },

                "product":{
                    "names":["thingythats1","thingythats2"]
                    "iters":["attr2","attr4"],
                    "repeat":1        <-----optional (dflt to 1)
                },

                "permutations":{
                    "iter":"attr4",
                    "name":"thingy1", <-----optional                
                    "r":2             <-----optional (dflt to length of iter)
                },

                "combinations":{
                    "iter":"attr2",
                    "name":"thingy2", <-----optional
                    "r":2             <-----must have
                },

                "combinations_with_replacement":{
                    "name":"thingy3"
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
