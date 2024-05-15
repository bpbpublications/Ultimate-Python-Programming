heights = [12, 45, 78, 77, 12, 14, 54]
heights_cm = [ht * 2.54 for ht in heights]
print(heights_cm)

weights = [2900, 3450, 6678, 2348, 800, 8999, 90]
wts = [(wt // 1000, wt % 1000) for wt in weights]
print(wts)

L1 = [t[0] * 1000 + t[1] for t in wts]
print(L1)

L2 = [kg * 1000 + gm for kg, gm in wts]
print(L2)
