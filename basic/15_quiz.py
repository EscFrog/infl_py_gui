import os
import tkinter as tk

root = tk.Tk()
root.title("escfrog notepad")
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

# 열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
  if os.path.isfile(filename): # 파일이 있으면 True, 없으면 False
    with open(filename, "r", encoding="utf8") as file:
      txt.delete("1.0", tk.END)
      txt.insert(tk.END, file.read())

def save_file():
  with open(filename, "w", encoding="utf8") as file:
    file.write(txt.get("1.0", tk.END)) # 모든 내용을 가져와서 저장

menu = tk.Menu(root)

# 파일 메뉴
menu_file = tk.Menu(root, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Quit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# 편집 메뉴
menu_edit = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=menu_edit)

# 서식 메뉴
menu_form = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Form", menu=menu_form)

# 보기 메뉴
menu_view = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=menu_view)

# 도움말 메뉴
menu_help = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=menu_help)

# 스크롤 바
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
txt = tk.Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True)

# 스크롤바 매칭
scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()