import random

class Card:
    """A simple Card class to represent a playing card."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """A Deck class to represent a deck of 52 playing cards."""

    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {
        'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
        'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
    }

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in Deck.suits for rank in Deck.ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    """A Hand class to represent a player's hand of cards."""

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += Deck.values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def blackjack():
    """Main function to play a simple game of Blackjack."""

    def take_bet():
        """Prompt the player for their bet."""
        while True:
            try:
                bet = int(input("How much would you like to bet? "))
                return bet
            except ValueError:
                print("Invalid input. Please enter a number.")

    def hit(deck, hand):
        """Deal a card to the player's hand and adjust for aces."""
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    def show_hand(player, dealer, hide_dealer_card=True):
        """Display the player's and dealer's hands."""
        print("\nDealer's hand:")
        if hide_dealer_card:
            print("<card hidden>")
            print(dealer.cards[1])
        else:
            for card in dealer.cards:
                print(card)
        print("\nPlayer's hand:")
        for card in player.cards:
            print(card)

    # Initialize deck and shuffle
    deck = Deck()
    deck.shuffle()

    # Initialize player and dealer hands
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal two cards to each
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Take bet from player
    player_bet = take_bet()

    # Show initial hands
    show_hand(player_hand, dealer_hand)

    # Player's turn
    while True:
        action = input("\nDo you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            hit(deck, player_hand)
            show_hand(player_hand, dealer_hand)
            if player_hand.value > 21:
                print("\nPlayer busts! You lose.")
                return
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    # Dealer's turn
    while dealer_hand.value < 17:
        hit(deck, dealer_hand)

    # Show final hands
    show_hand(player_hand, dealer_hand, hide_dealer_card=False)

    # Determine outcome
    if dealer_hand.value > 21 or player_hand.value > dealer_hand.value:
        print("\nPlayer wins!")
    elif player_hand.value < dealer_hand.value:
        print("\nDealer wins! You lose.")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    blackjack()
