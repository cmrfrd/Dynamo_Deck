class card(dict):
    '''
    This class represents a playing card
    '''
    def __init__(self, *args, **kwargs):
        '''initialize card object'''
        super(self.__class__, self).__init__(*args, **kwargs)
        #initialize the super dict
        
        self.is_face_up = False
        #^bool to shadow certain data_attributes
        
        self.__front_face = self.create_face('front_face')
        self.__back_face = self.create_face('back_face')
        #^use create_face method to encapsulate each face of card

        
    def create_face(self, face):
        '''
        method : create_face
        arguments : string face
        return : dict
        method returns subdict if subdict exists 
        '''
        face_dict = self[face]
        if face_dict:
            return card_face(face_dict)
        return card_face({})
        
    
    def flip(self):
        '''
        method : flip
        arguments : None
        return : bool
        method "flips" the card from current state to 
        "flipped" state
        '''
        self.is_face_up = not self.is_face_up
        return self.read()
    
    def read(self):
        '''
        method : read
        arguments : None
        return : dict
        reads the side of the card that is faceing the viewer
        by the is_face_up object variable
        '''
        if self.is_face_up:
            return self.__front_face.read()
        return self.__back_face.read()
        
    def __missing__(self, key):
        '''
        method : __missing__
        arguments : var key
        return : False
        if a key is missing from a dict, will envoke this
        method and return false
        '''
        return False
    
    def __str__(self):
        '''
        method : __str__
        argumets : none
        return : str
        overwritten str method to ensure data encapsulation 
        of inherited dict object
        '''
        return self.read()

    def __repr__(self):
        '''
        '''
        return self.read()
        
class card_face(dict):
    '''
    this class represents the face of a single card
    '''
    def __init__(self, *args, **kwargs):
        '''initialize card object'''
        super(self.__class__, self).update(*args, **kwargs)
    def read(self):
        return self
        
        
if __name__ == "__main__":
    data = {
            'front_face':{
                'SUIT':'HEARTS',
                'value':10
                }
            }
    
    new_card = card(data)
    print "Card is created"
    
    print "reading full card"
    print new_card
    
    print "Reading card"
    print new_card.read()
    
    
    print "Fliping Card"
    new_card.flip()
    
    print "doing new read"
    print new_card.read()