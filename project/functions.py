from tkinter import filedialog, END, messagebox

# 파일 추가
def add_file(listbox_file):
  files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), initialdir="/Users/*/Pictures")

  # 사용자가 선택한 파일 목록
  for file in files:
    listbox_file.insert(END, file)


# 선택 삭제
def del_file(listbox_file):
  for index in reversed(listbox_file.curselection()):
    listbox_file.delete(index)


# 저장 경로 (폴더)
def browse_dest_path(txt_dest_path):
  folder_selected = filedialog.askdirectory(initialdir="/Users/*/Pictures")
  if folder_selected is None:
    return
  # print(folder_selected)
  txt_dest_path.delete(0, END)
  txt_dest_path.insert(0, folder_selected)


# 병합 시작
def start(cmb_width, cmb_space, cmb_format, listbox_file, txt_dest_path):
  # 각 옵션들 값을 확인
  print("가로넓이 : ", cmb_width.get())
  print("간격 : ", cmb_space.get())
  print("포맷 : ", cmb_format.get())

  # 파일 목록 확인
  if listbox_file.size() == 0:
    messagebox.showwarning("경고", "이미지 파일을 추가하세요")
    return
  
  # 저장 경로 확인
  if len(txt_dest_path.get()) == 0:
    messagebox.showwarning("경고", "저장 경로를 선택하세요")
    return
