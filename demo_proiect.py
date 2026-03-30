import tkinter as tk
from tkinter import messagebox

class FashionAppDemo:
    def _init_(self, root):
        self.root = root
        self.root.title("Netflix AI Fashion Finder - Prototip")
        self.root.geometry("600x400")
        self.root.configure(bg="#141414") # Culoarea Netflix

        # Simulare ecran video
        self.video_frame = tk.Frame(root, bg="#333", width=560, height=300)
        self.video_frame.pack(pady=20)
        
        self.label = tk.Label(self.video_frame, text="[ CADRU DIN SERIAL ]", 
                              fg="white", bg="#333", font=("Arial", 14))
        self.label.place(relx=0.5, rely=0.5, anchor="center")

        # Butonul magic
        self.scan_btn = tk.Button(root, text="🔍 SCAN OUTFIT", bg="#E50914", fg="white", 
                                  font=("Arial", 10, "bold"), command=self.start_scan)
        self.scan_btn.pack()

    def start_scan(self):
        # Efect vizual de scanare
        self.scan_btn.config(text="SCANNING...", state="disabled")
        self.root.after(1500, self.show_results)

    def show_results(self):
        # Fereastra de rezultate
        result_win = tk.Toplevel(self.root)
        result_win.title("Haine Găsite")
        result_win.geometry("300x250")
        result_win.configure(bg="white")

        tk.Label(result_win, text="AI a găsit 2 produse:", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        
        items = [
            "🧥 Palton Lână - Burberry (950€)",
            "🕶️ Ochelari - Ray-Ban (150€)"
        ]

        for item in items:
            tk.Label(result_win, text=item, bg="white", fg="black").pack(pady=5)

        tk.Button(result_win, text="Adaugă în coș", bg="black", fg="white").pack(pady=20)
        
        self.scan_btn.config(text="🔍 SCAN OUTFIT", state="normal")

# Pornire aplicație
if _name_ == "_main_":
    root = tk.Tk()
    app = FashionAppDemo(root)
    root.mainloop()
