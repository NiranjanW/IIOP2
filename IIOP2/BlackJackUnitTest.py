__author__ = 'itnxw'

# Testing template for the Hand class


import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card(object):
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    # def draw(self, canvas, pos):
    #     card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
    #     canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


#####################################################
# Student should insert code for Hand class here
in_play = True
outcome = ""
score = 0
player_hand =""
dealer_hand=""

class Hand(object):
    def __init__(self):

        self.hand_card = []




    # def __str__(self):
    #    ans =''
    #    x = "Hands contain".join(self.hand_card[idx] for idx in range(len(self.hand_card)))
    #    for idx in range(len(self.hand_card)):
    #         card_out = self.hand_card[idx]
    #         ans += ' ' +str(card_out)
    #        # if not self.hand_card :
    #        #     return self.hand_card
    #        # else:
    #        #     card_out = self.hand_card[idx]
    #        # #ans = "Hands contain".join(self.hand_card[idx])
    #        #     ans += ' ' +str(card_out)
    #    return  "Hand contains" + ans
    #

    def __str__(self):
       #hand = str(self.hand_card)
       ans ='' #(self.hand_card)
       #x = "Hands contain".join(self.hand_card[idx] for idx in range(len(self.hand_card)))
       for idx in range(len(self.hand_card)):

           if not self.hand_card :
               return str([Card][0])
           else:
               card_out = self.hand_card[idx]
           #ans = "Hands contain".join(self.hand_card[idx])h
               ans += ' ' +str(card_out)
       return  "Hand contains" + ans

    def add_card(self, card):
        self.hand_card.append(card)
        #self.hand_card.extend(card)

    # def get_value(self):
    #     hand_value = 0
    #     for i in self.hand:
    #         hand_value += VALUES.get(i.get_rank())
    #         if i.get_rank() != 'A':
    #             return hand_value
    #         else:
    #             if hand_value + 10 <= 21:
    #                 return hand_value + 10
    #             else (returns hand_value)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        card_sum =0
        # for i in range(len(self.hand_card)):
        #     card_sum += VALUES[self.hand_card[i].get_rank()]

        for id in self.hand_card:
            value += VALUES.get(id.get_rank())

        return value
        #print card_sum
           # card_value = VALUES[self.hand_card[id].get_rank()]
           # value += card_value

        #return  card_sum

    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards

class Deck(object):
    def __init__(self):
       self.deck_hand = []
       for a in range(len(SUITS)):
           for b in range(len(RANKS)):
               card = Card(SUITS[a],RANKS[b])
               self.deck_hand.append(card)

    def __str__(self):
        ans =''
        for i in range(len(self.deck_hand)):
            deck_card = self.deck_hand[i]
            ans += str(deck_card) + ' '
        return ans


    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck_hand)

    def deal_card(self):
       return  random.choice(self.deck_hand)


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand , dealer_hand
    player_hand = Hand()
    dealer_hand = Hand()
    deck = Deck ()
    deck.shuffle()
    for i in range(2):
        player_hand.add_card(deck.deal_card())
        #deck.deck_hand.pop(player_hand[i])
        dealer_hand.add_card( deck.deal_card())

    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            print player_hand
        else :
            print 'BUST'
            in_play = False

    print player_hand.get_value() , dealer_hand.get_value()
    return   str(player_hand) ,  str(dealer_hand)


       #, player_hand.get_value

def hit():
    pass	# replace with your code below

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

def stand():
    pass	# replace with your code below

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
###################################################
# Test Deck code
######################################################
# test_deck = Deck()
# print test_deck
# print type(test_deck)
#
# c1 = test_deck.deal_card()
# print c1
# print type(c1)
# #print test_deck
#
# c2 = test_deck.deal_card()
# print c2
# print type(c2)
# #print test_deck
#
# test_deck = Deck()
# print test_deck
# test_deck.shuffle()
# #print test_deck
# print type(test_deck)
#
# c3 = test_deck.deal_card()
# print c3
# print type(c3)
# print test_deck
print '**************'
print deal()


###################################################
# Output to console
# output of string method for decks depends on your implementation of __str__
# note the output of shuffling is randomized so the exact order of cards
# need not match

#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK
#<class '__main__.Deck'>
#DK
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ
#DQ
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 H5
#<class '__main__.Deck'>
#H5
#<class '__main__.Card'>
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3






###################################################
# Test Hand code
#############################################
# c1 = Card("S", "A")
# c2 = Card("C", "2")
# c3 = Card("D", "T")
# print c1, c2, c3
# print type(c1), type(c2), type(c3)

# test_hand = Hand()
# #print test_hand
#
#
# test_hand.add_card(c1)
# #print test_hand
#
#
# test_hand.add_card(c2)
# #print test_hand
#
# test_hand.add_card(c3)
# #print test_hand
#
# #print type(test_hand)
# print test_hand.get_value()


###################################################
# Output to console
# note that the string representation of a hand will
# vary based on how you implemented the __str__ method

#SA C2 DT
#<class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
#Hand contains
#Hand contains SA
#Hand contains SA C2
#Hand contains SA C2 DT
#<class '__main__.Hand'>