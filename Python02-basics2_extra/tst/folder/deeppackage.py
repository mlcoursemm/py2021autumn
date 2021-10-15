def myfunc1():
    print('My func 1')

def myfunc2(x, y=None):
    if y is not None:
        print(x, y)
    else:
        print(x)
    return
