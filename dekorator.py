import time

def task_2(a):
    print("start task_2")
    yield "a"
    yield "aa"

def task_3(b):
    print("start task_3")
    yield "b"
    yield "bb"

def task_4(a, b):
    print("start task_4")
    yield "ab"
    yield "abab"

def test():
    # a = yield task_2(2)
    # b = yield task_3(2)
    # yield task_4(2, 8)
    yield task_2(2)
    yield task_3(2)
    yield task_4(2, 3)

for i in test():
    print("next")
    time.sleep(1)
    for j in i:
        time.sleep(1)
        print(j)
