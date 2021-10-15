def mynewfunc1():
    print('My new func 1')

def mynewfunc2(x, y=None):
    if y is not None:
        print(x, y)
    else:
        print(x)
    return
