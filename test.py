# print((int(7.5)))
# n = 7.5
# print("true") if int(n) == n else print("false")
# x = [[], []]
# print(len(x))


import threading
import gc


def test_func(a):
    # very long work
    for i in (range(10000)):
        x = i
    print("Done")


var = 6
t = threading.Thread(target=test_func(var))
t.start()
del var
gc.collect()
t.join()
