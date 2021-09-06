# https://programmers.co.kr/learn/courses/30/lessons/85002


# my solution
def solution(weights, head2head):
    win_rates, counts = [], [0] * len(weights)

    for competition in head2head:
        num_of_matches = competition.count('W') + competition.count('L')
        if num_of_matches == 0:
            win_rates.append(0)
        else:
            win_rates.append(competition.count('W') / num_of_matches * 100)

    for i in range(1, len(head2head)):
        for j in range(i):
            if head2head[i][j] == 'W':
                if weights[i] < weights[j]:
                    counts[i] += 1
            elif head2head[i][j] == 'L':
                if weights[j] < weights[i]:
                    counts[j] += 1

    return [boxer_info[0] for boxer_info in sorted(
        [(num + 1, win_rate, count, weight) for num, (win_rate, count, weight) in
         enumerate(zip(win_rates, counts, weights))],
        key=lambda boxer: (boxer[1], boxer[2], boxer[3]), reverse=True)]


def main():
    print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))  # [3, 4, 1, 2]
    print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))  # [2, 3, 1]
    print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))  # [2, 1, 3]


if __name__ == '__main__':
    main()
