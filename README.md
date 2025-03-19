# Sorting Visualizer

Sorting Visualizer is a Python-based graphical application that helps visualize various sorting algorithms in action. It provides an interactive way to understand how different sorting techniques work by animating the sorting process.

## Features
- **Multiple Sorting Algorithms**: Supports Bubble Sort, Quick Sort, Merge Sort, Insertion Sort, Selection Sort, Heap Sort, and more.
- **Custom Sorting Speed**: Allows adjusting the speed of sorting animations.
- **Random Data Generation**: Generates a new set of numbers to visualize sorting.
- **User-friendly Interface**: Built using `customtkinter` for a modern UI experience.

## Technologies Used
- **Python**
- **customtkinter** (for GUI)
- **colour** (for gradient-based coloring)
- **random** (for generating random numbers)

## Installation & Usage

### Prerequisites
Make sure you have Python (>=3.7) installed on your system.

### Step 1: Clone the Repository
```sh
git clone https://github.com/yusufbuyukbirer/sorting-visualizer.git
cd sorting-visualizer
```

### Step 2: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 3: Run the Application
```sh
python main.py
```

## How to Use
1. Select a sorting algorithm from the dropdown menu.
2. Choose the number of elements to be sorted using the slider.
3. Click the **Generate** button to create a new random dataset.
4. Adjust the sorting speed.
5. Click the **Sort** button to start the visualization.
6. Pause the sorting animation if needed.

## File Structure
```
Sorting-Visualizer/
│── functions/
│   ├── functions.py  # Sorting algorithm implementations
│── main.py           # Main application script
│── requirements.txt  # Required dependencies
│── README.md         # Project documentation
```


