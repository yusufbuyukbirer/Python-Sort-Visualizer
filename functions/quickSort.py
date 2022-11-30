import time

def num_partiton(numbers, start, end, drawData, timeTick):
    i = start + 1
    pivot = numbers[start]

    for j in range(start + 1, end + 1):
        if numbers[j] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
    numbers[start], numbers[i - 1] = numbers[i - 1], numbers[start]
    return i - 1

def quickSort(numbers, start, end, drawData, timeTick):
    if start < end:
        pivotSpot = num_partiton(numbers, start, end, drawData, timeTick)
        quickSort(numbers, start, pivotSpot - 1, drawData, timeTick)
        quickSort(numbers, pivotSpot + 1, end, drawData, timeTick)

        drawData(numbers)
        time.sleep(timeTick)

    drawData(numbers)         