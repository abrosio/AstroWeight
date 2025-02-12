import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
from informazioni import show_information
from formule import show_formulas
import importlib  

celestial_bodies = {
    "Mercurio": {"gravity": 0.38, "orbital_period": 0.24},
    "Venere": {"gravity": 0.91, "orbital_period": 0.62},
    "Marte": {"gravity": 0.38, "orbital_period": 1.88},
    "Giove": {"gravity": 2.34, "orbital_period": 11.86},
    "Saturno": {"gravity": 1.06, "orbital_period": 29.46},
    "Urano": {"gravity": 0.92, "orbital_period": 84.01},
    "Nettuno": {"gravity": 1.19, "orbital_period": 164.79},
    "Luna": {"gravity": 0.165, "orbital_period": 0.0748},
    "Titano": {"gravity": 0.138, "orbital_period": 0.044},
    "Encelado": {"gravity": 0.011, "orbital_period": 0.0014},
    "Io": {"gravity": 0.183, "orbital_period": 0.0041},
    "Europa": {"gravity": 0.134, "orbital_period": 0.0049},
    "Ganimede": {"gravity": 0.146, "orbital_period": 0.0072},
    "Callisto": {"gravity": 0.126, "orbital_period": 0.0167},
    "Sole": {"gravity": 27.01, "orbital_period": float("inf")},
    "Plutone": {"gravity": 0.620, "orbital_period": 248},
    "Eris": {"gravity": 0.825, "orbital_period": 557},
    "Cerere": {"gravity": 0.274, "orbital_period": 4.60}
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(BASE_DIR, "images")
planets_dir = os.path.join(BASE_DIR, "pianeti")

loaded_images = {}

def load_image(name):
    try:
        image_path = os.path.join(images_dir, f"{name.lower()}.png")
        img = Image.open(image_path).resize((80, 80), Image.LANCZOS)
        loaded_images[name] = ImageTk.PhotoImage(img)
        return loaded_images[name]
    except FileNotFoundError:
        messagebox.showerror("Errore", f"Immagine per {name} non trovata.")
        return None

def open_planet_info(planet_name):
    try:
        module_name = f"pianeti.{planet_name.lower()}"
        planet_module = importlib.import_module(module_name)
        if hasattr(planet_module, "show_info"):
            planet_module.show_info()
        else:
            messagebox.showerror("Errore", f"Il modulo '{module_name}' non contiene una funzione 'show_info'.")
    except ModuleNotFoundError:
        messagebox.showerror("Errore", f"Modulo non trovato per {planet_name}. Assicurati che '{planet_name.lower()}.py' esista nella cartella 'pianeti'.")
    except Exception as e:
        messagebox.showerror("Errore", f"Errore nell'aprire il file per {planet_name}: {e}")

def calculate_weight_on_body(earth_weight, body):
    gravity_factor = celestial_bodies.get(body, {}).get("gravity", 1.0)
    return round(earth_weight * gravity_factor, precision)

def calculate_age_on_body(earth_age, body):
    orbital_period = celestial_bodies.get(body, {}).get("orbital_period", 1.0)
    if orbital_period == float("inf"):
        return "Non Calcolabile"
    return round(earth_age / orbital_period, 2)

def convert_weight_to_kg(weight, unit):
    return weight * 0.453592 if unit == "lb" else weight

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("AstroWeight")
root.geometry("1000x940")
root.configure(bg='#2B2B2B')
root.resizable(False, False)

icona_path = os.path.join(BASE_DIR, "icon.ico")
root.iconbitmap(icona_path)

precision = 2

button_frame = ctk.CTkFrame(root, fg_color=root.cget('bg'))
button_frame.place(relx=1.0, rely=0.99, anchor="se")

formulas_button = ctk.CTkButton(button_frame, text="Formule", command=show_formulas, width=80, height=30, corner_radius=0)
formulas_button.grid(row=0, column=0, padx=5, pady=5)

information_button = ctk.CTkButton(button_frame, text="Informazioni", command=lambda: show_information(root), width=100, height=30, corner_radius=0)
information_button.grid(row=0, column=1, padx=5, pady=5)

main_frame = ctk.CTkFrame(root, fg_color="#3B3B3B", width=750, height=600)
main_frame.place(relx=0.5, rely=0.45, anchor="center")

layout = [
    ["Mercurio", "Venere", "Marte", "Giove", "Saturno", "Urano"],
    ["Nettuno", "Luna", "Io", "Europa", "Ganimede", "Callisto"],
    ["Titano", "Encelado", "Plutone", "Eris", "Cerere", "Sole"]
]

for row_index, row in enumerate(layout):
    for col_index, body in enumerate(row):
        img = load_image(body)
        if img:
            img_label = tk.Label(main_frame, image=img, bg="#3B3B3B", cursor="hand2")
            img_label.grid(row=row_index * 5, column=col_index, padx=10, pady=(10, 0), sticky="n")
            img_label.bind("<Button-1>", lambda event, name=body: open_planet_info(name))
            name_label = ctk.CTkLabel(main_frame, text=body, text_color="#FFFFFF", font=("Helvetica", 10, "bold"))
            name_label.grid(row=row_index * 5 + 1, column=col_index, padx=10, pady=(0, 5), sticky="n")

root.mainloop()
