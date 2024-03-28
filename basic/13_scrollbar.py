import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")
root.geometry("640x480+400+400") # 가로 크기, 세로 크기, x좌표, y좌표

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# yscrollcommand 부분이 리스박스에 스크롤바를 매핑해주는 부분.
# 이 부분이 없으면 스크롤을 내려도 다시 올라옴
listbox = tk.Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
  listbox.insert(tk.END, str(i) + "일")
listbox.pack(side="left")

 # 스크롤바에 리스트박스를 매핑.
 # 이 부분이 없으면 스크롤바를 움직여도 리스트박스가 움직이지 않는다.
scrollbar.config(command=listbox.yview)

root.mainloop()