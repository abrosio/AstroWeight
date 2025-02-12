import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://solarsystem.nasa.gov/moons/saturn-moons/enceladus")

def show_info():
    # Creazione della finestra per Encelado
    enceladus_window = tk.Toplevel()
    enceladus_window.title("Encelado")
    enceladus_window.geometry("780x720")  # Aumenta la larghezza della finestra
    enceladus_window.configure(bg="#2B2B2B")
    enceladus_window.resizable(False, False)

    # Percorso per l'icona e l'immagine di Encelado
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "encelado.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        enceladus_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine di Encelado
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    enceladus_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo di Encelado
    title_label = tk.Label(enceladus_window, text="Encelado", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine di Encelado
    image_label = tk.Label(enceladus_window, image=enceladus_image, bg="#2B2B2B")
    image_label.image = enceladus_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(enceladus_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "Encelado è una luna di Saturno e si trova a una distanza media di circa 238.000 km da Saturno. "
        "Il diametro di Encelado è di circa 504 km, circa il 40% di quello della Luna. Un giorno su Encelado dura circa 1.37 giorni terrestri. "
        "Un anno su Encelado (periodo orbitale) dura circa 3.5 giorni terrestri. La gravità sulla superficie di Encelado è circa 0.1 volte quella terrestre. "
        "La temperatura su Encelado è estremamente bassa, con una media di circa -201°C. Encelado è uno dei luoghi più freddi del sistema solare. "
        "Encelado ha una sottile atmosfera composta principalmente da vapore acqueo, con tracce di anidride carbonica e azoto. "
        "Encelado è noto per i suoi spettacolari geyser che eruttano acqua e particelle di ghiaccio, creando un sottile anello attorno a Saturno. "
        "La superficie di Encelado è ricoperta da ghiaccio, con vasti crateri e fratture. L'attività geotermica suggerisce la presenza di un oceano sotto la sua crosta. "
        "Encelado è visibile solo con un telescopio, ma è stato oggetto di intense osservazioni da parte delle missioni spaziali, come Cassini."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(enceladus_window, text="Scopri di più su Encelado", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    enceladus_window.protocol("WM_DELETE_WINDOW", enceladus_window.destroy)
