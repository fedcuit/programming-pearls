from collections import deque

__author__ = 'edfeng'

if __name__ == '__main__':
    d = deque("abcdefgh")
    d.rotate(-3)
    print ''.join(d)