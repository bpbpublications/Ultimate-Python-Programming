L = ['Ruby', 'C++', 'Python', 'JavaScript', 'C#', 'Java']
maximum = minimum = len(L[0])
longest_string = shortest_string = L[0]
for s in L:
    if len(s) > maximum:
        maximum = len(s)
        longest_string = s
    if len(s) < minimum:
        minimum = len(s)
        shortest_string = s
print(f'Longest : {longest_string}, Shortest : {shortest_string}')

# Longest and shortest strings can also be found out by providing the len function
# as argument to the key parameter in the max and min functions.
longest_string = max(L, key=len)
shortest_string = min(L, key=len)
print(f'Longest : {longest_string}, Shortest : {shortest_string}')
