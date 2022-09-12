import tkinter as tk
import sys
from tkinter import font as tkfont
from tkinter import messagebox as msgbox
from tkinter import filedialog as filed
from PIL import ImageTk, Image
from slimole_clean import run

class Default(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        top = tk.Frame(self)
        self.title("Projekt grupowy")
        top.pack(side = "top", fill="none", expand = True)
        top.grid_rowconfigure(0, minsize = 900, weight = 1)
        top.grid_columnconfigure(0, minsize = 1500, weight = 1)

        self.frames={}
        for F in (Welcomep, Mainp, Resultp):
            frame = F(top, self)
            self.frames[F] = frame
            self.frames[F].grid(row=0, column=0, sticky = "nsew")
        self.show_frame(Welcomep)

    #uruchamianie poszczególnych okienek
    def show_frame(self, cont, img_name = None):
        frame = self.frames[cont]
        if type(frame) is Resultp:
            frame.draw(img_name)
        #frame.pack(fill="both", expand=1)
        frame.tkraise()


class Welcomep(tk.Frame):

    def __init__(self, parent, controller): #, height, width, bg):
        tk.Frame.__init__(self, parent)
        #inicjowane widgety
        label_font = tkfont.Font(family = "Times", size = "36", weight = "bold")
        button_font = tkfont.Font(family="Times", size="16", weight="bold")
        label = tk.Label(self, text="Snails\n&\nSlugs", font = label_font, fg = "#7CB342")
        label.place(x = 610, y = 300)

        next = tk.Button(self, text="Rozpocznij",
                               command=lambda: controller.show_frame(Mainp),
                               width = 20,
                               bg = "#196F3D",
                               fg = "#E9F7EF",
                               font = button_font)
        next.place(x = 550, y = 600)


class Mainp(tk.Frame):

    def __init__(self, parent, controller): #, height, width, bg):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        button_font = tkfont.Font(family="Times", size="16", weight="bold")
        #inicjowane widgety
        add_img = tk.Button(self, text="Otwórz obraz z pliku",
                                  command=self.browse_files,
                                  width=25,
                                  bg = "#196F3D",
                                  fg="#E9F7EF",
                                  font=button_font)
        add_img.place(x=1000, y = 300)

        self.next_win = tk.Button(self, text="Wyszukaj",
                                  command=lambda: self.show_results(),
                                  state="disabled",
                                  width=25,
                                  bg = "#196F3D",
                                  fg="#E9F7EF",
                                  font=button_font)
        self.next_win.place(x = 1000, y = 500)

        self.filename = None
        self.placeholder = tk.Label(self, text="Nie wybrano obrazu")
        self.placeholder.place(x = 50, y = 50)

    #funkcje buttonów
    #funkcja do wyswietlania obrazu
    def show_image(self):
        img = Image.open(self.filename)
        img1 = ImageTk.PhotoImage(img)

        self.placeholder.configure(image=img1, height = 800, width = 800)
        self.placeholder.image = img1
        img.close()
        self.next_win["state"] = "normal"
    #funkcja do uploadu zdjęcia
    def browse_files(self):
        self.filename = filed.askopenfilename(initialdir="/",
                                         title="Wybierz obraz...",
                                         filetypes=(
                                             ("Pliki JPG", "*.jpg*"),
                                            ("Pliki PNG", "*.png*")
                                         ))

        self.show_image()

    #startuje skrypt rozpoznawania slimakow
    def show_results(self):
        return_img = run(self.filename)
        self.controller.show_frame(Resultp, return_img)



class Resultp(tk.Frame):
    def __init__(self, parent, controller): #, height, width, bg):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        button_font = tkfont.Font(family="Times", size="16", weight="bold")

        #inicjowane widgety
        self.placeholder = tk.Label(self, text="")
        self.placeholder.place(x = 50, y = 50)

        back_win = tk.Button(self, text="Wykonaj ponownie",
                                   command=lambda: controller.show_frame(Mainp),
                                   width=25,
                                   bg = "#196F3D",
                                   fg="#E9F7EF",
                                   font=button_font)
        back_win.place(x = 1000, y = 300)

        exitb = tk.Button(self, text="Zakończ",
                               command=lambda: app.destroy(),
                               width=25,
                               bg = "#196F3D",
                               fg = "#E9F7EF",
                               font = button_font)
        exitb.place(x = 1000, y = 500)
    #wyświetlanie obrazu
    def draw(self, img_name):
        if img_name is not None:
            img = Image.open(img_name)
            img1 = ImageTk.PhotoImage(img)
            self.placeholder.configure(image=img1, height = 800, width = 800)
            self.placeholder.image = img1

app = Default()
app.mainloop()
