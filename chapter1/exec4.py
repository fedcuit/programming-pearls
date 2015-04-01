__author__ = 'edfeng'

from random import randint
from time import time

N = 1000000


def new_file_with_tel_numbers(path):
    with open(path, 'w') as f:
        nums = list(xrange(1, N + 1))
        for i in xrange(1, N):
            target = randint(0, N - 1)
            nums[i], nums[target] = nums[target], nums[i]
        f.writelines(' '.join(map(str, nums)))


def timer(fnc):
    def wrapper(*args, **kwargs):
        start = time()
        result = fnc(*args, **kwargs)
        print 'Using {}, time used: {}'.format(fnc.__name__, time() - start)
        return result

    return wrapper


@timer
def sort_with_bitmap(nums):
    bitmap = [0] * (len(nums) + 1)
    for n in nums:
        bitmap[n] = 1
    return [i for i, n in enumerate(bitmap) if n == 1]


@timer
def sort_with_lib(nums):
    return sorted(nums)


def dump(path):
    with open(path, 'w') as f:
        f.writelines(str(with_lib))


if __name__ == '__main__':
    new_file_with_tel_numbers('tel_numbers.txt')
    with_lib = []
    with open('tel_numbers.txt', 'r') as f:
        nums = map(int, f.readline().split(' '))
        sort_with_bitmap(nums)
        with_lib = sort_with_lib(nums)

    dump('tel_numbers_with_lib.txt')
    dump('tel_numbers_with_bitmap.txt')