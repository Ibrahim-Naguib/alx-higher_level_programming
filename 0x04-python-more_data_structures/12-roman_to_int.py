#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    num = 0
    for i in reversed(roman_string):
        num = roman_nums[i]
        if total < num * 5:
            total += num
        else:
            total -= num
    return total