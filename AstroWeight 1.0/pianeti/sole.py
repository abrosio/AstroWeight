import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/sun/")

def show_info():
    # Creazione della finestra per il Sole
    sun_window = tk.Toplevel()
    sun_window.title("Il Sole")
    sun_window.geometry("780x720")  # Aumenta la larghezza della finestra
    sun_window.configure(bg="#2B2B2B")
    sun_window.resizable(False, False)

    # Percorso per l'icona e l'immagine del Sole
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "sole.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        sun_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine del Sole
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    sun_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo del Sole
    title_label = tk.Label(sun_window, text="Il Sole", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine del Sole
    image_label = tk.Label(sun_window, image=sun_image, bg="#2B2B2B")
    image_label.image = sun_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(sun_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "Il Sole è la stella centrale del nostro sistema solare e si trova a una distanza media di circa 149.6 milioni di km dalla Terra (1 UA). "
        "Il diametro del Sole è di circa 1.391.000 km, circa 109 volte quello della Terra. Un giorno sul Sole dura circa 25 giorni terrestri all'equatore. "
        "Un anno sul Sole non ha significato, poiché è la stella attorno alla quale ruotano tutti gli altri corpi celesti. La gravità sulla superficie del Sole è circa 28 volte quella terrestre. "
        "La temperatura sulla superficie del Sole è di circa 5.500°C, ma al suo centro può arrivare a circa 15 milioni di gradi Celsius. "
        "Il Sole è composto principalmente da idrogeno e elio, con tracce di altri elementi come carbonio, ossigeno e azoto. "
        "Il Sole produce energia attraverso la fusione nucleare nel suo nucleo, generando luce e calore che raggiungono la Terra. "
        "La sua energia è fondamentale per la vita sulla Terra, influenzando il clima e l'ambiente del nostro pianeta. "
        "Il Sole è visibile ad occhio nudo dalla Terra e domina il nostro cielo durante il giorno, fornendo luce e calore."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(sun_window, text="Scopri di più sul Sole", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    sun_window.protocol("WM_DELETE_WINDOW", sun_window.destroy)
