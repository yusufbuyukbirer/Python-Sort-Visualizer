# importing libraries
from tkinter import *
from tkinter import ttk
from functions.insertionSort import insertionSort
from functions.heapSort import heapSort
from functions.mergeSort import mergeSort
from functions.quickSort import quickSort
from functions.selectionSort import selectionSort
from functions.bubbleSort import bubbleSort
from functions.combSort import combSort
from functions.shellSort import shellSort
from functions.countingSort import countingSort
from colour import Color
import random
import customtkinter

# creating main window
window = customtkinter.CTk()
window.geometry("1200x500")
window.resizable(False, False)
window.title("Sort Visualizer!")

#TODO: DENEME AMAÇLI yazı

# variables
window.config(bg="#071a38")
maxNumber = 101
numbers = []
# rectangle_colors = list(Color("violet").range_to(Color("red"), maxNumber))


# functions
def drawData(numbers, color):
    canvas.delete("all")

    canvas_height = 478
    canvas_width = 878
    x_width = canvas_width / (len(numbers) + 1)
    offset = 2
    spacing = 6

    normalized_data = [i / max(numbers) for i in numbers]

    for i, height in enumerate(normalized_data):
        # upper left
        x0 = (i * x_width) + offset + spacing
        y0 = canvas_height - (height * 420)

        # upper right
        x1 = ((i + 1) * x_width) + offset
        y1 = canvas_height

        # creating rectangles
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

        # writing top of the rectangles
        canvas.create_text(x0, y0, anchor="sw", text=str(numbers[i]), fill="white", font=("Comic Sans MS", 10))

    window.update_idletasks()


# showing random number values in the form of rectangle
def generate():
    global numbers
    numberLength = int(sliderNumberLength.get())

    numbers = []
    for i in range(numberLength):
        numbers.append(random.randrange(numberLength))

    drawData(numbers, ['#0CA8F6' for x in range(len(numbers))])


# adjusting the algorithm speed
def comboBox_Speed():
    if comboBoxSpeed.get() == 'Very Slow':
        return 0.5
    elif comboBoxSpeed.get() == 'Slow':
        return 0.3
    elif comboBoxSpeed.get() == 'Medium':
        return 0.1
    elif comboBoxSpeed.get() == 'Fast':
        return 0.01
    else:
        return 0.001


# choosing algorithm
def sort():
    global numbers
    timeTick = comboBox_Speed()

    if comboBoxAlgorithm.get() == 'Bubble Sort':
        bubbleSort(numbers, drawData, timeTick)
    elif comboBoxAlgorithm.get() == 'Insertion Sort':
        insertionSort(numbers, drawData, timeTick)
    elif comboBoxAlgorithm.get() == 'Selection Sort':
        selectionSort(numbers, drawData, timeTick)
    elif comboBoxAlgorithm.get() == 'Heap Sort':
        heapSort(numbers, drawData, timeTick)
    elif comboBoxAlgorithm.get() == 'Comb Sort':
        combSort(numbers, drawData, timeTick)
    elif comboBoxAlgorithm.get() == 'Counting Sort':
        countingSort(numbers, drawData, timeTick)
    elif comboBoxAlgorithm.get() == 'Shell Sort':
        shellSort(numbers, drawData, timeTick)
    elif comboBoxAlgorithm.get() == 'Quick Sort':
        quickSort(numbers, 0, len(numbers) - 1, drawData, timeTick)
    elif comboBoxAlgorithm.get() == 'Merge Sort':
        mergeSort(numbers, 0, len(numbers) - 1, drawData, timeTick)


# button, combobox
btnGenerate = customtkinter.CTkButton(window,
                                      width=120,
                                      height=32,
                                      border_width=1,
                                      corner_radius=14,
                                      text_color="white",
                                      text_font=("Comic Sans MS", 10),
                                      text="Generate",
                                      command=generate
                                      )
btnSort = customtkinter.CTkButton(window,
                                  width=120,
                                  height=32,
                                  border_width=1,
                                  corner_radius=14,
                                  text_color="white",
                                  text_font=("Comic Sans MS", 10),
                                  text="Sort",
                                  command=sort
                                  )

comboBoxAlgorithm = ttk.Combobox(window,
                                 values=["Bubble Sort", "Insertion Sort", "Quick Sort", "Selection Sort", "Heap Sort",
                                         "Merge Sort", "Comb Sort",
                                         "Counting Sort", "Shell Sort"],
                                 width=30)
comboBoxAlgorithm.current(0)

comboBoxSpeed = ttk.Combobox(window,
                             values=["Very Slow", "Slow", "Medium", "Fast", "Super Fast"],
                             width=30)
comboBoxSpeed.current(0)

comboBoxAlgorithm.place(x=55, y=140)
comboBoxSpeed.place(x=55, y=195)
btnGenerate.place(x=100, y=285)
btnSort.place(x=100, y=330)


# slider
def sliderSayi(value):
    print(value)


sliderNumberLength = customtkinter.CTkSlider(window,
                                             from_=10,
                                             to=100,
                                             height=22,
                                             button_color="#1049a3",
                                             button_hover_color="#1f63cf",
                                             number_of_steps=9,
                                             command=sliderSayi)

# placing slider
sliderNumberLength.place(x=80, y=250)

# labels
algorithmLabel = customtkinter.CTkLabel(window,
                                        width=120,
                                        height=18,
                                        text="Choose the Algorithm",
                                        text_color="white",
                                        text_font=("Comic Sans MS", 10),
                                        corner_radius=8)

comboBoxSpeedLabel = customtkinter.CTkLabel(window,
                                            width=120,
                                            height=18,
                                            text="Speed",
                                            text_color="white",
                                            text_font=("Comic Sans MS", 10),
                                            corner_radius=8)

sliderNumberLabel = customtkinter.CTkLabel(window,
                                           width=120,
                                           height=18,
                                           text="Number Length",
                                           text_color="white",
                                           text_font=("Comic Sans MS", 10),
                                           corner_radius=8)

# placing labels
algorithmLabel.place(x=95, y=115)
comboBoxSpeedLabel.place(x=100, y=170)
sliderNumberLabel.place(x=102, y=225)

# sorting screen
canvas = Canvas(window,
                width=878,
                height=478,
                bg="black")
canvas.place(x=310, y=9.8)

# this is for running the program continously
window.mainloop()
