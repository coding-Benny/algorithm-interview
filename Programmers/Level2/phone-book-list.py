# https://programmers.co.kr/learn/courses/30/lessons/42577
# my solution 91.7/100.0(time over)
def solution(phone_book):
    for i, phone_number in enumerate(phone_book):
        prefix = [phone for phone in phone_book if phone_number in phone[:len(phone_number)] and phone != phone_number]

        if prefix:
            return False
    else:
        return True


# my solution 100.0/100.0
def solution2(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False
    else:
        return True


# another solution
def solution3(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# another solution
def solution4(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True


def main():
    print(solution(["119", "97674223", "1195524421"]))  # False
    print(solution2(["123", "456", "789"]))  # True
    print(solution2(["12", "123", "1235", "567", "88"]))  # False
    print(solution3(["12345", "25431", "12"]))  # False
    print(solution4(["113", "44", "4544"]))  # True


if __name__ == '__main__':
    main()
