import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://solarsystem.nasa.gov/moons/jupiter-moons/europa")

def show_info():
    # Creazione della finestra per Europa
    europa_window = tk.Toplevel()
    europa_window.title("Europa")
    europa_window.geometry("780x720")  # Aumenta la larghezza della finestra
    europa_window.configure(bg="#2B2B2B")
    europa_window.resizable(False, False)

    # Percorso per l'icona e l'immagine di Europa
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "europa.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        europa_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine di Europa
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    europa_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo di Europa
    title_label = tk.Label(europa_window, text="Europa", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine di Europa
    image_label = tk.Label(europa_window, image=europa_image, bg="#2B2B2B")
    image_label.image = europa_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(europa_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "Europa è una luna di Giove e si trova a una distanza media di circa 670.900 km da Giove. "
        "Il diametro di Europa è di circa 3.121 km, circa il 24% di quello della Terra. Un giorno su Europa dura circa 3.5 giorni terrestri. "
        "Un anno su Europa (periodo orbitale) dura circa 3.5 anni terrestri. La gravità sulla superficie di Europa è circa 0.13 volte quella terrestre. "
        "La temperatura su Europa è estremamente bassa, con una media di circa -160°C, ma sotto la sua superficie potrebbe esserci un oceano liquido. "
        "Europa ha una sottile atmosfera composta principalmente da ossigeno, ma troppo sottile per supportare la vita come la conosciamo. "
        "La superficie di Europa è coperta da un ghiaccio che si crede nasconda un oceano liquido sotto di esso, che potrebbe ospitare forme di vita. "
        "Europa è un obiettivo di grande interesse per la ricerca spaziale, specialmente per la sua potenziale abitabilità e le sue caratteristiche geologiche. "
        "Europa è visibile solo con un telescopio, ma è stata studiata in dettaglio dalle missioni spaziali come la sonda Galileo e la missione Juno."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(europa_window, text="Scopri di più su Europa", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    europa_window.protocol("WM_DELETE_WINDOW", europa_window.destroy)
