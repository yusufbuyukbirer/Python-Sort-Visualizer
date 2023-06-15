from colors import *
import time


def merge(numbers, start, middle, end, drawData, timeTick):
    p = start
    q = middle + 1
    tempArray = []

    for i in range(start, end + 1):
        if p > middle:
            tempArray.append(numbers[q])
            q += 1
        elif q > end:
            tempArray.append(numbers[p])
            p += 1
        elif numbers[p] < numbers[q]:
            tempArray.append(numbers[p])
            p += 1
        else:
            tempArray.append(numbers[q])
            q += 1

    for p in range(len(tempArray)):
        numbers[start] = tempArray[p]
        start += 1


def mergeSort(numbers, start, end, drawData, timeTick):
    if start < end:
        middle = int((start + end) / 2)
        mergeSort(numbers, start, middle, drawData, timeTick)
        mergeSort(numbers, middle + 1, end, drawData, timeTick)

        merge(numbers, start, middle, end, drawData, timeTick)

        drawData(numbers, [PURPLE if x >= start and x < middle else YELLOW if x == middle
        else DARK_BLUE if x > middle and x <= end else BLUE for x in range(len(numbers))])
        time.sleep(timeTick)

    drawData(numbers, [BLUE for x in range(len(numbers))])
