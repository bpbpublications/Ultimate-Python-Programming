with open('data.txt', 'r+') as f:
    lines = [line + '\n' for line in f]
    f.seek(0)
    f.writelines(lines)

# Another approach

# import os
#
# with open('data.txt', 'r') as f1:
#     with open('new.txt', 'w') as f2:
#         for line in f1:
#             f2.write(line + '\n')
# os.remove('data.txt')
# os.rename('new.txt', 'data.txt')
