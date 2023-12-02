if __name__ == "__main__":
    _WIN = 6
    _DRAW = 3
    _LOSE = 0

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

    drawing_hands = {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }

    losing_hands = {
        "A": "Z",
        "B": "X",
        "C": "Y",
    }

    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    total_points = 0
    for line in inputs:
        opp_hand, round_end = line.strip().split(" ")

        if round_end == "X":
            total_points += (_LOSE + my_scores.get(losing_hands.get(opp_hand)))
        elif round_end == "Y":
            total_points += (_DRAW + my_scores.get(drawing_hands.get(opp_hand)))
        else:
            total_points += (_WIN + my_scores.get(winning_hands.get(opp_hand)))

    print(total_points)
