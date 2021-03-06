import json
import itertools
from copy import deepcopy
from deck import deck
from card import card

flatten_list = lambda layers, *input_list:   \
                   (flattened_element         \
                   for element in input_list   \
                       for flattened_element in (flatten_list(layers-1, *element) 
                           if isinstance(element, (tuple, list)) and layers>-1
                           else (element,)))
#this function is just so useful
#I had to make it global to all the
#classes



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
    This is a unique dictionary
    
    whenever you grab a sub-dictionary, a "Dict" is returned instead
    of a "dict".
    '''

    def __getitem__(self, key):
        '''
        This method is designed so that any subdicts
        when accessed have the same property as the
        main dict
        '''
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
            return Dict({})
        return None

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
        combinatoric_functions = [
            itertools.permutations,
            itertools.combinations,
            itertools.combinations_with_replacement
        ]

        iterative_functions = [
            itertools.chain, 
            itertools.izip
        ]

        iterative_list_functions = [
            itertools.izip_longest,
            itertools.product
        ]

        iterator_function = self[iter_func]

        if iterator_function == itertools.repeat:
            #return the name of the value, and the function
            return [iter_func], iterator_function(attributes[iter_func_args])

        elif iterator_function in iterative_functions:
            #unpack the list of iters into chain, returns first iterator as the name
            return [iter_func_args[0]], iterator_function(*[attributes[attrib_arg] for attrib_arg in iter_func_args])

        elif iterator_function in combinatoric_functions:
            #unpacks vals accordingly into combinatoric funcs		
	    assert "iter" not in iter_func_args.keys()
	    #"iter" must be in functino definition	    

            iter_name = iter_func_args["iter"]
            value_name = iter_func_args["name"] if "name" in iter_func_args.keys() else iter_name
            r = iter_func_args["r"]
            #evaluate the necessary args

            return [iter_name, iterator_function(attributes[iter_name], r)]
        
        elif iterator_function in iterative_list_functions:
            #unpacks accordingly into iterfuncs accordingly
	    assert "iters" in iter_func_args.keys()
	    #make sure "iter" is in function definition

            iters = iter_func_args["iters"]
		
	    card_values_names = iter_func_args["iters"]
	    if "names" in iter_func_args.keys():
	        values_names = iter_func_args["names"]
		card_values_names = values_names+card_values_names[len(values_names):]
	    #the names for each value have been determined
	    #variable name card_values_names
		
            iter_args = [attributes[iter_name] for iter_name in iters]
	    #get the iterators from the attributes by the names in "iters"

	    #special cases
	    additional_arg = {}
	    if iterator_function == itertools.product:
            	additional_arg["repeat"] = iter_func_args["repeat"]
	    elif iterator_function == itertools.izip_longest:
		additional_arg["fillvalue"] = iter_func_args["fillvalue"]

            return card_values_names, iterator_function(*iter_args, **additional_arg)

        else:
            raise ValueError("Bad iterator function")

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
                                "chain":itertools.chain,
                                "izip":itertools.izip
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
            print card_instruction_name
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
            instruction_dict = Dict(instruction_dict)

        self.all_instructions.append(instruction_dict)
        return True

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
        instruction_file = instruction_file.replace("'", "\"")
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
