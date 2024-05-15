def max_min_avg(L):
    return max(L), min(L), sum(L) / len(L)


marks = [92, 76, 98, 67, 88, 92, 89]
maxmarks, minmarks, avgmarks = max_min_avg(marks)

annual_rain = [11, 2, 23, 11, 9, 2, 1, 23, 13, 3, 12, 20]
max_rain, min_rain, avg_rain = max_min_avg(annual_rain)

print(maxmarks, minmarks, avgmarks)
print(max_rain, min_rain, avg_rain)


q, r = divmod(11, 3)
print(q, r)