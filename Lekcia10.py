# import time
# from functools import lru_cache
#
# def print_decorator(func):
#     def wrapper():
#         print("START")
#         func()
#         print("END")
#     return wrapper
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print('Time elapsed: {:f}'.format(end - start))
#         return result
#     return wrapper
#
# @timer
# def test():
#     x = 1
#     for i in range(10000000):
#         x += 100
#
# @timer
# def greetings_two():
#     print("hello world!")
#     print("NEW CHANGEs")
#     print("hello world!")
#     print("NEW CHANGEs")
#     print("hello world!")
#     print("NEW CHANGEs")
#     print("hello world!")
#     print("NEW CHANGEs")
#     print("hello world!")
#     print("NEW CHANGEs")
#     print("hello world!")
#     print("NEW CHANGEs")
#     print("hello world!")
#     print("NEW CHANGEs")
#
# @timer
# def greetings(name: str):
#     print("hello world!")
#     print(name)
#     print("NEW CHANGEs")
#
# greetings("Honza")
# greetings_two()
# test()
#
#
#
# def test_fnc(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# test_fnc(1,2,3, name="asd")
# test_fnc(1,2,3,4,5)
# test_fnc()
from email.policy import default
#
# import click
#
# @click.command()
# @click.option("--name", "-n", default="Unknown", help="Name of person")
# @click.option("--age", help="Age of person")
# def main(name, age):
#     print("Hello World")
#     print(f"This is {name}")
#     print(f"My age is: {age}")
#
# main()



def decorator(func):
    def wrapper(*args, **kwargs):
        print("START")
        func(*args, **kwargs)
        print("END")

    return wrapper

@decorator
def test(*args, **kwargs):
    print("test")
    print(args)
    print(kwargs)


test()
test(1,2,3,4)
test(a="aa")


# import click
#
# @click.command()
# @click.option("--name", default="Unknown", help="Name of person")
# def main(name):
#     print("Hello")
#     print(f"This is {name}")
#
#
# main()