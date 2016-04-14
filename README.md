#DYNAMO_DECK
######A dynamic card creator

####About
This library is designed to simulate a deck of cards in memory for games or 
anything else really that would want to use cards for.

Using a special JSON instruction template you can create sequences of cards 

####Template Construction
So templates are split into 2 main areas **attributes** and **cards**.

**attributes** must contain any sort of generator, if it isn't, Dynamo_Deck will
make it a generator. 

**cards** contain different instruction sets for each group of cards you want to 
make.

Deck instructions are made as follows:
```
{
    "attributes":{                      <------"attributes" is a key word that contains
                                                all the information that "cards" will
                                                refer to
        "1through5":[1,2,3,4,5],
        "4names":["Alex","Bobby","Liam","Chase"],
        "pi":3.14159
                                        ^------each of these key,value pairs are attributes
                                               that can be reffered to in "cards". 
    },
    "cards":{                           <------"cards" is a key word that will contain
                                               all the instructions for different 
                                               sequences of cards
    }
}
```


Inside of the "cards" template we need to define groups of cards, or else we will end up 
with an empty deck. Basic Card instructions are made as follows:
```
"card_instruction_name":{                <------name of the card instruction
    "repeat":5,                          <------"repeat" is a key word and (as it says) repeats
                                                the instruction as many times as you want.
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

Itertools methods used:
[repeat](https://docs.python.org/2/library/itertools.html#itertools.repeat),
[chain](https://docs.python.org/2/library/itertools.html#itertools.chain),
[izip](https://docs.python.org/2/library/itertools.html#itertools.izip),
[izip_longest](https://docs.python.org/2/library/itertools.html#itertools.izip_longest),
[permutations](https://docs.python.org/2/library/itertools.html#itertools.permutations),
[combinations](https://docs.python.org/2/library/itertools.html#itertools.combinations),
[combinations_with_replacement](https://docs.python.org/2/library/itertools.html#itertools.combinations_with_replacement),
[product](https://docs.python.org/2/library/itertools.html#itertools.product)

###Three important things to mention:

1. You may notice you can create 2 sequences of cards for either face. If one sequence
is longer than the other, Dynamo_Deck uses [izip_longest](https://docs.python.org/2/library/itertools.html#itertools.izip_longest) with a fillvalue of {} (empty face).

2. In addition to that it is also important that Dynamo_Deck won't allow you to combine itertools
methods together (unless you define your own custom generator) because no one wants to get
all the permutations of a combination of numbers... NO ONE.

3. An optional argument "name" or "names" is provided so instead of the key to the name defaulting 
to what it is reffered to in "attributes", you can provide your own custom names.

A general template for an entire deck instruction goes as follows with the addition of
card instructions
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
                "title":"potatoes",   <------"potatoes" is not listed in "attributes". 
                                             Dynamo_Deck understands that and will cause
                                             it to be stored as "potatoes"
                "name":"attr3"        <------"attr3" islisted in "attributes". When this
                                             group is created, "attr3" will be replaced with
                                             None
            }
        },
        ...                           <------Dynamo_Deck is designed so if you want to make a 
                                             Single card, you can! Just give the card values that
                                             won't be turned into generators

        "sequential_cards_1":{
            
            "repeat":1,               <-----optional (default is one)

            "front_face":{            <-----optional (dflt is blank)
            
                "name":"attr3",       <-----referring to "attributes"
                
                "chain":["attr3"],    <-----Uses chain method

                "izip":["attr3"],     <-----Uses izip method

                "izip_longest":{      <-----Uses izip_longest method
                    "name":["stuffystuff", "thingything"]
                    "iters":["attr2","attr4"],
                    "fillvalue":""   <-----optional (dflt to none)
                },

                "product":{           <-----Uses product method
                    "names":["thingythats1","thingythats2"]
                    "iters":["attr2","attr4"],
                    "repeat":1        <-----optional (dflt to 1)
                },

                "permutations":{      <-----Uses permutations method
                    "iter":"attr4",
                    "name":"thingy1", <-----optional                
                    "r":2             <-----optional (dflt to length of iter)
                },

                "combinations":{      <-----Uses combinations method
                    "iter":"attr2",
                    "name":"thingy2", <-----optional
                    "r":2             <-----must have
                },

                "combinations_with_replacement":{        <-------Uses combinations_with_replacement method
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


As an example this is how you would make a standard deck of 52 cards.
If you want to be more specific with each card you can replace '11,12,13' 
with 'Jack, Queen, King'.
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
If we want to make a deck using Dynamo_Deck and our 52 card template you would do the following.
```Python
from Dynamo_Deck import Deck_Builder
from random import randrange

deck_52_path = "path/to/deck_52.json"
#filepath to our template

d_builder = Deck_Builder(deck_52_path)
#initialize our builder object with out template loaded into the object

deck_52 = d_builder.make_deck()
#make the deck loaded into the builder
```
```deck_52``` is now a ```deck``` object that we created and can now manipulate in memory. 

To get a random card:   ```r_card = deck_52.remove_card(randrange(len(l)))```

Card objects by default are <b>face down</b>. So if you ```print``` them they will appear as a ```{}```. In order to see the data we need to do ```r_card.flip()```. This enables the card to be read.


####Future
Make every deck of cards a generator so every card you grab from a deck is made on the fly.
