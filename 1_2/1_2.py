if __name__ == "__main__":
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    third_sum = 0
    second_sum = 0
    first_sum = 0
    current_sum = 0
    for val in inputs:
        if val == "\n":
            if current_sum > first_sum:
                third_sum = second_sum
                second_sum = first_sum
                first_sum = current_sum
            elif current_sum > second_sum:
                third_sum = second_sum
                second_sum = current_sum
            elif current_sum > third_sum:
                third_sum = current_sum
            current_sum = 0
        else:
            current_sum += int(val)

    print(first_sum + second_sum + third_sum)
