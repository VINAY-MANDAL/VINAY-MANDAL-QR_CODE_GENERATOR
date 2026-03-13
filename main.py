import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    
    if data == "":
        status.config(text="Enter some text or number")
        return
    
    img = qrcode.make(data)
    img.save("temp_qr.png")

    preview = Image.open("temp_qr.png")
    preview = preview.resize((200,200))

    img_tk = ImageTk.PhotoImage(preview)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    status.config(text="QR Code Generated")

def save_qr():
    file = filedialog.asksaveasfilename(defaultextension=".png")
    if file:
        img = qrcode.make(entry.get())
        img.save(file)
        status.config(text="QR Code Saved")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x400")

title = tk.Label(root, text="QR Code Generator", font=("Arial",16))
title.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

btn_generate = tk.Button(root, text="Generate QR", command=generate_qr)
btn_generate.pack(pady=5)

btn_save = tk.Button(root, text="Save QR", command=save_qr)
btn_save.pack(pady=5)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

status = tk.Label(root, text="")

status.pack()
root.mainloop()