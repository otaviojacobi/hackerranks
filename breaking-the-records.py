def breakingRecords(scores):
    breaks = [0, 0]
    mini = scores.pop(0)
    maxi = mini
    maxi_break = 0
    mini_break = 0
    for score in scores:
        if score > maxi:
            maxi = score
            maxi_break += 1
        if score < mini:
            mini = score
            mini_break += 1
    
    return [maxi_break, mini_break]

print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))