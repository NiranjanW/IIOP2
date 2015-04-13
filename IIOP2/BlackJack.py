__author__ = 'itnxw'
# Mini-project #6 - Blackjack

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player_hand, dealer_hand ='', ''
wins = 0
losses = 0
deck= None


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.hand_card = []
        #self.top_left_pos = pos


    def __str__(self):
       for idx in range(len(self.hand_card)):
           return str(self.hand_card[idx])

    def add_card(self, card):
       self.hand_card.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value =0
        for idx in self.hand_card:
            value += VALUES.get(idx.get_rank())
            if idx.get_rank != 'A':
                return value
            else:
                if value +10 <=21 :
                   return value + 10
                else:
                   return value


    # def draw(self, canvas, pos):
    #     # draw a hand on the canvas, use the draw method for cards
    #     # for card in self.hand_card:
    #     #     card.draw(canvas,pos)
    #     self.top_left_pos = pos
    #     # i = 0
        # # if in play, draw cover for first position
        # for card in self.hand_card:
        #         i += 1
        #         if i > 1:
        #             card.draw(canvas, [pos[0]+(CARD_SIZE[0]+10)*(i-1), pos[1]])
        #         else:
        #             for car in self.hand_card:
        #                 i +=1
        #                 card.draw(canvas, [pos[0]+(CARD_SIZE[0]+10)*(i-1), pos[1]])
        # if cover:
        #     for card in self.cards:
        #         i += 1
        #         if i > 1:
        #             card.draw(canvas, [pos[0]+(CARD_SIZE[0]+10)*(i-1), pos[1]])
        # else:
        #     for card in self.cards:
        #         i += 1
        #         card.draw(canvas, [pos[0]+(CARD_SIZE[0]+10)*(i-1), pos[1]])


    def draw(self, canvas, cover, pos):
        i = 0
        # if in play, draw cover for first position
        if cover:
            for card in self.hand_card:
                i += 1
                if i > 1:
                    card.draw(canvas, [pos[0]+(CARD_SIZE[0]+10)*(i-1), pos[1]])
        else:
            for card in self.hand_card:
                i += 1
                card.draw(canvas, [pos[0]+(CARD_SIZE[0]+10)*(i-1), pos[1]])
    # def draw(self, canvas):
    #    #self.top_left_pos = pos
    #    for i, c in enumerate(self.hand_card):
    #        c.draw(canvas, [self.top_left_pos[0] + CARD_SIZE[0] * i, self.top_left_pos[1]])
# define deck class
class Deck:
    #global deck
    def __init__(self):

        # create a Deck object
        self.deck =[]
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                card = Card(SUITS[i],RANKS[j])
                self.deck.append(card)



    def shuffle(self):
        # shuffle the deck
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        #return random.choice(self.deck)
        return self.deck.pop()

    def __str__(self):
        # return a string representing the deck
        ans =''
        for i in range(len(self.deck)):
            deck_card = self.deck[i]
            ans += str(deck_card) + ' '
        return ans



#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand,dealer_hand

    global outcome, prompt, wins, losses, in_play, deck, dealer_hand, player_hand
    outcome = ""
    if in_play:
        losses += 1
    else:
        in_play = True
    deck = Deck()
    deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    in_play = True
    prompt = "Hit or stand?"

def hit():
    pass	# replace with your code below

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

def stand():
    pass	# replace with your code below

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    global  player_hand , dealer_hand, in_play, losses

    if in_play:
        losses += 1
    else:
        in_play = True
    canvas.draw_text('Black Jack', (50,50),24 ,'Black')
    if in_play:
        dealer_hand.draw(canvas, True, [100,100])
        canvas.draw_image(card_back, (CARD_CENTER[0], CARD_CENTER[1]), CARD_SIZE, [100 + CARD_CENTER[0], 100 + CARD_CENTER[1]], CARD_SIZE)
    else:
        # show hole card if player hand not in play
        dealer_hand.draw(canvas, False, [100,100])
        # draw dealer_hand value
        canvas.draw_text("("+str(dealer_hand.get_value())+")", (60, 150), 18, 'White', 'serif')
    player_hand.draw(canvas, False, [100,400])
    # draw player_hand value
    canvas.draw_text("("+str(player_hand.get_value())+")", (60, 450), 18, 'White', 'serif')
    # card = Card("D", "2")
    # #card.draw(canvas, [300, 300])
    # deck = Deck()
    # deck.shuffle()
    # player_hand = Hand((150,150))
    # #for i in range(2):
    # play_card = deck.deal_card()
    # player_hand.add_card(play_card)
    # player_hand.draw(canvas)
    # #player_hand.draw(canvas , (150,150))

    in_play = True


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)

frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)

frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
