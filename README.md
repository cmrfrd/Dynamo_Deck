#DYNAMO_DECK
######A dynamic card creator

####About
This library is designed to simulate a deck of cards for games or 
anything else really that would want to use cards for.

Using a special JSON instruction template you can create sequences of cards 

####Template Construction
So templates are split into 2 main areas ~~attributes~~ and ~~cards~~. ~~attributes~~ contain 
ant sort of string, list, or custom generator. ~~cards~~ contain different instruction sets
for each group of cards you want to make.

Deck instructions are made as follows:
```
{
    "attributes":{                      <------"attributes" is a key word that contains
                                                all the information that "cards" will
                                                refer to
        "1through5":[1,2,3,4,5],
        "4names":["Alex","Bobby","Liam","Chase"],
        "pi":3.14159
                                        ^------"each of these key,value pairs are attributes
                                               that can be reffered to in "cards". 
    },
    "cards":{                           <------"cards" is a key word that will contain
                                               all the instructions for different 
                                               sequences of cards
    }
}
```


Inside of the 'deck' template we need to define 'cards' or else we will end up 
with an empty deck. Basic Card instructions are made as follows:
```
"card_instruction_name":{                <------name of the card instruction
    "repeat":5,                          <------times you want the instruction repeated.
                                                This is an optional argument and will 
                                                default to 1 if not provided
    "front_face":{                       <------"front_face" is a key word that will
                                                contain the instruction(s) for what will
                                                be on the front of the card. If this isn't 
                                                provided, the face will be auto filled
                                                with {}
    },
    "back_face":{                        <------"back_face" has the same significance and 
                                                meaning as "front_face". 
    }
}
```

So defining a card instruction is pretty easy. However defining the attributes and
how they will arrange themselves onto a card inside of a deck starts to get a 
little tricky. 

Face instructions can get a little tricky because the methods used are built off of
the [itertools](https://docs.python.org/2/library/itertools.html) library. Look at
how to use itertools to understand how each of the methods work. 

**You may notice you can create 2 sequences of cards for either face. If one sequence
is longer than the other, Dynamo_Deck uses [izip_longest](https://docs.python.org/2/library/itertools.html#itertools.izip_longest) for future cards and the fill
value is {}.

A general template for an entire deck instruction goes as follows:
```
{
    "attributes":{
        "attr1":5,
        "attr2":[1,2,3,4,5],
        "attr3":"Name_Example",
        "attr4":['a','b','c','d'],
        "attr5":null
        ...                           <-----add as many attributes as you like.
                                            Custom Generators can also be added 
    },
    "cards":{
    
        "a_static_card":{             <------Name of the card(s) instruction
            "repeat":2,
            "front_face":{
                "title":"potatoes",   <------not listed in "attributes". This
                                             attribute will be stored as
                                             "potatoes" because the value name
                                             is not defined in attributes
                "name":"attr3"        <------listed in "attributes". "attr3" will
                                             be replaced by None
            }
        },
        ...                           <------as static cards as you like

        "sequential_cards_1":{
            
            "repeat":1,               <-----optional (default is one)

            "front_face":{            <-----optional (dflt is blank)
            
                "name":"attr3",       <-----referring to "attributes"
                
                "chain":["attr3"],    <-----Uses [chain](https://docs.python.org/2/library/itertools.html#itertools.chain) method

                "izip":["attr3"],     <-----Uses [izip](https://docs.python.org/2/library/itertools.html#itertools.izip) method

                "izip_longest":{      <-----Uses [izip_longest](https://docs.python.org/2/library/itertools.html#itertools.izip_longest) method
                    "name":["stuffystuff", "thingything"]
                    "iters":["attr2","attr4"],
                    "fillvalue":""   <-----optional (dflt to none)
                },

                "product":{           <-----Uses [product](https://docs.python.org/2/library/itertools.html#itertools.product) method
                    "names":["thingythats1","thingythats2"]
                    "iters":["attr2","attr4"],
                    "repeat":1        <-----optional (dflt to 1)
                },

                "permutations":{      <-----Uses [permutations](https://docs.python.org/2/library/itertools.html#itertools.permutations) method
                    "iter":"attr4",
                    "name":"thingy1", <-----optional                
                    "r":2             <-----optional (dflt to length of iter)
                },

                "combinations":{      <-----Uses [combinations](https://docs.python.org/2/library/itertools.html#itertools.combinations) method
                    "iter":"attr2",
                    "name":"thingy2", <-----optional
                    "r":2             <-----must have
                },

                "combinations_with_replacement":{        <-------Uses [combinations_with_replacement](https://docs.python.org/2/library/itertools.html#itertools.combinations_with_replacement) method
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
```


deck_52
```
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
```
