import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/venus")

def show_info():
    # Creazione della finestra per il pianeta
    planet_window = tk.Toplevel()
    planet_window.title("Venere")
    planet_window.geometry("780x750")  # Aumenta la larghezza della finestra
    planet_window.configure(bg="#2B2B2B")
    planet_window.resizable(False, False)

    # Percorso per l'icona e l'immagine del pianeta
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "venere.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        planet_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine del pianeta
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    planet_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo del pianeta
    title_label = tk.Label(planet_window, text="Venere", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine del pianeta
    image_label = tk.Label(planet_window, image=planet_image, bg="#2B2B2B")
    image_label.image = planet_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(planet_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo aggiornato per Venere
    description_text = (
        "Venere è il secondo pianeta più vicino al Sole e si trova a una distanza media di circa 108.2 milioni di km (0.72 UA) dal Sole. "
        "Il pianeta ha un diametro di circa 12.104 km, circa il 95% di quello della Terra. Un giorno su Venere dura 243 giorni terrestri. "
        "Un anno su Venere (periodo orbitale) dura circa 225 giorni terrestri. La gravità sulla superficie di Venere è circa l'88% di quella terrestre. "
        "La temperatura su Venere è estremamente alta, con una media di circa 465°C, rendendolo il pianeta più caldo del sistema solare, "
        "anche più caldo di Mercurio, nonostante Mercurio sia più vicino al Sole. Venere ha un'atmosfera densa, composta principalmente da anidride carbonica "
        "e nuvole di acido solforico. L'atmosfera di Venere è circa 90 volte più spessa di quella terrestre e crea un effetto serra estremo che intrappola il calore. "
        "La superficie di Venere è composta da pianure vulcaniche e montagne, con grandi vulcani come Maat Mons. Venere non ha satelliti naturali. "
        "Venere è visibile ad occhio nudo come un oggetto luminoso nel cielo, spesso chiamato 'Stella del mattino' o 'Stella della sera', "
        "a seconda di quando appare all'orizzonte, ed è il quarto oggetto più luminoso nel cielo dopo il Sole, la Luna e Giove."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(planet_window, text="Scopri di più su Venere", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    planet_window.protocol("WM_DELETE_WINDOW", planet_window.destroy)
