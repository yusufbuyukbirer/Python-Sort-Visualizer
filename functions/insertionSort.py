import time

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