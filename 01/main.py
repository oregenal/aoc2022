#!/usr/bin/env python3
import sys

def decimal_sum(file):
    total = 0
    for line in file.readlines():
        result = 0
        for char in line:
            match char:
                case '2':
                    result = 2 + result*5
                case '1':
                    result = 1 + result*5
                case '0':
                    result = 0 + result*5
                case '-':
                    result = result*5 - 1
                case '=':
                    result = result*5 - 2
                case _:
                    break
        total += result
    return total

def snafu_number(number):
    snafu = ''
    while True:
        new_number = round(number / 5)
        modulo = number - new_number * 5
        number = new_number
        match modulo:
            case 2:
                snafu = '2' + snafu
            case 1:
                snafu = '1' + snafu
            case 0:
                snafu = '0' + snafu
            case -1:
                snafu = '-' +snafu
            case -2:
                snafu = '=' +snafu
            case _:
                break
        if number > -2 and number < 2: break
    return snafu

if __name__ == '__main__':
    if len(sys.argv) == 2:
        f = open(sys.argv[1])
        number = decimal_sum(f)
        print("Summ = ", number)
        print("SNAFU = ", snafu_number(number))
    else:
        print("Usage: " + sys.argv[0] + " <file_name.txt>")
