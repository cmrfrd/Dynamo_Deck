import json
import itertools
from copy import deepcopy
from deck import deck
from card import card

def flatten_list(layers, *input_list):
    '''
    this function is just so useful
    I had to make it global to all the
    classes
    '''
    return (flattened_element 
                for element in input_list
                for flattened_element in 
                (flatten_list(layers-1, *element) 
                if isinstance(element, (tuple, list)) and layers>-1 else (element,)))

class Arribute_Dict(dict):
    '''
    implementation is so when referencing attributes
    a line or 2 can be saved to be better understood

    returns key if missing
    '''
    def __missing__(self, key):
        return key

class Dict(dict):
    '''
    This is a really confusing and custom dictionary

    The main functionality is whenever the value (in key,value pair)
    is a dict, instead of returning a normal dict, it returns a dict
    with the same functionality as this dict.

    Essentially inheriting from a dict only applies to the first
    layer of the dict and no other subdicts. This inherited class
    applies the same functionality to all subdicts
    '''
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __getitem__(self, key):
        val = dict.__getitem__(self, key)
        if isinstance(val, dict):
            return Dict(val)
        return val

    def __missing__(self, key):
        if key=="repeat":
        #instructions without "repeat" default to 1 repetition
            return 1
        elif key in ["attributes", "cards", "front_face", "back_face"]:
        #instructions without "attributes", default to empty attribute dict
            return Dict()
        return False

    def iteritems(self):
        for key, value in dict.iteritems(self):
            if isinstance(value, dict):
                yield (key, Dict(value))
            else:
                yield (key, value)

class IterMethod_Dict(dict):
    '''
    when searching for an itertools method
    default is repeat
    '''
    def __missing__(self, key):
        return itertools.repeat

    def construct_iter(self, attributes, iter_func, iter_func_args):
        '''
        method to construct an iterator from attributes given,
        the itertools function, and the arguments
        turns arguments into a dict iterator
        '''
        iterator_function = self[iter_func]

        if iterator_function == itertools.repeat:
            #return the name of the value, and the function
            return [iter_func], iterator_function(attributes[iter_func_args])

        elif iterator_function == itertools.chain:
            #unpack the list of iters into chain, returns first iterator as the name
            return [iter_func_args[0]], iterator_function(*[attributes[attrib_arg] for attrib_arg in iter_func_args])

        else:
            #gets the names, then flatten list and add args to iterfunc
            list_vals = iter_func_args.values()
            names = list_vals[0] if isinstance(list_vals[0],list) else [list_vals[0]]
            flattened_list = list(flatten_list(1, list_vals))
            iter_args = [attributes[element_arg] for element_arg in flattened_list]
            return names, iterator_function(*iter_args)


class Deck_Builder(object):
    '''
    This class builds decks of cards into "Deck" objects
    name : Deck_Builder
    arguments : dict
    return : deck
    This class returns a singular deck object from
    a specified instruction set 'json_Deck_Builder'

    load deck, then excecute instructions to make cards
    '''

    all_instructions = []
    all_decks = []

    itermethods = IterMethod_Dict(
                            {
                                "izip_longest":itertools.izip_longest,
                                "product":itertools.product,
                                "permutations":itertools.permutations,
                                "combinations":itertools.combinations,
                                "combinations_with_replacement":itertools.combinations_with_replacement,
                                "chain":itertools.chain
                        }
                )
    
    def __init__(self, instruction=None, raise_error=False):
        '''
        name : build_deck
        arguments : ### filepath, or dict  ###
        return : Object deck
        This is the "main" function for the entire
        deck building program and will return a deck object to 
        the user to manipulate
        '''
        if instruction == None:
            pass
        else:
            self.load_instruction(instruction)

    def make_card_face_iter(self, card_instruction_face, deck_attributes):
        '''
        name : make_card_face_iter
        arguments : card_instruction_face
        return : iter
        Function returns an iterator
        ''' 
        card_names = []
        card_iters = []
        for face_value_method, face_value_instructions in card_instruction_face.iteritems():
            card_name, card_iter = self.itermethods.construct_iter(                                        
                                        deck_attributes,                                                        
                                        face_value_method,                                                      
                                        face_value_instructions                                                 
                                    )
            #grab the name of the iter, then the iter itself

            card_names.append(card_name)
            card_iters.append(card_iter)
            #add each var to their respective list
        #store all the names and iterators in lists


        if all(map(lambda f:isinstance(f,itertools.repeat), card_iters)):
            #when all the iters are infinite, just get one result
            yield dict([value_iter.next() for value_iter in card_iters])
        else:
            #yield a card for as long as there is a finite generator
            for forever in itertools.count():
                yield dict(zip(
                            list(flatten_list(1, card_names)), 
                            list(flatten_list(1, map(next, card_iters)))
                            )
                        )
        #create the iterator for the card face

    def make_deck(self, instruction=0):
        '''makes deck from an index or from an int or a dict'''

        return_deck = deck()

        try:
            instruction = self.all_instructions.pop(instruction)
        except TypeError:#invalid type indexing
            if isinstance(instruction, dict):
                pass #if it's a dict :D
            else:
                raise TypeError("instruction is not dict")#if not >:(
        except IndexError:#invalid indexing
            raise IndexError("invalid instruction index")#specify error

        #^this shit is just to make sure we get a single dict
        #...also specify error checking

        instruction = Dict(instruction)
        #make instruction a special dict (see 'Dict' class)

        attributes = Arribute_Dict(instruction["attributes"])
        #seperate attributes for referencing

        get_repeat = lambda x=1:x if x>0 else 0

        for card_instruction_name, card_instruction in instruction["cards"].iteritems():
            #loop through each card instruction

            repeat = get_repeat(card_instruction["repeat"])
            #format the repeat int to 0 or a positive int

            front_face_iter = self.make_card_face_iter(card_instruction["front_face"], attributes)
            back_face_iter = self.make_card_face_iter(card_instruction["back_face"], attributes)
            #make generators for the front and back of the cards

            for front, back in itertools.izip_longest(front_face_iter, back_face_iter, fillvalue={}):
            #loop through generators to get info for each card
                card_dict = {
                        "front_face":dict(front),
                        "back_face":dict(back)
                    }
                #blank template to add card information for card class

                for repeat_card in range(repeat):
                    return_deck.add_card(card(card_dict))
                #add the repeated cards
        
        self.all_decks.append(return_deck)
        return return_deck

    def load_instruction(self, instruction, raise_error=False):
        '''
        name : load_instructions
        arguments : instructions, raise_error
        return : boolean
        '''

        instruction_dict = {}

        if isinstance(instruction, str):#filepath string input
            instruction_dict = Deck_Builder.filepath_to_dict(instruction)
        elif isinstance(instruction, file):#json file input
            instruction_dict = Deck_Builder.file_to_dict(instruction)
        elif isinstance(instruction, dict):#dict input
            pass 
        else:#no other form of input accepted
            return False

        if not raise_error: 
            instruction_dict = Dict(instruction)

        self.all_instructions.append(instruction_dict)
        return True
    
    @staticmethod
    def get_func_from_string(func_name):
        '''
        name : get_func_from_string
        arguments : func_name string
        return : function
        gets the associated function from
        '''

    @staticmethod
    def filepath_to_dict(path):
        '''
        name : json_path_to_dict
        arguments : string
        return : dict
        This function will return a dictionary from a filepath
        to a json file
        ''' 
        instruction_file = open(path,"r").read()
        return json.loads(instruction_file)
    
    @staticmethod
    def file_to_dict(instruction_file):
        '''
        name : file_to_dict
        arguments : file
        return : dict
        This function will return a dictionary from a file 
        object provided
        ''' 
        if type(instruction_file) == file:
            return json.load(instruction_file)
        return False