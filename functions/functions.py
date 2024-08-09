from colors import *
import time


def bubbleSort(numbers, drawData, timeTick):
    size = len(numbers)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                drawData(numbers)
                time.sleep(timeTick)
    drawData(numbers)


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


def insertionSort(numbers, drawData, timeTick):
    index = range(1, len(numbers))
    for i in index:
        sortNumber = numbers[i]

        while numbers[i - 1] > sortNumber and i > 0:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            i -= 1
            drawData(numbers)
            time.sleep(timeTick)
    return numbers


def getSpace(space):
    space = (space * 10) // 13
    if space < 1:
        return 1
    return space


def combSort(numbers, drawData, timeTick):
    n = len(numbers)
    space = n
    swap = True

    while space != 1 or swap == 1:
        space = getSpace(space)
        swap = False

        for i in range(n - space):
            if numbers[i] > numbers[i + space]:
                numbers[i], numbers[i + space] = numbers[i + space], numbers[i]
                swap = True
                drawData(numbers)
                time.sleep(timeTick)

    return numbers


def heapify(numbers, n, i, drawData, timeTick):
    maxNumber = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and numbers[i] < numbers[left]:
        maxNumber = left

    if right < n and numbers[maxNumber] < numbers[right]:
        maxNumber = right

    if maxNumber != i:
        numbers[i], numbers[maxNumber] = numbers[maxNumber], numbers[i]
        heapify(numbers, n, maxNumber, drawData, timeTick)


def heapSort(numbers, drawData, timeTick):
    n = len(numbers)

    for i in range(n - 1, -1, -1):
        heapify(numbers, n, i, drawData, timeTick)

    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0, drawData, timeTick)
        drawData(numbers)
        time.sleep(timeTick)

    drawData(numbers)


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


def selectionSort(numbers, drawData, timeTick):
    for i in range(len(numbers) - 1):
        minimum = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[minimum]:
                minimum = j

        numbers[minimum], numbers[i] = numbers[i], numbers[minimum]
        drawData(numbers)
        time.sleep(timeTick)

    drawData(numbers)


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

        drawData(numbers)
        time.sleep(timeTick)

    drawData(numbers)


def shellSort(numbers, drawData, timeTick):
    n = len(numbers)
    space = n // 2

    while space > 0:
        for i in range(space, n):

            temp = numbers[i]
            j = i

            while j >= space and numbers[j - space] > temp:
                numbers[j] = numbers[j - space]
                j -= space

            numbers[j] = temp
        space //= 2
        drawData(numbers)
        time.sleep(timeTick)
    drawData(numbers)
