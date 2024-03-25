import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")

btn1 = tk.Button(root, text="버튼1")
btn1.pack()

btn2 = tk.Button(root, padx=10, pady=30, text="버튼2")
btn2.pack()

btn3 = tk.Button(root, padx=30, pady=10, text="버튼3")
btn3.pack()

btn4 = tk.Button(root, width=20, height=5, text="버튼4")
btn4.pack()

btn5 = tk.Button(root, fg="yellow", bg="red", text="버튼5")
btn5.pack()

btn_image = tk.PhotoImage(file="btn-img.png")
btn6 = tk.Button(root, image=btn_image)
btn6.pack()

def btncmd():
  print("버튼이 클릭되었어요")

btn7 = tk.Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()