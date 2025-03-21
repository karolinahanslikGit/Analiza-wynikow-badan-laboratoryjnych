import tkinter as tk
import os
from tkinter import PhotoImage
from tkinter import filedialog
import time
from tkinter import messagebox
from plikGlowny import ProgramGlowny
class Aplikacja:
    def __init__(self,root):
        self.programGlowny=ProgramGlowny()
        root.title('Aplikacja do analizy wyników badań laboratoryjnych krwi i moczu.')
        root.geometry('400x400')
        root.resizable(False,False)
        root.config(bg="#f8efed")
        text=tk.Label(root,text='Wprowadż plik z wynikami badań laboratoryjnych \n w formacie .pdf oraz dane pacjenta',bg='#f8efed',font=('Arial',12,'bold'),fg='#4c1949')
        text.grid(row=0,column=0,columnspan=2,pady=20,padx=5)
        text.grid_columnconfigure(0,weight=1)
        text.grid_rowconfigure(0,weight=0)
        imieLabel=tk.Label(root,text='Imię:',bg='#f8efed',font=('Arial',12,''),fg='#81b1ff')
        imieLabel.grid(row=1,column=0,sticky='w',padx=(25,0))
        nazwiskoLabel=tk.Label(root,text='Nazwisko:',bg='#f8efed',font=('Arial',12,''),fg='#81b1ff')
        nazwiskoLabel.grid(row=1,column=1,sticky='w',padx=(45,0))
        self.imie=tk.Entry(root,width=20)
        self.imie.grid(row=2,column=0)
        self.nazwisko=tk.Entry(root,width=20)
        self.nazwisko.grid(row=2,column=1)

        peselLabel=tk.Label(root,text='PESEL:',bg='#f8efed',font=('Arial',12,''),fg='#81b1ff')
        peselLabel.grid(row=3,column=0,pady=(20,0),sticky='w',padx=(25,0))
        self.dataUrLabel=tk.Label(root,text='Data Urodzenia:',bg='#f8efed',font=('Arial',12,''),fg='#81b1ff')
        self.dataUrLabel.grid(row=3,column=1,pady=(20,0),sticky='w',padx=(45,0))
        self.pesel=tk.Entry(root,width=20)
        self.pesel.grid(row=4,column=0)
        self.dataUr=tk.Entry(root,width=20)
        self.dataUr.grid(row=4,column=1)
        wgrajZdj=PhotoImage(file='ilustracje\wgrajButton.png')
        wgrajButton=tk.Button(root,image=wgrajZdj,takefocus=False,activebackground="#f8efed",command=self.DodajPlik,borderwidth=0,bg="#f8efed")
        wgrajButton.grid(row=5,column=0,columnspan=2,pady=(20,0),padx=(0,10))
    
        self.generowanieLabel=tk.Label(root,text="",bg='#f8efed',font=('Arial',12,''),fg='#800000')
        self.nazwaPlikuLabel=tk.Label(root,text="",bg='#f8efed',font=('Arial',12,''),fg='#800000')
        self.generowanieLabel.grid(row=6,column=0,columnspan=2,sticky='w',pady=(10,0),padx=10)
        self.nazwaPlikuLabel.grid(row=7,column=0,columnspan=2,sticky='e',pady=(10,0),padx=10)
        root.mainloop()
   
    def UruchomMain(self,sciezkaPliku):

            

            if(self.programGlowny.SprawdzeniePliku(sciezkaPliku)==True):
                self.programGlowny.AnalizaPliku(sciezkaPliku,self.imie.get(),self.nazwisko.get(),self.pesel.get(),self.dataUr.get())
                self.generowanieLabel.configure(text='Raport został wygenerowany')
            else:
                    self.generowanieLabel.configure(text="Błąd")

                    messagebox.showerror('Error','Nieobsługiwany typ pliku')
    def DodajPlik(self):
    
        initial_dir = os.path.expanduser("~/Desktop")
        sciezkaPliku = filedialog.askopenfilename(initialdir=initial_dir, title="Wybierz plik",filetypes=[('Pliki PDF','*.pdf')])
        if(sciezkaPliku!=''):
            s=os.path.basename(sciezkaPliku)
            self.generowanieLabel.configure(text='Gerowanie raportu ...')
            self.nazwaPlikuLabel.configure(text=f"Wybrany plik: {s}")
            
            try:
                root.after(1000,self.UruchomMain,sciezkaPliku)
                
            except:
                self.generowanieLabel.configure(text="Błąd")
                messagebox.showerror('Error','Nieobsługiwany typ pliku')
root =tk.Tk()
aplikacja=Aplikacja(root)
root.mainloop()
        
    
    
   