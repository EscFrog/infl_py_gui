import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")
# root.geometry("640x480+300+300") # 가로 크기, 세로 크기, x좌표, y좌표
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()