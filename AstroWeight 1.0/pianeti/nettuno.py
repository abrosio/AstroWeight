import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/neptune")

def show_info():
    # Creazione della finestra per il pianeta
    planet_window = tk.Toplevel()
    planet_window.title("Nettuno")
    planet_window.geometry("780x720")  
    planet_window.configure(bg="#2B2B2B")
    planet_window.resizable(False, False)

    # Percorso per l'icona e l'immagine del pianeta
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "nettuno.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        planet_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine del pianeta
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    planet_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo del pianeta
    title_label = tk.Label(planet_window, text="Nettuno", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
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
        "Nettuno è l'ottavo pianeta più vicino al Sole e si trova a una distanza media di circa 4.498 milioni di km (30.07 UA) dal Sole. "
        "Il pianeta ha un diametro di circa 49.244 km, circa 4 volte quello della Terra. Un giorno su Nettuno dura circa 16.1 ore terrestri. "
        "Un anno su Nettuno (periodo orbitale) dura circa 165 anni terrestri. La gravità sulla superficie di Nettuno è circa 1.1 volte quella terrestre. "
        "La temperatura su Nettuno è molto bassa, con una media di circa -218°C. Nettuno ha un'atmosfera composta principalmente da idrogeno, elio e metano, "
        "che conferisce al pianeta il suo caratteristico colore blu intenso. Nettuno è noto per avere il vento più veloce del sistema solare, con raffiche che "
        "possono superare i 2.100 km/h. La superficie di Nettuno è gassosa, senza una solida definizione. "
        "Nettuno ha almeno 14 lune conosciute, tra cui Tritone, una luna ghiacciata che ha un'orbita retrograda. "
        "Nettuno è visibile solo con un telescopio, ed è l'ottavo oggetto più luminoso nel cielo, ma è difficile da osservare senza strumenti adeguati."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(planet_window, text="Scopri di più su Nettuno", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    planet_window.protocol("WM_DELETE_WINDOW", planet_window.destroy)
