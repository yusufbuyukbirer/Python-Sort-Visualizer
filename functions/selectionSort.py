import time

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