def draw_box(l=5, b=10):
    for i in range(l):
        for j in range(b):
            print('*', end='')
        print()

draw_box(3, 4)
draw_box(8, 12)
