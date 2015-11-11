import json
from card import card

class deck(object):
    '''
    This class represents a deck of cards
    '''
    def __init__(self, *args):
        
        self.card_list = []
        self.missing_cards = []
        
        self.add_cards(*args)
    
    @staticmethod
    def all_cards_or_decks(*args):
        '''
        name : all_cards_or_decks
        arguments : Object card(s), Object deck(s)
        return : boolean
        methods return T/F if input is all cards or deck
        '''
        all(isinstance(cd, (card, deck)) for cd in args)
        
    
    def pick_card(self, remove=True, location=0):
        '''
        name : pick_card
        arguments : int, boolean
        return : Object Card
        Method picks a card by an index "location". 
        Places cards in buffer "missing_cards"
        '''
        if remove:
            return self.remove_card(location)
            
        self.missing_cards.extend(self.card_list[location])
        #extend "missing cards"
        return self.missing_cards[-1]
        #get the card by getting last card
    
    def pick_cards(self, remove=True, *args):
        '''
        name: pick_cards
        arguments : boolean, int(s)
        return Object(s) card(s)
        Method picks multiple card specified by "args"
        '''
        if remove:
            return self.remove_cards(args)
        self.missing_cards.extend([self.pick_card(remove, i) for i in args])
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
            if card_input in self.missing_cards:
                self.missing_cards.remove()
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
            for s in args:
                if isinstance(s, card):
                    self.add_card(location, s)
                elif isinstance(s, deck):
                    self.add_deck(location, s)
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
        adds a mising card to the missing card list
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
        adds multiple missing cards to the missing
        card list
        '''
        if all(isinstance(cd, card) for cd in args):
            for c in args:
                if self.add_missing_card(c)):
                    pass
                else:
                    return False
            return True
        return False
        
    def add_deck(self, location=0, deck_input):
        '''
        name : add_deck
        arguments : object Deck
        return : boolean
        Method takes a deck of cards as input and adds to deck
        '''
        if isinstance(deck_input, deck):
            c, m = self.get_deck_data()
            if self.add_cards(c):
                if self.add_missing_cards(m):
                    return True
        return False
        
    def add_decks(self, location=0, *args):
        '''
        name : add_decks
        arguments : object Deck or Object Card
        return : boolean
        Method takes decks of cards as input and adds to deck
        '''
        if deck.all_cards_or_decks(*args):
            for select in args:
                if isinstance(select, card):
                    self.add_card()
                elif isinstance(select, deck):
                    self.add_deck(location, select)
                location += 1
            return True
        return False
    
    def remove_card(self, location=0):
        '''
        name : remove_card
        arguments : int
        return : Object card
        method removes card from deck and returns it
        '''
        return self.card_list.pop(location)
    
    def remove_cards(self, *args):
        '''
        name : remove_cards
        arguments : int(s)
        return : list Object Card
        This method removes cards from the deck and returns
        them in a list to the user. If unused, cards are
        deleted
        '''
        return [self.remove_card(i) for i in args]
        
    def get_deck_data(self):
        '''
        name : get_deck_data
        arguments : None
        return : listObject Card, listObject Card
        Method returns the deck, and the missing cards
        '''
        return self.card_list, self.missing_cards