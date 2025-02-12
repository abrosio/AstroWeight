import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://science.nasa.gov/uranus")

def show_info():
    # Creazione della finestra per il pianeta
    planet_window = tk.Toplevel()
    planet_window.title("Urano")
    planet_window.geometry("780x720")  # Aumenta la larghezza della finestra
    planet_window.configure(bg="#2B2B2B")
    planet_window.resizable(False, False)

    # Percorso per l'icona e l'immagine del pianeta
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "urano.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        planet_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine del pianeta
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    planet_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo del pianeta
    title_label = tk.Label(planet_window, text="Urano", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine del pianeta
    image_label = tk.Label(planet_window, image=planet_image, bg="#2B2B2B")
    image_label.image = planet_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(planet_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "Urano è il settimo pianeta più vicino al Sole e si trova a una distanza media di circa 2.871 milioni di km (19.2 UA) dal Sole. "
        "Il pianeta ha un diametro di circa 50.724 km, circa 4 volte quello della Terra. Un giorno su Urano dura circa 17.2 ore terrestri. "
        "Un anno su Urano (periodo orbitale) dura circa 84 anni terrestri. La gravità sulla superficie di Urano è circa 0.9 volte quella terrestre. "
        "La temperatura su Urano è estremamente bassa, con una media di circa -224°C, il che lo rende uno dei pianeti più freddi del sistema solare. "
        "Urano ha un'atmosfera composta principalmente da idrogeno, elio e metano, che conferisce al pianeta il suo caratteristico colore azzurro-verde. "
        "Urano è l'unico pianeta che ruota sul suo lato, con un'inclinazione assiale di circa 98°. La superficie di Urano è gassosa, senza una solida definizione. "
        "Urano ha almeno 27 lune conosciute, tra cui Miranda, Ariel, Umbriel, Titania e Oberon. "
        "Urano è visibile solo con un telescopio, ed è il settimo oggetto più luminoso nel cielo, ma è difficile da osservare senza strumenti adeguati."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(planet_window, text="Scopri di più su Urano", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    planet_window.protocol("WM_DELETE_WINDOW", planet_window.destroy)
