import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

txt = tk.Text(root, width=30, height=5) # 여러 줄의 텍스트 입력
txt.pack()
txt.insert(tk.END, "글자를 입력하세요")

e = tk.Entry(root, width=30) # 한 줄짜리 테스트 입력
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
  # 내용 출력
  print(txt.get("1.0", tk.END)) # "1.0"의 의미는 "1 : 첫번째 라인, 0 : 0번째 글자"부터라는 뜻
  print(e.get()) # 엔트리에 있던 글자를 가져온다.

  # 내용 삭제
  txt.delete("1.0", tk.END)
  e.delete(0, tk.END)

btn = tk.Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()