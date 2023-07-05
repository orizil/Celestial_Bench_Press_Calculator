import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from planetary_data import *


class CelestialBenchPressCalculator:
    def __init__(self, root):
        self.root = root
        self.selected_planet = tk.StringVar()
        self.selected_planet.set("earth")

        self.left_panel = ctk.CTkFrame(self.root)
        self.left_panel.grid(row=0, column=0, padx=5, pady=5)

        self.right_panel = ctk.CTkFrame(self.root)
        self.right_panel.grid(row=0, column=1, padx=5, pady=5)

        self.weight = tk.StringVar()
        self.weight.set('50')

        self.create_planet_buttons()
        self.create_input_label()
        self.create_result_label()
        self.create_info_label()
        self.create_slider_and_entry()
        self.weight.trace_add("write", self.update_slider_from_entry)

    def create_planet_buttons(self):
        button_images = load_image_files()
        button_index = 0

        for name, image in button_images:
            button_row = button_index // 2
            button_column = button_index % 2

            planet_button = ctk.CTkButton(self.left_panel, image=image, text=name.capitalize(),
                                          fg_color="transparent", command=lambda planet=name: self.button_click(planet))
            planet_button.grid(row=button_row, column=button_column, pady=5)

            button_index += 1

    def create_input_label(self):
        label_text = "Current max bench press (kg):"
        label = ctk.CTkLabel(self.right_panel, text=label_text, font=("Josefin", 18))
        label.grid(row=1, column=0, columnspan=2, padx=15, pady=(15, 5))

    def create_info_label(self):
        label_text = "Welcome to the Celestial Bench Press Calculator!\n\n  Choose a planet from the solar system,\n" \
                     "the moon, or 433-Eros - the first soft-landed asteroid!"
        label = ctk.CTkLabel(self.right_panel, text_color="gray", text=label_text, font=("Josefin", 12))
        label.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

    def create_slider_and_entry(self):
        self.bench_press_entry = ctk.CTkEntry(self.right_panel, textvariable=self.weight, width=40)
        validate_cmd = self.right_panel.register(self.validate_input)
        self.bench_press_entry.configure(validate="key", validatecommand=(validate_cmd, '%P'))
        self.bench_press_entry.grid(row=2, column=0, padx=15)

        self.bench_press_slider = ctk.CTkSlider(self.right_panel, from_=0, to=300)
        self.bench_press_slider.set(50)
        self.bench_press_slider.grid(row=2, column=1, padx=15, pady=(5, 15))
        self.bench_press_slider.bind("<B1-Motion>", self.update_entry_from_slider)
        self.bench_press_slider.bind("<ButtonRelease-1>", self.update_entry_from_slider)

    def create_result_label(self):
        self.result_label = ctk.CTkLabel(self.right_panel, text="Select a celestial object", font=("Josefin", 14))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=15, pady=(5, 15))

    def button_click(self, planet):
        self.selected_planet.set(planet)
        self.calc_result()

    def update_entry_from_slider(self, event):
        slider_bench_press = int(round(self.bench_press_slider.get()))
        self.weight.set(str(slider_bench_press))
        self.calc_result()

    def update_slider_from_entry(self, *args):
        try:
            slider_bench_press = int(self.weight.get())
            self.bench_press_slider.set(slider_bench_press)
            self.calc_result()
        except ValueError:
            self.result_label.configure(text="Invalid input")

    def validate_input(self, val):
        if val.isdigit():
            if int(val) <= 300:
                return True
        return False

    def calc_result(self):
        a_ratio = planet_gravity_acc['earth'] / planet_gravity_acc[self.selected_planet.get()]
        result = round(int(self.weight.get()) * a_ratio, 2)
        self.result_label.configure(text=f"Your bench press on {self.selected_planet.get().capitalize()}: {result} kg")


if __name__ == '__main__':
    ctk.set_appearance_mode('dark')
    root = ctk.CTk()
    root.title("Celestial Bench Press Calculator")
    root.geometry('600x400')

    calculator = CelestialBenchPressCalculator(root)

    root.mainloop()
