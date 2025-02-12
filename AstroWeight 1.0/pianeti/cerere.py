import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/dwarf-planets/ceres/")

def show_info():
    # Creazione della finestra per Ceres
    planet_window = tk.Toplevel()
    planet_window.title("Ceres")
    planet_window.geometry("780x700")  # Aumenta la larghezza della finestra
    planet_window.configure(bg="#2B2B2B")
    planet_window.resizable(False, False)

    # Percorso per l'icona e l'immagine di Ceres
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "cerere.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        planet_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine di Ceres
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    planet_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo del pianeta
    title_label = tk.Label(planet_window, text="Ceres", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine del pianeta
    image_label = tk.Label(planet_window, image=planet_image, bg="#2B2B2B")
    image_label.image = planet_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(planet_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "Ceres è un pianeta nano situato nella fascia principale di asteroidi tra Marte e Giove, a una distanza media di circa 413.000.000 km dal Sole. "
        "Il diametro di Ceres è di circa 940 km, circa un quarto di quello della Luna. Un giorno su Ceres dura circa 9.1 ore terrestri. "
        "Un anno su Ceres (periodo orbitale) dura circa 4.6 anni terrestri. "
        "La gravità sulla superficie di Ceres è circa 0.03 volte quella terrestre. "
        "La temperatura su Ceres è estremamente bassa, con una media di circa -105°C, rendendola un corpo ghiacciato nel sistema solare. "
        "Ceres ha una sottile atmosfera composta principalmente da vapore d'acqua, che può evaporare durante i periodi più caldi del suo anno. "
        "La superficie di Ceres è caratterizzata da un paesaggio variegato con grandi crateri, montagne e segni di attività geologica passata, inclusi possibili ghiacciai sotterranei. "
        "Ceres è stato studiato da vicino dalla sonda Dawn della NASA, che ha rivelato molti dettagli sulle sue caratteristiche geologiche e la sua evoluzione."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(planet_window, text="Scopri di più su Ceres", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    planet_window.protocol("WM_DELETE_WINDOW", planet_window.destroy)
