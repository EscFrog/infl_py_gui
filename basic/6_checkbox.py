import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

# 체크 박스에는 변수가 반드시 필요함
chkvar = tk.IntVar() # Tkinter에서 사용할 int형 변수를 선언하는 방법.
chkbox = tk.Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()


chkvar2 = tk.IntVar()
chkbox2 = tk.Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
  print(chkvar.get()) # 0 : 체크 해제 상태, 1 : 체크 상태
  print(chkvar2.get()) # 0 : 체크 해제 상태, 1 : 체크 상태

btn = tk.Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()