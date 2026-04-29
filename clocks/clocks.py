import time
import cursor
import sys
import datetime


zero = [
    "     __   ",
    "    |  |  ",
    "    |__|  "
]

one = [
    "          ",
    "       |  ",
    "       |  "
]

two = [
    "     __   ",
    "     __|  ",
    "    |__   "
]

three = [
    "     __   ",
    "     __|  ",
    "     __|  "
]

four = [
    "          ",
    "    |__|  ",
    "       |  "
]

five = [
    "     __   ",
    "    |__   ",
    "     __|  "
]

six = [
    "     __   ",
    "    |__   ",
    "    |__|  "
]

seven = [
    "     __   ",
    "       |  ",
    "       |  "
]

eight = [
    "     __   ",
    "    |__|  ",
    "    |__|  "
]

nine = [
    "     __   ",
    "    |__|  ",
    "     __|  "
]

def match(lst):
    match_lst = []

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            match lst[i][j]:
                case "0":
                    match_lst.append(zero)
                case "1":
                    match_lst.append(one)
                case "2":
                    match_lst.append(two)
                case "3":
                    match_lst.append(three)
                case "4":
                    match_lst.append(four)
                case "5":
                    match_lst.append(five)
                case "6":
                    match_lst.append(six)
                case "7":
                    match_lst.append(seven)
                case "8":
                    match_lst.append(eight)
                case "9":
                    match_lst.append(nine)

    return match_lst      


def draw(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] == 0:
            result.append("00")
        elif lst[i] < 10:
            result.append("0" + str(lst[i]))
        elif lst[i] >= 10:
            result.append(str(lst[i]))
    match_lst = match(result)

    sys.stdout.write(f"\033[{len(match_lst[0])}A")
    for i, row in enumerate(zip(*match_lst)):
        line = []
        for idx, part in enumerate(row): 
            line.append(part)
            if hour < 100:
                if (idx + 1) % 2 == 0 and idx != len(row) - 1 and i != 0:
                    line.append("   * ")
                elif (idx + 1) % 2 == 0 and idx != len(row) - 1 and i == 0:
                    line.append("     ")
            else:
                if idx+1 != 1:
                    if (idx + 1) % 2 != 0 and idx != len(row) - 1 and i != 0:
                        line.append("   * ")
                    elif (idx + 1) % 2 != 0 and idx != len(row) - 1 and i == 0:
                        line.append("     ")
        sys.stdout.write("".join(line) + "\n")

    sys.stdout.flush()
cursor.hide()
while True:

    mins = int(datetime.datetime.now().strftime("%H:%M:%S")[3:5])
    secs = int(datetime.datetime.now().strftime("%H:%M:%S")[6:8])
    hour = int(datetime.datetime.now().strftime("%H:%M:%S")[0:2])

    
    draw([hour, mins, secs])

    time.sleep(0.1)
