import os
import tkinter as tk
from PIL import Image, ImageTk

def show_formulas():
    formulas_window = tk.Toplevel()
    formulas_window.title("Formule di Calcolo")
    formulas_window.geometry("600x650")
    formulas_window.configure(bg='#2B2B2B') 
    formulas_window.resizable(False, False)
    formulas_window.attributes('-topmost', True)  

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    icona_path = os.path.join(BASE_DIR, "icon.ico")
    if os.path.exists(icona_path):
        try:
            formulas_window.iconbitmap(icona_path)
        except Exception as e:
            print(f"Errore durante l'impostazione dell'icona: {e}")
    else:
        print("Icona non trovata.")

    weight_frame = tk.Frame(formulas_window, bg="#3B3B3B")
    weight_frame.pack(pady=20, padx=20, fill="x")

    tk.Label(weight_frame, text="Calcolo del Peso", font=("Helvetica", 14, "bold"), bg="#3B3B3B", fg="#FFFFFF").pack(pady=(10, 5))
    tk.Label(weight_frame, text="Peso su Pianeta = Peso sulla Terra × Fattore Gravità", font=("Helvetica", 12), bg="#3B3B3B", fg="#FFFFFF").pack(pady=5)
    tk.Label(weight_frame, text="Questa formula utilizza il fattore di gravità del pianeta per calcolare il peso.", bg="#3B3B3B", fg="#BBBBBB", wraplength=500).pack(pady=(5, 5))

    formula1_path = os.path.join(BASE_DIR, "images", "formula1.png")
    if os.path.exists(formula1_path):
        formula1_image = Image.open(formula1_path).resize((500, 144), Image.LANCZOS)
        formula1_photo = ImageTk.PhotoImage(formula1_image)
        formula1_label = tk.Label(weight_frame, image=formula1_photo, bg="#3B3B3B")
        formula1_label.image = formula1_photo  # Mantenere riferimento
        formula1_label.pack(pady=(5, 10))
    else:
        print("Immagine della formula del peso non trovata.")

    age_frame = tk.Frame(formulas_window, bg="#3B3B3B")
    age_frame.pack(pady=20, padx=20, fill="x")

    tk.Label(age_frame, text="Calcolo dell'Età", font=("Helvetica", 14, "bold"), bg="#3B3B3B", fg="#FFFFFF").pack(pady=(10, 5))
    tk.Label(age_frame, text="Età su Pianeta = Età sulla Terra ÷ Periodo Orbitale del Pianeta", font=("Helvetica", 12), bg="#3B3B3B", fg="#FFFFFF").pack(pady=5)
    tk.Label(age_frame, text="Questa formula divide l'età sulla Terra per il periodo orbitale del pianeta.", bg="#3B3B3B", fg="#BBBBBB", wraplength=500).pack(pady=(5, 5))

    formula2_path = os.path.join(BASE_DIR, "images", "formula2.png")
    if os.path.exists(formula2_path):
        formula2_image = Image.open(formula2_path).resize((500, 148), Image.LANCZOS)
        formula2_photo = ImageTk.PhotoImage(formula2_image)
        formula2_label = tk.Label(age_frame, image=formula2_photo, bg="#3B3B3B")
        formula2_label.image = formula2_photo  # Mantenere riferimento
        formula2_label.pack(pady=(5, 10))
    else:
        print("Immagine della formula dell'età non trovata.")
