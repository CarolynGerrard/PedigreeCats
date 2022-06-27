#
# def gen_int(n):
#     for i in range(n):
#         yield i
#
# def gen_2(gen):
#     for n in gen:
#         if n % 2:
#             yield n
#


def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a + b


if __name__ == "__main__":
    fib()

    #
    # for i in gen_2(gen_int(10)):
    #     print(i)
