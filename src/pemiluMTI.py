"""
CREATOR:
    Rehan Adi Satrya, Teknik Informatika 2018, 13518061
    Institut Teknologi Bandung

For Bussiness Enquiries, contact:
    ID LINE: rehanadi30
    Phone Numbers: +62 858 9423 4755
    Email: rehanadi457@gmail.com / 13518061@std.stei.itb.ac.id
"""



#===================================================================================
from tkinter import *
from tkinter.ttk import * 
import os, os.path
from tkinter.ttk import *
from PIL import ImageTk, Image #buat naro gambar
import csv
import tkinter.font
from tkinter import messagebox
from tkinter import simpledialog
import hashlib
import subprocess, platform #buat bersihin terminal
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#SPESIFIKASI WINDOW UTAMA
class FullScreenApp(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
   

    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Pemilu MTI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a vote button
        voteMonica = Button(kanvasUtama, text="MUHAMMAD REYHAN\n13417071", style = 'W.TButton', command=vote1, width = 50)
        voteReyhan = Button(kanvasUtama, text="MONICA CORY ANGEL\n13417102", style = 'W.TButton', command=vote2, width = 50)
        voteKotakKosong = Button(kanvasUtama, text="ABSTAIN", style = 'W.TButton', command=vote3, width = 50)


        # placing vote button 
        voteMonica.place(x=100, y= 650, height=50)
        voteKotakKosong.place(x=600,y= 650, height=50)
        voteReyhan.place(x=1100, y = 650, height=50)
#----------------------------------------------
        #Buat gambar

        #Gambar Reyhan
        load = Image.open('Foto rey png.png')
        render = ImageTk.PhotoImage(load)

        img = Label(kanvasUtama, image=render, borderwidth=0)
        img.image = render
        img.place(x = 100, y = 200)

        #Gambar Kotak Kosong
        load = Image.open('KotakKosong.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(kanvasUtama, image=render, borderwidth=0)
        img.image = render
        img.place(x = 600, y = 200)

        #gambar Cory
        load = Image.open('Foto Cory png.png')
        render = ImageTk.PhotoImage(load)

        img = Label(kanvasUtama, image=render, borderwidth=0)
        img.image = render
        img.place(x = 1100, y = 200)
        

#-------------------------------------------------
def bersihinTerminal():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate() #Biar terminal bersih 
    else: #Linux and Mac
        print("\033c", end="")

#-------------------------------------------------
#Kalo ngevote siapa masuk kemana
def vote1(): #memilih nomor urut 1
    answer = messagebox.askokcancel('Konfirmasi', 'Kamu yakin akan memilih Muhammad Reyhan?? Jika sudah menenekan "OK" kamu tidak akan bisa mengubah pilihanmu lagi')
    if answer:
        messagebox.showinfo('Apresiasi', 'Terima kasih sudah memilih!!!')
        root.destroy()
        row = ['1','0','0']
        with open('pemilu.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        bersihinTerminal()
        print("Vote recorded Succesfully")

def vote2(): #memilih nomor urut 2
    answer = messagebox.askokcancel('Konfirmasi', 'Kamu yakin akan memilih Monica Cory Angel?? Jika sudah menenekan "OK" kamu tidak akan bisa mengubah pilihanmu lagi')
    if answer:
        messagebox.showinfo('Apresiasi', 'Terima kasih sudah memilih!!!')
        root.destroy()
        row = ['0','1','0']
        with open('pemilu.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        bersihinTerminal()
        print("Vote recorded Succesfully")

def vote3(): #memilih nomor urut 3
    answer = messagebox.askokcancel('Konfirmasi', 'Kamu yakin akan memilih Kotak Kosong?? Jika sudah menenekan "OK" kamu tidak akan bisa mengubah pilihanmu lagi')
    if answer:
        messagebox.showinfo('Apresiasi', 'Terima kasih sudah memilih!!!')
        root.destroy()
        row = ['0','0','1']
        with open('pemilu.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        bersihinTerminal()
        print("Vote recorded Succesfully")

#---------------------------------------------

#Memanggil fungsi utama

token = input("Masukkan token Panitia : ")
if (token == 'pemiluskuy'):
    root = Tk()
    kanvasUtama = Canvas(width=1920, height=1080,bd=-2, bg="sky blue")
    belakang=ImageTk.PhotoImage(Image.open('logoMTI.jpg'))
    kanvasUtama.create_image(0,0,anchor=NW,image=belakang)
    kanvasUtama.pack()

    #style
    style = Style()
    style.configure('W.TButton', font =('verdana',22, 'bold'), background = 'blue', foreground = 'black', bordercolor="blue") 
    style.theme_use('clam')

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    app = FullScreenApp(root)
    root.mainloop()
else:
    bersihinTerminal()
    print("Salah Woy!!")



