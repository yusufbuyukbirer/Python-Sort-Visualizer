import time

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