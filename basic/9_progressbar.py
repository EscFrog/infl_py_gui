import tkinter.ttk as ttk
import tkinter as tk
import time

root = tk.Tk()
root.title("escfrog GUI")
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10) # 10ms 마다 움직임
progressbar.pack()

p_var2 = tk.DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd():
  progressbar.stop() # 작동 중지

btn = tk.Button(root, text="중지", command=btncmd)
btn.pack()

def btncmd2():
  for i in range(1, 101):
    time.sleep(0.01) # 0.01초 대기
    
    p_var2.set(i) # progress bar의 값 설정
    progressbar2.update() # ui 업데이트
    print(p_var2.get())

btn2 = tk.Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()