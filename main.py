# This is a simple example of how linear search works
# Imagine it's a card game and you are supposed to pick a card, 
# and you just start picking up cards until you reach the wanted card
# note : cards are in decreasing order

tests = {
    "number in middle" : {
        "inputs" :{
            "cards" : [13, 11, 7, 5, 3],
            "query" : 7},
        "output" : 2
    },
    "number is the first element" : {
        "inputs" : {
            "cards" : [14, 12, 9, 7, 8],
            "query" : 14
        },
        "output" : 0
    },
    "number is the last element" : {
        "inputs" : {
            "cards" : [15, 14, 9, 8, 4, 2],
            "query" : 2
        },
        "output" : 5
    },
    "number is not in the cards" : {
        "inputs" : {
            "cards" : [9, 7, 6, 5, 2, 1],
            "query" : 3
        },
        "output" : None
    },
    "there are many same numbers in cards" : {
        "inputs" : {
            "cards" : [14, 14, 14, 14, 14, 13, 12, 9, 9, 9, 9],
            "query" : 9
        },
        "output" : 7
    },
    "there is only 1 card and thats the correct card" : {
        "inputs" : {
            "cards" : [5],
            "query" : 5
        },
        "output" : 0
    },
    "there are no cards at all" : {
        "inputs" : {
            "cards" : [],
            "query" : 3
        },
        "output" : None
    }
}
# ----------------------------------------------------------------------------------
# Program : Linear Search
# ----------------------------------------------------------------------------------


def locate_card(cards, query):
    position = 0
    for card in cards:
        if card == query:
            return position
        else:
            position += 1


# ----------------------------------------------------------------------------------
# Testings
# ----------------------------------------------------------------------------------

print(locate_card(**tests["number in middle"]["inputs"]))
print(locate_card(**tests["number is not in the cards"]["inputs"]))
print(locate_card(**tests["number is the first element"]["inputs"]))
print(locate_card(**tests["number is the last element"]["inputs"]))
print(locate_card(**tests["there are many same numbers in cards"]["inputs"]))
print(locate_card(**tests["there are no cards at all"]["inputs"]))
print(locate_card(**tests["there is only 1 card and thats the correct card"]["inputs"]))


# ----------------------------------------------------------------------------------
# Notes : If you have any other testing possibility, I would be more than happy if you share it with community
# ----------------------------------------------------------------------------------
