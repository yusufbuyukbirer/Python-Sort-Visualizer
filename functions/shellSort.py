import time

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