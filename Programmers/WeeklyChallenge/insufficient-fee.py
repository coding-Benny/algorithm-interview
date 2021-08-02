def get_insufficient_money(price: int, money: int, count: int) -> int:
    fee = 0
    for i in range(1, count + 1):
        fee += price * i
    return fee - money if fee > money else 0


def solution(price, money, count):
    return abs(min(money - sum([price * i for i in range(1, count + 1)]), 0))


def main():
    print(get_insufficient_money(3, 20, 4))
    print(solution(1, 10, 3))


if __name__ == '__main__':
    main()
