def getTotalX(a, b):
    # Write your code here
    X = 0
    for k in range(1, 10000):
        ak = 0
        bk = 0
        for an in a:
            if k % an == 0:
                ak += 1
        for bn in b:
            if bn % k == 0:
                bk += 1

        if ak == len(a) and bk == len(b):
            X += 1
    return X

print(getTotalX([2,3], [2,4]))
print(getTotalX([2,6], [24,36]))
print(getTotalX([2,4], [16,32, 96]))
