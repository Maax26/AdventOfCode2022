if __name__ == "__main__":
    _WIN = 6
    _DRAW = 3
    _LOSE = 0

    opp_scores = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    my_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    winning_hands = {
        "A": "Y",
        "B": "Z",
        "C": "X",
    }

    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    total_points = 0
    for line in inputs:
        opp_hand, my_hand = line.strip().split(" ")
        opp_score = opp_scores.get(opp_hand, 0)
        my_score = my_scores.get(my_hand, 0)

        if winning_hands.get(opp_hand) == my_hand:
            total_points += (my_score + _WIN)
        elif my_score == opp_score:
            total_points += (my_score + _DRAW)
        else:
            total_points += (my_score + _LOSE)

    print(total_points)
