'''Sort
Написати функцію що вміє сортувати список чисел по порядку.'''

def srt(*num):
    return sorted(num)

from sort import srt

def test_srt_good():
    assert srt(1,2,3) = 1, 2, 3