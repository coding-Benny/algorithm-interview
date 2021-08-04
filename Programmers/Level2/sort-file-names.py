import re


def split_part(files):
    # 각 구간을 |로 분리
    for idx, file in enumerate(files):
        for i, char in enumerate(file):
            if char.isdigit():
                char = '|' + char
                file = file[:i] + char + file[i + 1:]
                break

        count = 0
        for j, char in enumerate(file[i + 1:]):
            if char.isdigit():
                count += 1
            if not char.isdigit() or count > 5:
                char = '|' + char
                file = file[:i + 1] + file[i + 1:i + j + 1] + char + file[i + j + 2:]
                break

        files[idx] = file


def solution(files):
    split_part(files)

    # 기준에 따라 정렬
    files.sort(key=lambda name: (name.split('|')[0].lower(),
                                 int(name.split('|')[1])))

    # 구분자 제거
    for idx, file in enumerate(files):
        file = file.replace('|', '')
        files[idx] = file

    return files


def solution2(files):
    a = sorted(files, key=lambda file: int(re.findall('\d{1,5}', file)[0]))
    b = sorted(a, key=lambda file: re.split('\d{1,5}', file.lower())[0])
    return b


def main():
    # ["F-15", "foo9.txt", "foo010bar020.zip"]
    print(solution(["foo9.txt", "foo010bar020.zip", "F-15"]))
    # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
    print(solution2(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
    # ["img000012345", "img1.png","img2","IMG02"]
    print(solution2(["img000002345", "img1.png", "img2", "IMG02"]))


if __name__ == '__main__':
    main()
