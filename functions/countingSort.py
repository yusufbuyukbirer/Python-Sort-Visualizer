import time

def countingSort(numbers, drawData, timeTick):
    n = max(numbers) + 1
    count = [0] * n

    for item in numbers:
        count[item] += 1


    k = 0

    for i in range(n):
        for j in range(count[i]):
            numbers[k] = i
            drawData(numbers)
            time.sleep(timeTick)
            k += 1

    drawData(numbers)            