import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/moon")

def show_info():
    # Creazione della finestra per la Luna
    moon_window = tk.Toplevel()
    moon_window.title("Luna")
    moon_window.geometry("780x720")  # Aumenta la larghezza della finestra
    moon_window.configure(bg="#2B2B2B")
    moon_window.resizable(False, False)

    # Percorso per l'icona e l'immagine della Luna
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "luna.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        moon_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine della Luna
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    moon_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo della Luna
    title_label = tk.Label(moon_window, text="Luna", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine della Luna
    image_label = tk.Label(moon_window, image=moon_image, bg="#2B2B2B")
    image_label.image = moon_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(moon_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "La Luna è il satellite naturale della Terra e si trova a una distanza media di circa 384.400 km dalla Terra. "
        "Il diametro della Luna è di circa 3.474 km, circa un quarto di quello della Terra. Un giorno sulla Luna dura circa 29.5 giorni terrestri. "
        "Un anno sulla Luna (periodo orbitale) dura lo stesso tempo di un giorno lunare, ovvero 29.5 giorni terrestri. La gravità sulla superficie della Luna è circa "
        "un sesto di quella terrestre. La temperatura sulla Luna varia enormemente tra il giorno e la notte. Durante il giorno, può arrivare fino a 127°C, "
        "mentre di notte scende fino a -173°C. La Luna ha un'atmosfera estremamente sottile, quasi assente, composta principalmente da elio, neon e idrogeno. "
        "La superficie della Luna è ricoperta da crateri, mari lunari (grandi pianure basaltiche), e montagne. Questi crateri si sono formati a causa degli impatti "
        "di meteoriti nel corso della sua lunga storia. La Luna ha una faccia visibile dalla Terra, poiché è in rotazione sincrona con la Terra. "
        "La Luna è visibile ad occhio nudo come un oggetto luminoso nel cielo, e riveste un'importanza culturale, scientifica e storica per l'umanità."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(moon_window, text="Scopri di più sulla Luna", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    moon_window.protocol("WM_DELETE_WINDOW", moon_window.destroy)
