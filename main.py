from functions.functions import *
from colour import Color
import random
import customtkinter


class SortingVisualizer:
    def __init__(self):
        self.window = customtkinter.CTk()
        self.window.geometry("1200x600")
        self.window.resizable(False, False)
        self.window.title("Sorting Visualizer")
        self.window.configure(fg_color="#071a38")

        self.max_number = 101
        self.numbers = []
        self.rectangle_colors = list(Color("violet").range_to(Color("red"), self.max_number))

        self.create_widgets()

    def draw_data(self, numbers=None):
        self.canvas.delete("all")
        if numbers is not None:
            self.numbers = numbers
        if not self.numbers:
            return

        canvas_height, canvas_width = 580, 878
        x_width = canvas_width / (len(self.numbers) + 1)
        offset, spacing = 6, 2

        normalized_data = [i / max(self.numbers) for i in self.numbers]

        for i, height in enumerate(normalized_data):
            x0 = (i * x_width) + offset + spacing
            y0 = canvas_height - (height * 420)

            x1 = ((i + 1) * x_width) + offset
            y1 = canvas_height

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.rectangle_colors[i])
            self.canvas.create_text(x0, y0, anchor="sw", text=str(self.numbers[i]), fill="white", font=("LDF Comic Sans", 10))

        self.window.update_idletasks()

    def generate(self):
        number_length = int(self.slider_number_length.get())
        self.numbers = random.sample(range(1, number_length + 1), number_length)
        self.draw_data()

    def get_speed(self):
        speeds = {
            "Very Slow": 0.5,
            "Slow": 0.3,
            "Medium": 0.1,
            "Fast": 0.01,
            "Super Fast": 0.001
        }
        return speeds.get(self.combobox_speed.get(), 0.1)

    def sort(self):
        time_tick = self.get_speed()
        selected_algorithm = self.combobox_sort.get()

        sorting_algorithms = {
            "Bubble Sort": bubble_sort,
            "Insertion Sort": insertion_sort,
            "Selection Sort": selection_sort,
            "Heap Sort": heap_sort,
            "Comb Sort": comb_sort,
            "Counting Sort": counting_sort,
            "Shell Sort": shell_sort,
            "Quick Sort": lambda numbers, draw_data, time_tick: quick_sort(numbers, 0, len(numbers) - 1, draw_data, time_tick),
            "Merge Sort": lambda numbers, draw_data, time_tick: merge_sort(numbers, 0, len(numbers) - 1, draw_data, time_tick)
        }

        if selected_algorithm in sorting_algorithms:
            sorting_algorithms[selected_algorithm](self.numbers, self.draw_data, time_tick)

    def create_widgets(self):
        self.btn_generate = customtkinter.CTkButton(self.window, text="Generate", font=("LDF Comic Sans", 15),
                                                    width=200, corner_radius=10, command=self.generate)
        self.btn_sort = customtkinter.CTkButton(self.window, text="Sort", font=("LDF Comic Sans", 15),
                                                width=200, corner_radius=10, command=self.sort)
        self.btn_pause = customtkinter.CTkButton(self.window, text="Pause", font=("LDF Comic Sans", 15),
                                                 width=200, corner_radius=10)

        self.combobox_sort = customtkinter.CTkComboBox(self.window,
                                                       values=["Bubble Sort", "Comb Sort", "Counting Sort", "Heap Sort",
                                                               "Insertion Sort", "Merge Sort", "Selection Sort",
                                                               "Shell Sort", "Quick Sort"],
                                                       font=("LDF Comic Sans", 15),
                                                       dropdown_font=("LDF Comic Sans", 15),
                                                       width=200, justify="center")

        self.combobox_speed = customtkinter.CTkComboBox(self.window,
                                                        values=["Very Slow", "Slow", "Medium", "Fast", "Super Fast"],
                                                        font=("LDF Comic Sans", 15),
                                                        dropdown_font=("LDF Comic Sans", 15),
                                                        width=200, justify="center")

        self.slider_number_length = customtkinter.CTkSlider(self.window, from_=10, to=100, height=22, width=220,
                                                            button_color="#1049a3", button_hover_color="#1f63cf",
                                                            number_of_steps=9)

        self.canvas = customtkinter.CTkCanvas(self.window, width=878, height=580, bg="black")
        self.canvas.place(x=310, y=9.8)

        self.btn_sort_label = customtkinter.CTkLabel(self.window, text="Choose an Algorithm", font=("LDF Comic Sans", 15))
        self.btn_speed_label = customtkinter.CTkLabel(self.window, text="Speed", font=("LDF Comic Sans", 15))
        self.btn_slider_label = customtkinter.CTkLabel(self.window, text="Number Length", font=("LDF Comic Sans", 15))

        self.combobox_sort.place(x=60, y=140)
        self.combobox_speed.place(x=60, y=215)
        self.btn_generate.place(x=60, y=325)
        self.btn_sort.place(x=60, y=370)
        self.btn_pause.place(x=60, y=415)
        self.slider_number_length.place(x=50, y=290)
        self.btn_sort_label.place(x=90, y=105)
        self.btn_speed_label.place(x=130, y=180)
        self.btn_slider_label.place(x=102, y=260)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = SortingVisualizer()
    app.run()