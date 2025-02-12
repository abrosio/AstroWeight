import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://solarsystem.nasa.gov/moons/jupiter-moons/io")

def show_info():
    # Creazione della finestra per Io
    io_window = tk.Toplevel()
    io_window.title("IO")
    io_window.geometry("780x720")  # Aumenta la larghezza della finestra
    io_window.configure(bg="#2B2B2B")
    io_window.resizable(False, False)

    # Percorso per l'icona e l'immagine di Io
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "io.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        io_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine di Io
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    io_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo di Io
    title_label = tk.Label(io_window, text="Io", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine di Io
    image_label = tk.Label(io_window, image=io_image, bg="#2B2B2B")
    image_label.image = io_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(io_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "Io è una luna di Giove e si trova a una distanza media di circa 421.700 km da Giove. "
        "Il diametro di Io è di circa 3.643 km, circa il 28% di quello della Terra. Un giorno su Io dura circa 1.8 giorni terrestri. "
        "Un anno su Io (periodo orbitale) dura circa 1.8 anni terrestri, ed è molto più breve del suo giorno. La gravità sulla superficie di Io è circa 0.18 volte quella terrestre. "
        "La temperatura su Io è estremamente variabile, con una media di circa -143°C, ma può raggiungere anche i 1.300°C in prossimità dei vulcani attivi. "
        "Io è il corpo più geologicamente attivo del sistema solare, con centinaia di vulcani attivi che eruttano zolfo e lava, creando una superficie in continua trasformazione. "
        "Io ha un'atmosfera molto sottile, composta principalmente da anidride solforosa, ma è troppo sottile per supportare la vita. "
        "La superficie di Io è coperta da vulcani, montagne e vaste pianure di zolfo, risultando molto diversa da quella di qualsiasi altro corpo del sistema solare. "
        "Io è visibile con un telescopio e ha suscitato grande interesse per le sue caratteristiche geologiche uniche, studiate soprattutto dalla sonda Galileo."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(io_window, text="Scopri di più su Io", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    io_window.protocol("WM_DELETE_WINDOW", io_window.destroy)
