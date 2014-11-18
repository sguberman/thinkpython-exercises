import random

class Card(object):
    '''
    Represents a standard playing card.
    '''
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    
    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)
    
    
class Deck(object):
    '''
    Represents a standard deck of 52 playing cards.
    '''
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort()
    
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    
    def deal_hands(self, num_hands, num_cards):
        hands = []
        for i in range(num_hands):
            h = Hand('Hand %d' % i)
            self.move_cards(h, num_cards)
            hands.append(h)
        return hands


class Hand(Deck):
    '''
    Represents a hand of playing cards.
    '''
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def test_Card():
    print 'Testing Card() init and str...'
    card1 = Card(2, 11)
    print card1

def test_Deck():
    print 'Testing Deck() init and str...'
    deck = Deck()
    print deck

def test_Hand():
    print 'Testing Hand() init and str...'
    hand = Hand('new hand')
    print 'cards: ', hand.cards
    print 'label: ', hand.label

def test_deal_hands():
    deck = Deck()
    deck.shuffle()
    hands = deck.deal_hands(3, 5)
    for hand in hands:
        print hand.label
        print hand

def main():
    test_Card()
    test_Deck()
    test_Hand()
    test_deal_hands()

if __name__ == '__main__':
    main()
