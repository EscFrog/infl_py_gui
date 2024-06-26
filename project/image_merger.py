import tkinter as tk
import tkinter.ttk as ttk
from options import GUIElements
import functions as fc

root = tk.Tk()
root.title("escfrog image merger")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = tk.Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = tk.Button(file_frame, padx=5, pady=5, width=10, text="파일추가", command=lambda: fc.add_file(listbox_file))
btn_add_file.pack(side="left")

btn_del_file = tk.Button(file_frame, padx=5, pady=5, width=10, text="선택삭제", command=lambda: fc.del_file(listbox_file))
btn_del_file.pack(side="right") 

# 리스트 프레임
list_frame = tk.Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

listbox_file = tk.Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
listbox_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox_file.yview)

# 저장 경로 프레임
path_frame = tk.LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = tk.Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = tk.Button(path_frame, text="찾아보기", width=10, command=lambda: fc.browse_dest_path(txt_dest_path))
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = tk.LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = tk.Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = tk.Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = tk.Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Progress Bar
frame_progress = tk.LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x",padx=5, pady=5, ipady=5)

p_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = tk.Frame(root)
frame_run.pack(fill="x",padx=5, pady=5)

btn_close = tk.Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

# GUI 요소 인스턴스 생성
gui_elements = GUIElements(listbox_file, txt_dest_path, progress_bar, p_var)

btn_start = tk.Button(frame_run, padx=5, pady=5, text="시작", width=12, command=lambda: fc.start(cmb_width.get(), cmb_space.get(), cmb_format.get(), gui_elements))
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()