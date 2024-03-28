import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

# 맨 윗줄
btn_f16 = tk.Button(root, text="F16")
btn_f17 = tk.Button(root, text="F17")
btn_f18 = tk.Button(root, text="F18")
btn_f19 = tk.Button(root, text="F19")

btn_f16.grid(row=0, column=0)
btn_f17.grid(row=0, column=1)
btn_f18.grid(row=0, column=2)
btn_f19.grid(row=0, column=3)

# clear 줄
btn_clear = tk.Button(root, text="clear")
btn_equal = tk.Button(root, text="=")
btn_div = tk.Button(root, text="/")
btn_mul = tk.Button(root, text="*")

btn_clear.grid(row=1, column=0)
btn_equal.grid(row=1, column=1)
btn_div.grid(row=1, column=2)
btn_mul.grid(row=1, column=3)

# 7 시작 줄
btn_7 = tk.Button(root, text="7")
btn_8 = tk.Button(root, text="8")
btn_9 = tk.Button(root, text="9")
btn_sub = tk.Button(root, text="-")

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

# 4 시작 줄
btn_4 = tk.Button(root, text="4")
btn_5 = tk.Button(root, text="5")
btn_6 = tk.Button(root, text="6")
btn_add = tk.Button(root, text="+")

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_add.grid(row=3, column=3)

# 1 시작 줄
btn_1 = tk.Button(root, text="1")
btn_2 = tk.Button(root, text="2")
btn_3 = tk.Button(root, text="3")
btn_enter = tk.Button(root, text="enter")

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_enter.grid(row=4, column=3, rowspan=2) # 현재 위치로부터 아래쪽으로 몇 줄을 더함.

# 0 시작 줄
btn_0 = tk.Button(root, text="0")
btn_dot = tk.Button(root, text=".")

btn_0.grid(row=5, column=0, columnspan=2)  # 현재 위치로부터 오른쪽으로 몇 칸을 더함.
btn_dot.grid(row=5, column=2)




root.mainloop()