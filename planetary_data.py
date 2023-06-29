import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

## planet names + moon & eros
planets_names = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "moon", "433 Eros"]

# Gravitational acceleration on different planets (in m/s^2)
planet_gravity_acc = \
    {
        "mercury": 3.7,
        "venus": 8.87,
        "earth": 9.81,
        "mars": 3.711,
        "jupiter": 24.79,
        "saturn": 10.44,
        "uranus": 8.69,
        "neptune": 11.15,
        "moon": 1.622,
        "433 Eros": 0.016
    }


def load_image_files():
    planet_image_files = []
    for planet in planets_names:
        image_path = f"images/{planet}.png"  # Replace with the path to your button images
        image = ctk.CTkImage(light_image=Image.open(image_path), size=(60, 60))
        planet_image_files.append((planet, image))
    return planet_image_files
