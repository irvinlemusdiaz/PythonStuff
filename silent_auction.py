#todo-1 ask the user for inputs

#todo-2 save data in a dictionary

#toodo-3 ask if there are more bidders

#todo-4 compare bids and find the highest bidder
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)  # Clear the screen for the next bidder



