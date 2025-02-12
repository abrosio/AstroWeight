import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://solarsystem.nasa.gov/moons/jupiter-moons/callisto")

def show_info():
    # Creazione della finestra per Callisto
    callisto_window = tk.Toplevel()
    callisto_window.title("Callisto")
    callisto_window.geometry("780x720")  # Aumenta la larghezza della finestra
    callisto_window.configure(bg="#2B2B2B")
    callisto_window.resizable(False, False)

    # Percorso per l'icona e l'immagine di Callisto
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "callisto.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        callisto_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine di Callisto
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    callisto_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo di Callisto
    title_label = tk.Label(callisto_window, text="Callisto", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine di Callisto
    image_label = tk.Label(callisto_window, image=callisto_image, bg="#2B2B2B")
    image_label.image = callisto_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(callisto_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "Callisto è una luna di Giove e si trova a una distanza media di circa 1.882.700 km da Giove. "
        "Il diametro di Callisto è di circa 4.821 km, circa il 37% di quello della Terra. Un giorno su Callisto dura circa 16.7 giorni terrestri. "
        "Un anno su Callisto (periodo orbitale) dura circa 16.7 anni terrestri. La gravità sulla superficie di Callisto è circa 0.13 volte quella terrestre. "
        "La temperatura su Callisto è estremamente bassa, con una media di circa -139°C, rendendola una delle lune più fredde di Giove. "
        "Callisto ha una sottile atmosfera composta principalmente da anidride carbonica e ossigeno. È troppo sottile per sostenere la vita. "
        "La superficie di Callisto è molto craterizzata, con vasti bacini d'impatto e alcune regioni più giovani. Non si ritiene che ci sia attività geologica recente. "
        "Callisto è uno degli obiettivi più studiati nelle missioni spaziali, per la sua superficie unica e la possibilità di un oceano sotterraneo. "
        "Callisto è visibile con un telescopio, ma è stato osservato più dettagliatamente da missioni come Galileo e Juno, che hanno rivelato la sua storia geologica."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(callisto_window, text="Scopri di più su Callisto", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    callisto_window.protocol("WM_DELETE_WINDOW", callisto_window.destroy)
