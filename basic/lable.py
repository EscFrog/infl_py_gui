import tkinter as tk

root = tk.Tk()
root.title("escfrog GUIx")
root.geometry("640x480")

label1 = tk.Label(root, text="레이블1")
label1.pack()

photo = tk.PhotoImage(file="basic/btn-img.png")
label2 = tk.Label(root, image=photo)
label2.pack()

def change():
  label1.config(text="또 만나요")

btn = tk.Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()