#HINT: You can call clear() to clear the output in the console.

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    # bid_dictionary = {}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        # print(bidder)
        bid_amount = bidding_record[bidder]
        print(bid_amount)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid amount of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price

    yesno = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if yesno == "no":
        bidding_finished = True
        find_highest_bidder(bids)