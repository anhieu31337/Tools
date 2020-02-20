import sys


def to_lil_endian(sub_str):
    sub_str = sub_str[::-1]
    res = '0x'
    for c in sub_str:
        res += hex(ord(c))[2:]
    return res

def print_lil_endian(input_string):
    arr = []
    for i in range(0, len(input_string), 4):
        len_rest = len(input_string) - i
        if(len_rest > 4):
            len_rest = 4
        arr.append(to_lil_endian(input_string[i:i+len_rest]))

    for x in arr[::-1]:
        print('push '+ x) 

if __name__ == "__main__":
    if(len(sys.argv) is not 2):
        print('USAGE:')
        print('python 2little-endian.py [INPUT]')
        exit()

    input_string = sys.argv[1]
    print_lil_endian(input_string)
