import os

def find_highest_bidder(list):
    highest_bid = 0
    highest_bidder = 0
    for index, item in enumerate(bids):
        if item["bid"] > highest_bid:
            highest_bid = item["bid"]
            highest_bidder = index
    print(f"Auction won by {bids[highest_bidder]['name']} with ${bids[highest_bidder]['bid']}")

print("Welcome to the secret auction program.")
bids = []
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))
    other_bidders = input("Are there any other bidders? (yes/no)").lower()
    bids.append({"name": name, "bid": bid})
    if other_bidders == "no":
        find_highest_bidder(bids)
        bidding_finished = True
    else:
        os.system('clear')
