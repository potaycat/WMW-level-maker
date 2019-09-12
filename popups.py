import tkinter as tk
from tkinter import ttk

def commingsoon():
    popup = tk.Tk()
    popup.wm_title('.')
    ttk.Label(popup, text="Comming Soon :)").pack()
    ttk.Button(popup, text="OK, cool", command = popup.destroy ).pack()
       

def about_dialog():
    popup = tk.Tk()
    popup.wm_title('About')
    ttk.Label(popup, text="Where's My Water Level Creator v0.0.1 pre-alpha release").pack()
    ttk.Label(popup, text='Brought to you by Long Nguyễn').pack()
    ttk.Label(popup, text="note that I have no association with WMW's creators or whosoever").pack()
    ttk.Button(popup, text="Close", command = popup.destroy ).pack()
    
