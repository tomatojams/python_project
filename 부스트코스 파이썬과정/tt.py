import timeit


def test():
    dict_first = {'사과': 30, '배': 15, '감':10, '포도':10}
    dictnew = dict_first.copy()

t1 = timeit.timeit('test()', setup='from __main__ import test', number=10000)
print(t1)