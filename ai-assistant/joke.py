import random


def get_joke():
    jokes = [
        "I have a few jokes about unemployed people, but none of them work.",
        "I tried to make a pun about a vacuum, but it sucked.",
        "What’s the best way to make a tissue dance? Put a little boogie in it.",
        "I used to steal soap, but I’m clean now.",
        "My IQ test results came back—they were negative.",
    ]

    print("\n" + random.choice(jokes), end="\n\n")
