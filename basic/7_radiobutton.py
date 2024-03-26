import tkinter as tk

root = tk.Tk()
root.title("escfrog GUI")
root.geometry("640x480") # 가로 크기, 세로 크기, x좌표, y좌표

tk.Label(root, text="메뉴를 선택하세요").pack()

burger_var = tk.IntVar()
btn_burger1 = tk.Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = tk.Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = tk.Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

tk.Label(root, text="음료를 선택하세요").pack()

drink_var = tk.StringVar()
btn_drink1 = tk.Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = tk.Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
  print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)
  print(drink_var.get()) # 음료 중 선택된 값을 출력

btn = tk.Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()