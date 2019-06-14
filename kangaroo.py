def kangaroo(x1, v1, x2, v2):
    try:
        k = (x1-x2)/(v2-v1)
    except:
        return 'NO'
    return 'YES' if k == int(k) and k > 0  else 'NO'

print(kangaroo(0, 2, 5, 3))