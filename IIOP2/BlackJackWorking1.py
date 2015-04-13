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
prompt = ""
bet = 1
wins = 0
losses = 0
dealer_hand = None
player_hand = None
deck = None

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
        # finds the card in the sprite
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        # draws an individual card
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        hand_str = "Hand contains"
        for i in self.cards:
            hand_str = hand_str+" "+str(i)
        return hand_str

    def add_card(self, card):
        return self.cards.append(card)

    def get_value(self):
        value = 0
        ace_in_hand = False
        # calculate minimum value
        for card in self.cards:
            value += VALUES[str(card)[1]]
        # check for aces
        for card in self.cards:
            if str(card)[1] == "A":
                ace_in_hand = True
        if not ace_in_hand:
            return value
        # if there is an ace, get highest value without busting
        if ace_in_hand:
            if value + 10 <= 21:
                return value + 10
            else:
                return value

    def draw(self, canvas, cover, pos):
        i = 0
        # if in play, draw cover for first position
        if cover:
            for card in self.cards:
                i += 1
                if i > 1:
                    card.draw(canvas, [pos[0]+(CARD_SIZE[0]+10)*(i-1), pos[1]])
        else:
            for card in self.cards:
                i += 1
                card.draw(canvas, [pos[0]+(CARD_SIZE[0]+10)*(i-1), pos[1]])

                    
# define deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        deck_str = "Deck contains"
        for card in self.cards:
            deck_str = deck_str+" "+str(card)
        return deck_str

#define event handlers for buttons
def deal():
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
    global outcome, prompt, wins, losses, in_play
    # if the hand is in play, hit the player
    if in_play and player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You busted"
            prompt = "Deal again?"
            in_play = False
            losses += 1

def stand():
    global outcome, prompt, wins, losses, in_play
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        in_play = False
        if dealer_hand.get_value() < 17:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = "Dealer busted. You win!"
            prompt = "Deal again?"
            wins += 1
        elif player_hand.get_value() > dealer_hand.get_value():
            outcome = "You win!"
            prompt = "Deal again?"
            wins += 1
        elif player_hand.get_value() == dealer_hand.get_value():
            outcome = "Dealer wins tie"
            prompt = "Deal again?"
            losses += 1
        else:
            outcome = "Dealer wins"
            prompt = "Deal again?"
            losses += 1

# draw handler
def draw(canvas):
    # draw name of game
    canvas.draw_text('Blackjack', (40, 60), 36, 'Yellow', 'serif')
    canvas.draw_text('Wins: ', (460, 30), 18, 'Yellow', 'serif')
    canvas.draw_text(str(wins), (540, 30), 18, 'Yellow', 'serif')
    canvas.draw_text('Losses: ', (460, 55), 18, 'Yellow', 'serif')
    canvas.draw_text(str(losses), (540, 55), 18, 'Yellow', 'serif')
    canvas.draw_text(outcome, (100, 285), 36, 'White', 'serif')
    canvas.draw_text(prompt, (100, 335), 36, 'White', 'serif')
    # cover hole card if player hand in play
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

# keyboard handler
def key_handler(key):
    if key == simplegui.KEY_MAP['d']:
        deal()
    elif key == simplegui.KEY_MAP['h']:
        hit()
    elif key == simplegui.KEY_MAP['s']:
        stand()

# set bet
def set_bet(value):
    global bet
    bet = int(value)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_label('')
frame.add_label('')
frame.add_button("Deal (D)", deal, 200)
frame.add_label('')
frame.add_label('')
frame.add_button("Hit (H)",  hit, 200)
frame.add_label('')
frame.add_label('')
frame.add_button("Stand (S)", stand, 200)

frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric
