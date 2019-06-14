def stdev(a):
    length = len(a)
    sum = 0
    for i in range(length):
        sum += a[i]
    average = sum/length

    squared_diff = []
    for i in range(length):
        squared_diff.append((a[i] - average)**2)


    sum2 = 0
    avg2 = 0
    for i in range(length):
        sum2 += squared_diff[i]

    avg2 = sum2/length

    std_dev = avg2**(0.5)

    print("Standard deviation, average, number of terms")
    return std_dev,average,length

def zedscore(score, std_dev, avg):
    return ((score - avg)/std_dev)
