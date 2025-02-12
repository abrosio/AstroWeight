import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/saturn")

def show_info():
    # Creazione della finestra per il pianeta
    planet_window = tk.Toplevel()
    planet_window.title("Saturno")
    planet_window.geometry("780x720")  # Aumenta la larghezza della finestra
    planet_window.configure(bg="#2B2B2B")
    planet_window.resizable(False, False)

    # Percorso per l'icona e l'immagine del pianeta
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "saturno.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        planet_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine del pianeta
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    planet_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo del pianeta
    title_label = tk.Label(planet_window, text="Saturno", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
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
        "Saturno è il sesto pianeta più vicino al Sole e si trova a una distanza media di circa 1.429 miliardi di km (9.5 UA) dal Sole. "
        "Il pianeta ha un diametro di circa 116.460 km, circa 9,5 volte quello della Terra. Un giorno su Saturno dura circa 10.7 ore terrestri. "
        "Un anno su Saturno (periodo orbitale) dura circa 29 anni terrestri. La gravità sulla superficie di Saturno è circa 1.07 volte quella terrestre. "
        "La temperatura su Saturno varia tra -140°C e -180°C, con una temperatura media di circa -178°C. Saturno ha un'atmosfera composta principalmente "
        "da idrogeno ed elio, con tracce di metano, ammoniaca e vapore acqueo. La sua atmosfera è famosa per i suoi spettacolari anelli, "
        "composti principalmente da particelle di ghiaccio e roccia. La superficie di Saturno è anch'essa gassosa, senza una vera superficie solida. "
        "Saturno ha almeno 82 lune conosciute, tra cui la luna Titano, la seconda luna più grande del sistema solare. "
        "Saturno è visibile ad occhio nudo come un oggetto luminoso nel cielo, ed è il sesto oggetto più luminoso nel cielo dopo il Sole, la Luna, "
        "Venere, Giove e Marte."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(planet_window, text="Scopri di più su Saturno", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    planet_window.protocol("WM_DELETE_WINDOW", planet_window.destroy)
