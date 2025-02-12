import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/dwarf-planets/pluto/")

def show_info():
    # Creazione della finestra per Plutone
    planet_window = tk.Toplevel()
    planet_window.title("Plutone")
    planet_window.geometry("780x710")  # Aumenta la larghezza della finestra
    planet_window.configure(bg="#2B2B2B")
    planet_window.resizable(False, False)

    # Percorso per l'icona e l'immagine di Plutone
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "plutone.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        planet_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine di Plutone
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    planet_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo del pianeta
    title_label = tk.Label(planet_window, text="Plutone", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
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
        "Plutone è un pianeta nano situato nella fascia di Kuiper, a una distanza media di circa 5.9 miliardi di km dal Sole. "
        "Il diametro di Plutone è di circa 2.377 km, circa il 18% di quello della Terra. Un giorno su Plutone dura circa 6.4 giorni terrestri. "
        "Un anno su Plutone (periodo orbitale) dura circa 248 anni terrestri, rendendolo uno degli oggetti più distanti e lenti del sistema solare. "
        "La gravità sulla superficie di Plutone è circa 0.06 volte quella terrestre. "
        "La temperatura su Plutone è estremamente bassa, con una media di circa -229°C, rendendolo uno dei luoghi più freddi del sistema solare. "
        "Plutone ha un'atmosfera molto sottile, composta principalmente da azoto, metano e monossido di carbonio, che si condensa e sublima a seconda della sua posizione orbitale. "
        "La superficie di Plutone è variegata, con montagne di ghiaccio, vaste pianure e regioni scure di terreno ricco di metano. "
        "Plutone è visibile solo con un telescopio, ed è stato studiato da vicino dalla sonda New Horizons nel 2015."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(planet_window, text="Scopri di più su Plutone", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    planet_window.protocol("WM_DELETE_WINDOW", planet_window.destroy)
