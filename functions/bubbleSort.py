import time

def bubbleSort(numbers, drawData, timeTick):
    size = len(numbers)
    for i in range(size - 1):
        for j in range(size - i -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                drawData(numbers)
                time.sleep(timeTick)
    drawData(numbers)             