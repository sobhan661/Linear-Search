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
# A tool for testing function with more visibility and it's easier to understand
# ----------------------------------------------------------------------------------

def result_test(tests):
    """
    A function that makes testing and its results easier
    """
    all_results = []
    for test_name, test in tests.items():
        results = []
        if locate_card(**test["inputs"]) == test["output"]:
            results.append(f"Test '{test_name}': {locate_card(**test['inputs'])}")
            results.append("Passes!")
        else:
            results.append(f"Test '{test_name}': {locate_card(**test['inputs'])}")
            results.append("Failed")
        all_results.append(results)

    # Print results for better visibility
    for result in all_results:
        print(" | ".join(result))

# ----------------------------------------------------------------------------------
# Program : Linear Search
# ----------------------------------------------------------------------------------

def locate_card(cards, query):
    """Simple linear search usage program that finds the wanted number using linear search"""
    # This variable here stores the index number 
    position = 0 
    for card in cards:
        if card == query:
            return position
        else:
            position += 1

# ----------------------------------------------------------------------------------
# Testing With Tool
# ----------------------------------------------------------------------------------

result_test(tests)

# ----------------------------------------------------------------------------------
# Notes : If you have any other testing possibility, I would be more than happy if you share it with community
# ----------------------------------------------------------------------------------