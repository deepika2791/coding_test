import re
import sys
import copy

lines = sys.stdin.readlines()
lines = [line for line in lines if line.strip()]
output_lines = copy.deepcopy(lines)
bullet = []
pattern1 = re.compile('^\*+')
pattern2 = re.compile('^\.+')

def get_number(string):
    '''
    :param string: prefix stars
    :return: bullet number string
    '''
    global bullet
    len1 = len(string)
    len2 = len(bullet)

    if len1 == len2:
        bullet[-1] += 1
    elif len2 < len1:
        bullet[len2:len1] = [1] * (len1 - len2)
    else:
        bullet[len1 - 1] += 1
        bullet = bullet[:len1]
    return (".".join(map(str, bullet)))


def get_sign(curr_str, prev_str):
    '''
    :param curr_str: prefix dot string in current line
    :param prev_str: prefix dot string in previous line
    :return: return suitable listing for line
    '''
    len1 = len(prev_str)
    if len(curr_str) > len1:
        temp = " " *(len1+1) + "+"
    else:
        temp = " " * (len1+1) + "-"
    return temp


last_index = None
for index, line in enumerate(lines):
    obj = pattern1.search(line)
    sign_obj = pattern2.search(line)
    if obj:
        prev_dots = ''
        dots_count = 0
        stars = obj.group()
        bullet_str = get_number(stars)
        temp_line = pattern1.sub(bullet_str, line)
        output_lines[index] = temp_line

    elif sign_obj:
        dots = sign_obj.group()
        if dots_count > 0:
            dots = sign_obj.group()
            sign_str = get_sign(dots, prev_dots)
            temp_line = pattern2.sub(sign_str, output_lines[last_index])
            output_lines[last_index] = temp_line
        last_index = index
        prev_dots = dots
        dots_count += 1
    elif len(line.strip()) > 0:
        temp_line = " "*(len(prev_dots)+2)+line
        output_lines[index] = temp_line

for index, line in enumerate(output_lines):
    sign_obj = pattern2.search(line)
    if sign_obj:
        dots = sign_obj.group()
        sign_str = " " * (len(dots)+1) + "-"
        line = pattern2.sub(sign_str, line)
        output_lines[index] = line

print("\n".join(output_lines))
