from static_card_builder import static_card_builder
from sequential_card_builder import sequential_card_builder
import json

class Dict(dict):
    '''
    simple inherited dict class adds 
    __missing__ method for ease of use
    in error checking
    '''
    def __missing__(self, key):
        return False

class deck_builder(object):
    '''
    This class builds decks of cards into "Deck" objects
    name : deck_builder
    arguments : dict
    return : deck
    This class returns a singular deck object from
    a specified instruction set 'json_deck_builder'
    '''
    
    @staticmethod
    def build_deck(self, instructions, raise_error=False):
        '''
        name : build_deck
        arguments : ### filepath, or dict  ###
        return : Object deck
        This function is the "main" function for the entire
        deck building program and will return a deck object to 
        the user to manipulate
        '''
        
        #
        #
        #
        #
        #instructions = json.load(json_deck_builder)
        #accoutn for str, file obj, or dict
        #pass in unstruction set
        
        #stat_cards = []
        #seq_cards = []
        #create the container for the lists of cards
        
        #if instructions['static_cards']:
        #   stat_cards = static_card_builder.build(instructions['static_cards'])
        #
        #if instructions['sequential_cards']:
        #   seq_cards = sequential_card_builder.build(instructions['sequential_cards'])
        #if the instruction set exists, build the cards
        
        #return_deck = deck().load_cards(static_cards + seq_cards)
        
        #return return_deck
        pass
    
    @staticmethod
    def error_check(instructions):
        '''
        name : error_check
        arguments : dict
        return : boolean
        This functino checks to make the sure the instruction
        set provided from a user is valid and is not missing 
        any non-appropriate keywords
        '''
        pass
    
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
        
    @staticmethod
    def stringjson_to_dict(string_dict):
        '''
        name : stringdict_to_dict
        arguments : string
        return : dict
        This function takes a json string and converts
        it to a dict
        '''
        try:
            pass
        except ValueError:
            pass