def solution(numbers, hand):
    answer = ''

    pos_dictionary = {
        '1': [0, 0],
        '2': [0, 1],
        '3': [0, 2],
        '4': [1, 0],
        '5': [1, 1],
        '6': [1, 2],
        '7': [2, 0],
        '8': [2, 1],
        '9': [2, 2],
        '*': [3, 0],
        '0': [3, 1],
        '#': [3, 2]
    }

    l_pos = "*"
    r_pos = "#"

    for number in numbers:
        if number in [1, 4, 7]:
            l_pos = str(number)
            answer += 'L'

        elif number in [3, 6, 9]:
            r_pos = str(number)
            answer += 'R'

        else:
            l_dist = abs(pos_dictionary[str(number)][0] - pos_dictionary[l_pos][0]) + abs(pos_dictionary[str(number)][1] - pos_dictionary[l_pos][1])
            r_dist = abs(pos_dictionary[str(number)][0] - pos_dictionary[r_pos][0]) + abs(pos_dictionary[str(number)][1] - pos_dictionary[r_pos][1])

            if l_dist < r_dist:
                l_pos = str(number)
                answer += 'L'
            elif l_dist > r_dist:
                r_pos = str(number)
                answer += 'R'
            else:
                if hand == "right":
                    r_pos = str(number)
                    answer += 'R'
                else:
                    l_pos = str(number)
                    answer += 'L'

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))

