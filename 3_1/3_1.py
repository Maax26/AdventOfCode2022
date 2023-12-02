if __name__ == "__main__":
    priority_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority = []

    for c in priority_string:
        priority.append(c)

    inputs = open("test_input.txt")

    total_priority = 0
    for line in inputs:
        comp_1 = line[:int(len(line)/2)]
        comp_2 = line[int(len(line)/2)]

        for c in comp_1:
            if c in comp_2:
                total_priority += (priority.index(c) + 1)
                break

    print(total_priority)