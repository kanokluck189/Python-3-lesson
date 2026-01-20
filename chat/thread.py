from threading import Thread

t = 1

def test_func_1():
    global t
    for i in range(10000000000):
        # print(".", end="")
        t += 1

def test_func_2():
    global t
    for i in range(10000000000):
        # print("+", end="")
        t -= 1

def test_func_3():
    for i in range(10000000):
        print(t, end=" ")

t1 = Thread(target=test_func_1)
t2 = Thread(target=test_func_2)
t3 = Thread(target=test_func_3)
t4 = Thread(target=test_func_1)
t5 = Thread(target=test_func_2)
t6 = Thread(target=test_func_1)
t7 = Thread(target=test_func_2)

t3.start()
t1.start()
t2.start()
t4.start()
t5.start()
t6.start()
t7.start()

# GIL - Global Interpreter Lock

# IO - bound operations / CPU bound operations