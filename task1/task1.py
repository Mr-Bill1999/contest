n, m = map(int, input().split())
iterator1 = 0
iterator2 = m - 1
start_massive = [i+1 for i in range(n)]
intervals = []

if m >= 2:
    while start_massive[len(start_massive)-1] != start_massive[0]:
        if len(start_massive[iterator1:iterator2+1]) == m:
            intervals.append(start_massive[iterator1:iterator2+1])
            iterator1 = iterator2
            iterator2 += m - 1
        else:
            for i in range(m - len(start_massive[iterator1:iterator2+1])):
                iterator2 = len(start_massive) - 1
                if start_massive[iterator2] < n:
                    start_massive.append(start_massive[iterator2] + 1)
                    iterator2 += 1
                elif start_massive[iterator2] == n:
                    start_massive.append(1)
                    iterator2 += 1

    intervals.append(start_massive[len(start_massive)-m:len(start_massive)])

    result = ''
    for i in range(len(intervals)):
        result += str(intervals[i][0])

    print(result)
elif m == 1:
    start_massive.append(start_massive[0])
    for i in range(len(start_massive)):
        print(start_massive[i], end='')
else:
    print(False)