import os
from PIL import Image, ImageTk
import tkinter as tk

def show_information(root):
    info_window = tk.Toplevel(root)
    info_window.title("Informazioni")
    info_window.geometry("480x200")
    info_window.configure(bg='#2B2B2B')  
    info_window.resizable(False, False)
    info_window.attributes('-topmost', True) 

    icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')  
    print("Icon path:", icon_path)  
    try:
        info_window.iconbitmap(icon_path) 
    except Exception as e:
        print(f"Errore durante il caricamento dell'icona: {e}")


    main_frame = tk.Frame(info_window, bg="#3B3B3B")  
    main_frame.pack(padx=20, pady=20, fill="both", expand=True)

    logo_path = os.path.join(os.path.dirname(__file__), "images", "logo.png")
    if os.path.exists(logo_path):
        logo_image = Image.open(logo_path).resize((80, 80), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        info_window.logo_photo = logo_photo 

        logo_label = tk.Label(main_frame, image=info_window.logo_photo, bg="#3B3B3B")
        logo_label.pack(side="left", padx=10, pady=10)
    else:
        print("Logo non trovato.")

    info_text = (
        "AstroWeight\n"
        "© 2024 AstroWeight.\n"
        "Tutti i diritti riservati.\n"
        "Versione 1.0.0\n"
        "\nCreated by Antonino Brosio & Antonella Tripodi"
    )

    info_label = tk.Label(
        main_frame,
        text=info_text,
        font=("Helvetica", 10),
        fg="#FFFFFF",
        bg="#3B3B3B",
        justify="left"
    )
    info_label.pack(side="right", padx=20, pady=0)

    root.mainloop()
