import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

def open_browser_link():
    webbrowser.open("https://solarsystem.nasa.gov/moons/jupiter-moons/ganymede/")

def show_info():
    # Creazione della finestra per Ganimede
    ganimede_window = tk.Toplevel()
    ganimede_window.title("Ganimede")
    ganimede_window.geometry("780x720")  # Aumenta la larghezza della finestra
    ganimede_window.configure(bg="#2B2B2B")
    ganimede_window.resizable(False, False)

    # Percorso per l'icona e l'immagine di Ganimede
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "img", "ganimede.png")
    
    # Carica l'icona se disponibile
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        ganimede_window.iconbitmap(icon_path)

    # Carica e ridimensiona l'immagine di Ganimede
    img = Image.open(img_path)
    img_resized = img.resize((300, 300), Image.LANCZOS)
    ganimede_image = ImageTk.PhotoImage(img_resized)
    
    # Etichetta per il titolo di Ganimede
    title_label = tk.Label(ganimede_window, text="Ganimede", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Visualizza l'immagine di Ganimede
    image_label = tk.Label(ganimede_window, image=ganimede_image, bg="#2B2B2B")
    image_label.image = ganimede_image  # Mantiene il riferimento
    image_label.pack(pady=10)

    # Frame per il testo descrittivo con bordo rilievo ombreggiato
    text_frame = tk.Frame(ganimede_window, bg="#2B2B2B", bd=2, relief="sunken")  # Aggiungi il bordo con rilievo ombreggiato
    text_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Aumenta la larghezza e altezza del frame

    # Testo descrittivo
    description_text = (
        "Ganimede è la luna più grande di Giove e si trova a una distanza media di circa 1.070.400 km da Giove. "
        "Il diametro di Ganimede è di circa 5.268 km, maggiore di quello di Mercurio, ed è la luna più grande del sistema solare. Un giorno su Ganimede dura circa 7.2 giorni terrestri. "
        "Un anno su Ganimede (periodo orbitale) dura circa 7.2 anni terrestri. La gravità sulla superficie di Ganimede è circa 0.15 volte quella terrestre. "
        "La temperatura su Ganimede è estremamente bassa, con una media di circa -160°C. Tuttavia, la luna potrebbe possedere un oceano sotto la sua superficie ghiacciata. "
        "Ganimede ha una sottile atmosfera composta principalmente da ossigeno, ma troppo sottile per supportare la vita. "
        "La superficie di Ganimede è ricoperta da ghiaccio, con caratteristiche geologiche come crateri, pianure e evidenti segni di attività tettonica passata. "
        "Ganimede è un obiettivo importante per la ricerca spaziale grazie alla possibilità di un oceano sotterraneo e per il suo magnetismo intrinseco. "
        "Ganimede è visibile solo con un telescopio, ma è stato studiato da missioni come Galileo e Juno, che hanno rivelato dettagli importanti sulla sua struttura."
    )
    
    # Crea un widget Text per il testo descrittivo all'interno dello stesso frame ombreggiato
    text_widget = tk.Text(text_frame, wrap="word", height=12, width=70, font=("Courier New", 10), bg="#2B2B2B", fg="#FFFFFF", bd=0)
    text_widget.insert(tk.END, description_text)
    text_widget.config(state=tk.DISABLED)  # Rende il testo non modificabile
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)  # Aggiungi del padding interno al widget Text

    # Pulsante per il link esterno
    open_link_button = tk.Button(ganimede_window, text="Scopri di più su Ganimede", command=open_browser_link, bg="#FF6347", fg="white", font=("Helvetica", 12, "bold"))
    open_link_button.pack(pady=20)

    # Gestione della chiusura
    ganimede_window.protocol("WM_DELETE_WINDOW", ganimede_window.destroy)
