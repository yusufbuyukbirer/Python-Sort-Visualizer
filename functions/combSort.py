import time

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
        
        for i in range (n - space):
            if numbers[i] > numbers[i + space]:
                numbers[i], numbers[i + space] = numbers[i + space], numbers[i]
                swap = True
                drawData(numbers)
                time.sleep(timeTick)

    return numbers