import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/mars")

def show_info():
    # Creazione della finestra per il pianeta
    planet_window = tk.Toplevel()
    planet_window.title("Marte")
    planet_window.geometry("780x750")  # Aumenta la larghezza della finestra
    planet_window.configure(bg="#2B2B2B")
    planet_window.resizable(False, False)

    # Percorso per l'icona e l'immagine del pianeta
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "marte.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        planet_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine del pianeta
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    planet_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo del pianeta
    title_label = tk.Label(planet_window, text="Marte", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
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
        "Marte è il quarto pianeta più vicino al Sole e si trova a una distanza media di circa 227.9 milioni di km (1.52 UA) dal Sole. "
        "Il pianeta ha un diametro di circa 6.779 km, circa il 53% di quello della Terra. Un giorno su Marte dura 24.6 ore terrestri. "
        "Un anno su Marte (periodo orbitale) dura circa 687 giorni terrestri. La gravità sulla superficie di Marte è circa il 38% di quella terrestre. "
        "La temperatura su Marte è molto bassa, con una media di circa -60°C, ma può variare da -125°C nei poli a 20°C nelle zone equatoriali durante il giorno. "
        "Marte ha un'atmosfera molto sottile, composta principalmente da anidride carbonica, con tracce di azoto e argon. Questa atmosfera non è sufficiente "
        "per trattenere il calore, rendendo il pianeta freddo. La superficie di Marte è caratterizzata da grandi pianure, vulcani come il Monte Olimpo, "
        "il più grande del sistema solare, e valli profonde come il Valles Marineris. Marte ha due piccole lune, Fobos e Deimos. "
        "Marte è visibile ad occhio nudo ogni due anni, come un oggetto rosso nel cielo, ed è il quarto oggetto più luminoso nel cielo dopo il Sole, la Luna e Venere. "
        "Marte è di grande interesse per gli scienziati poiché potrebbe essere stato in passato un pianeta abitabile e viene regolarmente visitato da sonde e rover umani."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(planet_window, text="Scopri di più su Marte", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    planet_window.protocol("WM_DELETE_WINDOW", planet_window.destroy)
