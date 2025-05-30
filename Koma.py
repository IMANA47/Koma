from tkinter import *
from tkinter import messagebox, filedialog


class Koma:
    def __init__(self, master):
        self.master = master
        self.filename = None
    def creat_window(self):
        self.master.title("Koma - Editeur de texte")
        self.master.geometry("1200x700")

    # Methode Pour zone de texte
    def creat_textrea(self):
        self.textrea = Text(self.master, font=("Arial", 13))
        self.textrea.pack(side=LEFT,fill=BOTH, expand=True)

        self.scroll = Scrollbar(self.master, command= self.textrea.yview())
        self.textrea.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)

    # Methode pour ouvrire document
    def new_document(self):
        if len(self.textrea.get(1.0, END+ '-1c')) >0:
            message_save = messagebox.askyesno("Koma", "L'editeur va quitter le document, voulez vous l'enregistrer ? " )

            if message_save > 0:
                self.save()
        self.textrea.delete(1.0, END)


    #Methode pour ouvrire document
    def open_document(self):
        if len(self.textrea.get(1.0, END+ '-1c')) >0:
            message_save = messagebox.askyesno("Koma", "Voulez-vous enregistrer les modifications du document ? " )

            #Si il choisi oui
            if message_save >0:
                self.save()
            self.textrea.delete(1.0, END)

        self.filename = filedialog.askopenfilename(initialdir="/",title="Ouvrir un document",
                                            defaultextension=".txt",
                                            filetypes=[('Fichier texte', '*.txt'),('Script python', '*.py'),
                                                       ('Fichier html', '*.html'),('Fichier javascript', '*.js'),
                                                       ('Fichier css', '*.css'),('Fichier PhP', '*.php'),('Tous fichiers', '*.*')])

        if self.filename:
            try:
                file = open(self.filename, 'r')
                fr = file.read()
                file.close()
                self.textrea.insert("1.0", fr)

            except Exception as e:
                (messagebox.showerror("Ouvrir document", e))








    def save_as(self):
        try:
            file = filedialog.asksaveasfile(initialdir="/",title="Enregistrer sous", initialfile="Koma",
                                            defaultextension=".txt",
                                            filetypes=[('Fichier texte', '*.txt'),('Script python', '*.py'),
                                                       ('Fichier html', '*.html'),('Fichier javascript', '*.js'),
                                                       ('Fichier css', '*.css'),('Fichier PhP', '*.php'),('Tous fichiers', '*.*')])

            content_file = self.textrea.get(1.0, END)
            if file:
                f = open(file, "w")
                f.write(content_file)
                f.close()
                self.filename = file
        except Exception as e:
            messagebox.showerror("Exception", e)

    def save(self):
        if self.filename:
            try:
                content_file = self.textrea.get(1.0, END)
                with open(self.filename, "w") as f:
                    f.write(content_file)
            except Exception as e:
                messagebox.showerror("Exception", e)
        else:
            self.save_as()


    # Methode fermer document
    def close_document(self):
        if len(self.textrea.get(1.0, END+ '-1c')) > 0:
            save = messagebox.askyesno("Enrefistrer", "Voulez vous enregistrer votre document ?")
            if save <=0:
                self.textrea.quit()
            else:
                self.save()
                self.textrea.quit()
        else:
            self.textrea.quit()

    #Methode copy
    def copy(self):
        self.textrea.event_generate("<<Copy>>")

    # Methode coller
    def cut(self):
        self.textrea.event_generate("<<Cut>>")
        # Methode paste
    def paste(self):
        self.textrea.event_generate("<<Paste>>")

    def selectAll(self):
        self.textrea.event_generate("<<SelectAll>>")



    def add_menu(self):
        barMenu = Menu(self.master)
        self.master.config(menu=barMenu)

        # Menu fichier
        filesMenu = Menu(barMenu, font=("Arial", 13), tearoff=False)
        filesMenu.add_command(label="Nouveau document",accelerator="Ctrl+N", command=self.new_document)
        filesMenu.add_command(label="Ouvrir",accelerator="Ctrl+O", command=self.open_document)
        filesMenu.add_separator()
        filesMenu.add_command(label="Enregistrer sous",accelerator="Ctrl+Shift+S", command=self.save_as)
        filesMenu.add_command(label="Enregistrer",accelerator="Ctrl+S", command=self.save)
        filesMenu.add_separator()
        filesMenu.add_command(label="Fermer",accelerator="Ctrl+F", command=self.close_document)
        barMenu.add_cascade(label="Fichier", menu=filesMenu)


        # Edition menu
        editionMenu = Menu(barMenu, font=("Arial", 13), tearoff=False)

        editionMenu.add_command(label="Copier",accelerator="Ctrl+C", command=self.copy)
        editionMenu.add_command(label="Couper",accelerator="Ctrl+X", command=self.cut)
        editionMenu.add_separator()
        editionMenu.add_command(label="Coller",accelerator="Ctrl+V", command=self.paste)
        editionMenu.add_separator()
        editionMenu.add_command(label="Selectionner tout",accelerator="Ctrl+A", command=self.selectAll)
        barMenu.add_cascade(label="Edition", menu=editionMenu)

        # Menu Aide
        # aideMenu = Menu(barMenu, font=("Arial", 13), tearoff=False)
        # aideMenu.add_command(label="Afficher l'aide", command=self.copy)
        # aideMenu.add_command(label="Envoyer des commentaires", command=self.cut)
        # aideMenu.add_separator()
        # aideMenu.add_command(label="A propos de Koma", command=self.paste)
        # barMenu.add_cascade(label="Aide", menu=aideMenu)


if __name__ == "__main__":
    master = Tk()
    editeur = Koma(master)
    editeur.creat_window()
    editeur.creat_textrea()
    editeur.add_menu()
    master.mainloop()
