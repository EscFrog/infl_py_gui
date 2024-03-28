import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

# 맨 윗줄
btn_f16 = tk.Button(root, text="F16", padx=5, pady=20)
btn_f17 = tk.Button(root, text="F17", padx=5, pady=20)
btn_f18 = tk.Button(root, text="F18", padx=5, pady=20)
btn_f19 = tk.Button(root, text="F19", padx=5, pady=20)

btn_f16.grid(row=0, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)

# clear 줄
btn_clear = tk.Button(root, text="clear", padx=5, pady=20)
btn_equal = tk.Button(root, text="=", padx=5, pady=20)
btn_div = tk.Button(root, text="/", padx=5, pady=20)
btn_mul = tk.Button(root, text="*", padx=5, pady=20)

btn_clear.grid(row=1, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)

# 7 시작 줄
btn_7 = tk.Button(root, text="7", padx=5, pady=20)
btn_8 = tk.Button(root, text="8", padx=5, pady=20)
btn_9 = tk.Button(root, text="9", padx=5, pady=20)
btn_sub = tk.Button(root, text="-", padx=5, pady=20)

btn_7.grid(row=2, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)

# 4 시작 줄
btn_4 = tk.Button(root, text="4", padx=5, pady=20)
btn_5 = tk.Button(root, text="5", padx=5, pady=20)
btn_6 = tk.Button(root, text="6", padx=5, pady=20)
btn_add = tk.Button(root, text="+", padx=5, pady=20)

btn_4.grid(row=3, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)

# 1 시작 줄
btn_1 = tk.Button(root, text="1", padx=5, pady=20)
btn_2 = tk.Button(root, text="2", padx=5, pady=20)
btn_3 = tk.Button(root, text="3", padx=5, pady=20)
btn_enter = tk.Button(root, text="enter", padx=5, pady=20)

btn_1.grid(row=4, column=0, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3) # 현재 위치로부터 아래쪽으로 몇 줄을 더함.

# 0 시작 줄
btn_0 = tk.Button(root, text="0", padx=5, pady=20)
btn_dot = tk.Button(root, text=".", padx=5, pady=20)

btn_0.grid(row=5, column=0, columnspan=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)  # 현재 위치로부터 오른쪽으로 몇 칸을 더함.
btn_dot.grid(row=5, column=2, sticky=tk.N+tk.W+tk.E+tk.S, padx=3, pady=3)




root.mainloop()