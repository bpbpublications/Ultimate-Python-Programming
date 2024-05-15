class GetSquares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i * i
            i += 1


g = GetSquares(2, 9)
L = [4, 9, 16, 25, 36, 49, 64, 81]


def func(data):
    print(sum(data))
    for i in data:
        if i % 2 == 0:
            print(i, end=' ')
    print()


func(L)
func(g)


# def generate_squares(start, stop):
#     while start <= stop:
#         yield start * start
#         start += 1
#
# g = generate_squares(2, 9)
#
# L = [4, 9, 16, 25, 36, 49, 64, 81]
#
# def func(data):
#     print(sum(data))
#     for i in data:
#         if i % 2 == 0:
#             print(i, end=' ')
#     print()
#
# func(L)
# func(g)
