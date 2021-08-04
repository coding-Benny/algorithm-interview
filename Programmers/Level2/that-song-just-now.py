# https://programmers.co.kr/learn/courses/30/lessons/17683
from datetime import datetime


def transcode(sheet):
    return sheet.replace('C#', 'c').replace('D#', 'd').replace('E#', 'e')\
        .replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


def solution(m, musicinfos):
    answer = []
    m = transcode(m)

    for music in musicinfos:
        music_info = music.split(",")
        start, end, title, sheet = music_info[0], music_info[1], music_info[2], music_info[3]

        sheet = transcode(sheet)

        fmt = '%H:%M'
        play_time = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
        play_time = play_time.seconds // 60
        duration = len(sheet)

        if play_time % duration == 0:
            melody = sheet * (play_time // duration)
        else:
            melody = sheet * (play_time // duration) + sheet[:play_time % duration]

        if m in melody:
            answer.append((title, play_time))

    if not answer:
        return '(None)'
    elif len(answer) >= 2:
        answer.sort(key=lambda song: song[1], reverse=True)

    return answer[0][0]


def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s


def solution2(m, musicinfos):
    answer = [0, '(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]:
            answer = [time_length, title]
    return answer[-1]


def main():
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))  # HELLO
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))  # FOO
    print(solution2("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))  # WORLD


if __name__ == '__main__':
    main()
