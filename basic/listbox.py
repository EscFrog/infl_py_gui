import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

# selectmode : 하나만 선택하게 할 것인가, 여러개를 선택할 수 있게 할 것인가?
# height : 0으로 두면 모든 목록이 보인다. 숫자를 입력하면 그 숫자에 해당하는 개수까지만 보인다
listbox = tk.Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(tk.END, "수박")
listbox.insert(tk.END, "포도")
listbox.pack()

def btncmd():
  # 삭제
  # listbox.delete(tk.END) # 맨 뒤의 항목을 삭제
  # listbox.delete(0) # 맨 앞의 항목을 삭제

  # 개수 확인
  print("리스트에는", listbox.size(), "개가 있어요")

  # 항목 확인
  print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

  # 선택된 항목 확인
  print("선택된 항목 : ", listbox.curselection())


btn = tk.Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()