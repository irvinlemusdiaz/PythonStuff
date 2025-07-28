#create a dictionary or list to hold the cards and their values. Do know that unlike a normal deck of cards, you have unlimited cards in this game.
import random
def create_deck():
    deck = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    return deck

def deal_card(deck):
    card = random.choice(list(deck.keys()))
    return card, deck[card]

#handling aces is a bit tricky, as they can be worth either 1 or 11 points.
def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def display_hand(hand, hide_first_card=False):
    if hide_first_card:
        return ['??'] + hand[1:]
    return hand

def blackjack():
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Deal initial cards
    for _ in range(2):
        card, value = deal_card(deck)
        player_hand.append(value)
        card, value = deal_card(deck)
        dealer_hand.append(value)

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your hand: {display_hand(player_hand)} (Score: {player_score})")
        print(f"Dealer's hand: {display_hand(dealer_hand, hide_first_card=True)}")

        if player_score == 21:
            print("Blackjack! You win!")
            return
        elif player_score > 21:
            print("You went over 21! You lose!")
            return

        action = input("Type 'hit' to get another card, 'stand' to pass: ").lower()
        if action == 'hit':
            card, value = deal_card(deck)
            player_hand.append(value)
        elif action == 'stand':
            game_over = True
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")

    # Dealer's turn
    while dealer_score < 17:
        card, value = deal_card(deck)
        dealer_hand.append(value)
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {display_hand(player_hand)} (Score: {player_score})")
    print(f"Dealer's final hand: {display_hand(dealer_hand)} (Score: {dealer_score})")

    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("You lose!")
    else:
        print("It's a draw!")

blackjack()
