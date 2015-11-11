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
    
    @staticmethod
    def all_cards_or_decks(*args):
        '''
        name : all_cards_or_decks
        arguments : Object card(s), Object deck(s)
        return : boolean
        methods return T/F if input is all cards or deck
        '''
        all(isinstance(cd, (card, deck)) for cd in args)
        
    @staticmethod
    def slice_deck_card(*args):
        '''
        name : slice_deck_card
        arguments : Object card(s), Object deck(s)
        return : List Object Card, List Object Deck
        Method slices input to cards, and decks
        '''
        cards = []
        decks = []
        if deck.all_cards_or_decks(*args):
            for s in args:
                if isinstance(s, card):
                    cards.append(s)
                elif isinstance(s, deck):
                    decks.append(s)
                else:
                    pass
                    #raise error
            return cards, decks
        return cards, decks
    
    def pick_card(self, remove=True, location=0):
        '''
        name : pick_card
        arguments : int, boolean
        return : Object Card
        Method picks a card by an index "location". 
        Places cards in buffer "missing_cards"
        '''
        
    
    def pick_cards(self, remove=True, *args):
        '''
        name: pick_cards
        arguments : boolean, int(s)
        return Object(s) card(s)
        Method picks multiple card specified by "args"
        '''
        if remove:
            return self.remove_cards(args)
        self.missing_cards.extend([self.card_list.pop(i) for i in args])
        #entend "missing cards"
        return self.missing_cards[-len(args):]
        #get those cards by slicing the length of the inputs
        
    def add_card(self, card_input, location=0):
        '''
        name : add_card
        arguments : int, Object Card
        return : boolean
        method adds a card object to the deck 
        based on location
        '''
        if isinstance(card_input, card):
            self.card_list.insert(location, card_input)
            return True
        return False
    
    def add_cards(self, location=0,*args):
        '''
        name : add_cards
        arguments : int, Object Cards or Object deck
        return : boolean
        This method takes cards as input and adds
        them in order based on the location
        '''
        if deck.all_cards_or_decks(*args):
            #cards, decks = deck.slice_deck_card(args)
            for s in args:
                if isinstance(s, card):
                    self.add_card(location, s)
                elif isinstance(s, deck):
                    decks.add_deck(s)
                else:
                    pass
                    #raise error
                location += 1
            return True
        return False
    
    def add_missing_card(self, card_input):
        '''
        name : add_missing_card
        arguments : Object Card
        return : boolean
        '''
        if isinstance(card_input, card):
            self.missing_cards.append(card_input)
            return True
        return False
        
    def add_missing_cards(self, *args):
        '''
        name : add_missing_cards
        arguments : Object Cards
        return : boolean
        '''
        if deck.all_cards_or_decks(*args):
            
            return True
        return False
        
    def add_decks(self, location=0,*args):
        '''
        name : add_decks
        arguments : object Deck or Object Card
        return : boolean
        Method takes a deck of cards as input and adds to deck
        '''
        if deck.all_cards_or_decks(*args):
            for select in args:
                if isinstance(select, card):
                    self.add_cards()
                elif isinstance(select, deck):
                    self.add_decks(select)
                location += 1
            return True
        return False
        
    
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