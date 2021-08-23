# https://programmers.co.kr/learn/courses/30/lessons/72412


# my solution 40.0/100.0 - Accuracy is perfect, efficiency is 0 points :(
def solution(info, query):
    meets = []
    for q in query:
        q = [condition for condition in q.split() if condition != "and"]
        dev = [developer for developer in info
               if (developer.split()[0] == q[0] or q[0] == '-')
               and (developer.split()[1] == q[1] or q[1] == '-')
               and (developer.split()[2] == q[2] or q[2] == '-')
               and (developer.split()[3] == q[3] or q[3] == '-')
               and (int(developer.split()[4]) >= int(q[4]))]
        meets.append(len(dev))
    return meets


def main():
    print(
        solution(
            [
                "java backend junior pizza 150", "python frontend senior chicken 210",
                "python frontend senior chicken 150", "cpp backend senior pizza 260",
                "java backend junior chicken 80", "python backend senior chicken 50"
            ],
            [
                "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
                "- and - and - and chicken 100", "- and - and - and - 150"
            ]
        )
    )  # [1, 1, 1, 1, 2, 4]


if __name__ == '__main__':
    main()
