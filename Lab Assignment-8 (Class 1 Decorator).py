def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner
def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner
def pipe(func):
    def inner(*args, **kwargs):
        print("|" * 30)
        func(*args,**kwargs)
        print("|" * 30)
    return inner


@star
@pipe
@percent
def printer(msg):
    print(msg)

printer("Kshitij")
