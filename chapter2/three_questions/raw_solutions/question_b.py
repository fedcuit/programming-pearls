from collections import deque

__author__ = 'edfeng'


def solution1(s, t):
    d = deque(s)
    d.rotate(t)
    return ''.join(d)


def solution2(s, t):
    return s[-t:] + s[:-t]


if __name__ == '__main__':
    assert solution1("abcdefgh", -3) == "defghabc"
    assert solution1("abcdefgh", 3) == "fghabcde"
    assert solution2("abcdefgh", -3) == "defghabc"
    assert solution2("abcdefgh", 3) == "fghabcde"