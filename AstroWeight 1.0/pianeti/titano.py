import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://solarsystem.nasa.gov/moons/saturn-moons/titan/overview/")

def show_info():
    # Creazione della finestra per Titano
    titan_window = tk.Toplevel()
    titan_window.title("Titano")
    titan_window.geometry("780x720")  # Aumenta la larghezza della finestra
    titan_window.configure(bg="#2B2B2B")
    titan_window.resizable(False, False)

    # Percorso per l'icona e l'immagine di Titano
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "titano.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        titan_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine di Titano
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    titan_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo di Titano
    title_label = tk.Label(titan_window, text="Titano", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine di Titano
    image_label = tk.Label(titan_window, image=titan_image, bg="#2B2B2B")
    image_label.image = titan_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(titan_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "Titano è la luna più grande di Saturno e si trova a una distanza media di circa 1.222.000 km da Saturno. "
        "Il diametro di Titano è di circa 5.151 km, maggiore di quello di Mercurio. Un giorno su Titano dura circa 16 giorni terrestri. "
        "Un anno su Titano (periodo orbitale) dura circa 29.5 anni terrestri, lo stesso di Saturno. La gravità sulla superficie di Titano è circa 0.14 volte quella terrestre. "
        "La temperatura su Titano è estremamente bassa, con una media di circa -179°C, rendendolo uno dei luoghi più freddi del sistema solare. "
        "Titano ha un'atmosfera densa, composta principalmente da azoto, con tracce di metano e altri composti organici. La sua atmosfera è più densa di quella terrestre. "
        "Titano è l'unica luna del sistema solare con un'atmosfera significativa e possiede anche laghi e mari di metano liquido sulla sua superficie. "
        "Titano ha una superficie coperta da ghiaccio e rocce, e sotto di essa potrebbe esserci un oceano di acqua liquida. "
        "Titano è visibile solo con un telescopio, ma rappresenta un obiettivo di grande interesse per le missioni spaziali, come la missione Cassini-Huygens."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(titan_window, text="Scopri di più su Titano", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    titan_window.protocol("WM_DELETE_WINDOW", titan_window.destroy)
