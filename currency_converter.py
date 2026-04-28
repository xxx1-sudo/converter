import tkinter as tk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("300x250")

        # Label
        self.label = tk.Label(root, text="Betrag eingeben:")
        self.label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

    
        self.btn_eur_usd = tk.Button(root, text="EUR → USD", command=self.eur_to_usd)
        self.btn_eur_usd.pack(pady=5)

        self.btn_usd_eur = tk.Button(root, text="USD → EUR", command=self.usd_to_eur)
        self.btn_usd_eur.pack(pady=5)

        # Output
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def eur_to_usd(self):
        try:
            amount = float(self.entry.get())
            result = amount * 1.09  # fixer Kurs
            self.output_label.config(text=f"{result:.2f} USD")
        except ValueError:
            self.output_label.config(text="Bitte gültige Zahl eingeben")

    def usd_to_eur(self):
        try:
            amount = float(self.entry.get())
            result = amount * 0.92  # fixer Kurs
            self.output_label.config(text=f"{result:.2f} EUR")
        except ValueError:
            self.output_label.config(text="Bitte gültige Zahl eingeben")


if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()