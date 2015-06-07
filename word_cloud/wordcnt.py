import sys


def calc_word_cnt(file_name):
    all_lines = open(file_name, mode='r').readlines()

    word_cnt = {}

    for line in all_lines:
        items = line.split()
        for itm in items:
            if itm in word_cnt:
                word_cnt[itm] = word_cnt[itm] + 1
            else:
                word_cnt[itm] = 1

    # print(word_cnt)

    for word, cnt in word_cnt.items():
        if len(word) >= 2 and cnt >= 7:
            print(word, ', ', cnt)


if __name__ == '__main__':
    filename = sys.argv[1]
    print("parsing file: " + filename)
    calc_word_cnt(filename)
