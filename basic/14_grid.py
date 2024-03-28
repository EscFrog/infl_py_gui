import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

# 맨 윗줄
btn_f16 = tk.Button(root, text="F16", width=3, height=3)
btn_f17 = tk.Button(root, text="F17", width=3, height=3)
btn_f18 = tk.Button(root, text="F18", width=3, height=3)
btn_f19 = tk.Button(root, text="F19", width=3, height=3)

btn_f16.grid(row=0, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_f17.grid(row=0, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_f18.grid(row=0, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_f19.grid(row=0, column=3, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)

# clear 줄
btn_clear = tk.Button(root, text="clear", width=3, height=3)
btn_equal = tk.Button(root, text="=", width=3, height=3)
btn_div = tk.Button(root, text="/", width=3, height=3)
btn_mul = tk.Button(root, text="*", width=3, height=3)

btn_clear.grid(row=1, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_equal.grid(row=1, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_div.grid(row=1, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_mul.grid(row=1, column=3, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)

# 7 시작 줄
btn_7 = tk.Button(root, text="7", width=3, height=3)
btn_8 = tk.Button(root, text="8", width=3, height=3)
btn_9 = tk.Button(root, text="9", width=3, height=3)
btn_sub = tk.Button(root, text="-", width=3, height=3)

btn_7.grid(row=2, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_8.grid(row=2, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_9.grid(row=2, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_sub.grid(row=2, column=3, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)

# 4 시작 줄
btn_4 = tk.Button(root, text="4", width=3, height=3)
btn_5 = tk.Button(root, text="5", width=3, height=3)
btn_6 = tk.Button(root, text="6", width=3, height=3)
btn_add = tk.Button(root, text="+", width=3, height=3)

btn_4.grid(row=3, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_5.grid(row=3, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_6.grid(row=3, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_add.grid(row=3, column=3, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)

# 1 시작 줄
btn_1 = tk.Button(root, text="1", width=3, height=3)
btn_2 = tk.Button(root, text="2", width=3, height=3)
btn_3 = tk.Button(root, text="3", width=3, height=3)
btn_enter = tk.Button(root, text="enter", width=3, height=3)

btn_1.grid(row=4, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_2.grid(row=4, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_3.grid(row=4, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1) # 현재 위치로부터 아래쪽으로 몇 줄을 더함.

# 0 시작 줄
btn_0 = tk.Button(root, text="0", width=3, height=3)
btn_dot = tk.Button(root, text=".", width=3, height=3)

btn_0.grid(row=5, column=0, columnspan=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)  # 현재 위치로부터 오른쪽으로 몇 칸을 더함.
btn_dot.grid(row=5, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=1, pady=1)




root.mainloop()