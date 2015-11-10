import json
from card import card

class deck(object):
    '''
    This class represents a deck of cards
    '''
    def __init__(self, *args):
        
        self.card_list = []
        self.missing_cards = []
        
        self.add_cards(args)
    
    def pick_card(self, remove=False, *args):
        '''
        name : pick_card
        arguments : int, boolean
        return : Object Card
        This method picks a card by an index "card_index". 
        This funciton does not remove the card, instead it
        places it in a buffer "missing_cards" unless specified
        by "remove". Either way, poped card is returned
        '''
        
        if remove:
            return self.remove_cards(args)
        
        self.missing_cards.extend([self.card_list.pop(i) for i in args])
        #entend "missing cards"
        
        return self.missing_cards[-len(args):]
        #get those cards by slicing the length of the inputs
    
    def add_cards(self, *args):
        '''
        name : add_cards
        arguments : dict, or args Object Card
        return : boolean
        This method takes cards as input and adds them to 
        the deck.
        '''
        if all(isinstance(cd, (card, deck)) for cd in args):
            pass
    
    def remove_cards(self, *args):
        '''
        name : remove_cards
        arguments : int(s)
        return : list Object Card
        This method removes cards from the deck and returns
        them in a list to the user. If unused, cards are
        deleted
        '''
        return [self.card_list.pop(i) for i in args]
        
    def get_card_data(self):
        '''
        name : get_card_data
        arguments : None
        return : listObject Card, listObject Card
        Method returns the deck, and the missing cards
        '''
        return self.card_list, self.missing_cards