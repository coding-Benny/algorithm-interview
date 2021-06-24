import re


def solution(new_id: str) -> str:
    # 1. 모든 대문자를 소문자로 변환
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub(r'[^0-9a-zA-Z._-]', '', new_id)
    # 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub(r'[.][.]+', '.', new_id)
    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id = new_id.lstrip('.').rstrip('.')
    # 5. 빈 문자열이라면, new_id에 "a"를 대입
    if not new_id:
        new_id = 'a'
    # 6. 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    #    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    # 7. 길이가 2자 이하라면, id의 마지막 문자를 id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id


if __name__ == '__main__':
    res = solution("...!@BaT#*..y.abcdefghijklm")
    print(res)
    res = solution("z-+.^.")
    print(res)
    res = solution("=.=")
    print(res)
    res = solution("123_.def")
    print(res)
    res = solution("abcdefghijklmn.p")
    print(res)
