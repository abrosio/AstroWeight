import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/mercury")

def show_info():
    # Creazione della finestra per il pianeta
    planet_window = tk.Toplevel()
    planet_window.title("Mercurio")
    planet_window.geometry("780x740")  # Aumenta la larghezza della finestra
    planet_window.configure(bg="#2B2B2B")
    planet_window.resizable(False, False)

    # Percorso per l'icona e l'immagine del pianeta
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "mercurio.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        planet_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine del pianeta
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    planet_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo del pianeta
    title_label = tk.Label(planet_window, text="Mercurio", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine del pianeta
    image_label = tk.Label(planet_window, image=planet_image, bg="#2B2B2B")
    image_label.image = planet_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(planet_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo aggiornato
    description_text = (
        "Mercurio è il pianeta più vicino al Sole e si trova a una distanza media di circa 57.9 milioni di km (0.39 UA) dal Sole. "
        "Il pianeta ha un diametro di circa 4.880 km, circa il 38% di quello della Terra. Un giorno su Mercurio dura 58.6 giorni terrestri. "
        "Un anno su Mercurio (periodo orbitale) dura solo 88 giorni terrestri. La gravità sulla superficie di Mercurio è circa il 38% di quella terrestre. "
        "La temperatura su Mercurio varia enormemente tra il giorno e la notte. Durante il giorno, può arrivare fino a 430°C, mentre di notte scende fino a -180°C. "
        "Mercurio ha un'atmosfera molto sottile, chiamata esosfera, composta principalmente da ossigeno, sodio, idrogeno, elio e potassio. Tuttavia, è così sottile che non può trattenere il calore. "
        "La superficie di Mercurio è ricoperta da crateri, simili a quelli della Luna. Questo indica che il pianeta non ha un'atmosfera che possa proteggere la sua superficie dall'impatto di meteoriti. "
        "Mercurio non ha satelliti naturali. Mercurio è visibile ad occhio nudo solo durante il crepuscolo, poco prima dell'alba o subito dopo il tramonto, in quanto si trova sempre vicino al Sole"
        "e può essere visto come un piccolo punto luminoso nel cielo."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(planet_window, text="Scopri di più su Mercurio", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    planet_window.protocol("WM_DELETE_WINDOW", planet_window.destroy)
