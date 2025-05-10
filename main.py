# ----------------------------------------------------------------------------------
# This is a simple example of how linear search works
# Imagine it's a card game and you are supposed to pick a card, 
# and you just start picking up cards until you reach the wanted card
# note : cards are in decreasing order
# ----------------------------------------------------------------------------------

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
    all_results = []  # List to store results of all test cases
    for test_name, test in tests.items():  # Iterate through each test case
        results = []  # Temporary list to store the result of the current test case
        # Call the locate_card function and compare its output with the expected output
        if locate_card(**test["inputs"]) == test["output"]:
            # If the output matches, append the test name and "Passes!" to results
            results.append(f"Test '{test_name}': {locate_card(**test['inputs'])}")
            results.append("Passes!")
        else:
            # If the output does not match, append the test name and "Failed" to results
            results.append(f"Test '{test_name}': {locate_card(**test['inputs'])}")
            results.append("Failed")
        all_results.append(results)  # Add the current test's results to the overall results list

    # Print results for better visibility
    for result in all_results:  # Iterate through all results
        print(" | ".join(result))  # Print each result as a formatted string

# ----------------------------------------------------------------------------------
# Program : Linear Search
# ----------------------------------------------------------------------------------

def locate_card(cards, query):
    """
    Simple linear search usage program that finds the wanted number using linear search
    """
    # This variable here stores the index number 
    position = 0 
    while position < len(cards):  # Loop until the end of the list
        if cards[position] == query:
            return position  # Return the position if the card matches the query
        position += 1  # Increment the position to check the next card
    return None  # Return None if the query is not found in the cards


# ----------------------------------------------------------------------------------
# Testing With Tool
# ----------------------------------------------------------------------------------

result_test(tests)

# ----------------------------------------------------------------------------------
# Notes : If you have any other testing possibility, I would be more than happy if you share it with community
# ----------------------------------------------------------------------------------