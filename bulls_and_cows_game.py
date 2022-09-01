numbers = []


def generator():
    for num in range(1234, 9877):
        unique_number = ''.join(set(str(num)))
        if len(str(num)) == len(unique_number) and '0' not in str(num):
            numbers.append(num)


def match(num_1, num_2):
    s1 = str(num_1)
    s2 = str(num_2)
    result = [0, 0]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == j:
                    result[0] += 1
                else:
                    result[1] += 1

    return result


generator()


def delete(num, res):
    global numbers
    lst = []
    for x in numbers:
        if match(num, x) == res:
            lst.append(x)
    numbers = lst


def gameplay():
    game_over = False
    turns = 0
    while not game_over:
        turns += 1
        print(f"My guess is {numbers[0]}")
        bulls = int(input("Num of bulls: "))
        if bulls == 4:
            break
        cows = int(input("Num of cows: "))
        delete(numbers[0], [bulls, cows])
    print(f"Game is Over! It took you {turns} attempts!")


gameplay()
