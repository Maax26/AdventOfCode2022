if __name__ == "__main__":
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    max_sum = 0
    current_sum = 0
    for val in inputs:
        if val == "\n":
            if current_sum > max_sum:
                max_sum = current_sum
            current_sum = 0
        else:
            current_sum += int(val)

    print(max_sum)