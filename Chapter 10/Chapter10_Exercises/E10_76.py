def max_min_avg(*args):
    return max(args), min(args), sum(args) / len(args)

maximum, minimum, average = max_min_avg(3,5,6,7,8)
print(f'Maximum {maximum}, Minimum {minimum}, Average {average}')
